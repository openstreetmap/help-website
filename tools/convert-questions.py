#!usr/bin/env python3
#
# convert-questions.py
# Convert OSQA HTML questions to commonmark.
# Copyright 2020 Gerald Combs <gerald@wireshark.org>
#
# SPDX-License-Identifier: MIT
#

# To do:
# - Search?

from bs4 import BeautifulSoup

import argparse
import concurrent.futures
import html
import logging
import os
import os.path
import re
import subprocess
import sys
import time


class Question:
    def __init__(self, import_file):
        self.import_file = import_file
        (number, self.slug) = import_file.removesuffix('.html').split('.', maxsplit=2)
        self.number = int(number)
        self.title = None
        self.answers = 0
        self.accepted = False
        self.date = None
        self.lastmod = None


def exit_err(message):
    logging.critical(message)
    sys.exit(1)


def quote_toml(unquoted_str):
    return html.escape(unquoted_str, quote=True).replace('\\', '&#92;')


def convert_question(question, questions_dir, content_dir):
    with open(os.path.join(questions_dir, question.import_file), 'r', encoding='utf-8') as import_f:
        html_body = import_f.read()
    soup = BeautifulSoup(html_body, 'html.parser')
    question.title = quote_toml(soup.find('title').string).removesuffix(' - Wireshark Q&amp;A')
    q_description = quote_toml(soup.find('meta', {'name': 'description'})['content'])
    q_keywords = soup.find('meta', {'name': 'keywords'})['content']

    # div#CALeft contains the question and answers.
    q_content = soup.find('div', id='CALeft')

    # Number of answers
    question.answers = len(q_content.find_all('div', class_='answer-body'))
    # Accepted?
    if q_content.find('div', class_='answer accepted-answer'):
        question.accepted = True


    # Asked / answered / edited date div.post-update-info
    for pu_el in q_content.find_all('div', class_='post-update-info post-update-info-user'):
        prefixed_date = pu_el.find('p').get_text(strip=True)
        m = re.search('(asked|answered|edited) *(.*)', prefixed_date)
        timeval = time.strptime(m.group(2), "%d %b '%y, %H:%M")
        if m.group(1) == 'asked':
            question.date = timeval
        if question.lastmod is None or question.lastmod < timeval:
            question.lastmod = timeval
    for ca_el in q_content.find_all('span', class_='comment-age'):
        m = re.search('\((.*)\)', ca_el.get_text(strip=True))
        timeval = time.strptime(m.group(1), "%d %b '%y, %H:%M")
        if question.lastmod is None or question.lastmod < timeval:
            question.lastmod = timeval

    # Remove things we don't want.
    # active / oldest / newest / popular answers buttons
    for tabs_a_el in q_content.find_all('div', class_='tabsA'):
        tabs_a_el.decompose()
    # "permanent link" button
    for tabs_a_el in q_content.find_all(class_='action-link'):
        tabs_a_el.decompose()
    # "Your answer" form
    for form_el in q_content.find_all('form'):
        form_el.decompose()
    # Neutralize non-quesiton links, e.g. /tags/foo
    for dl_el in q_content.find_all('a', href=re.compile('^/.*')):
        if dl_el['href'].startswith('/questions/'):
            continue
        del dl_el['href']
        dl_el.name = 'span'

    # https://pandoc.org/MANUAL.html#markdown-variants
    pd_proc = subprocess.run([
            'pandoc',
            '--from=html+raw_html',
            '--to=commonmark',
            '--wrap=none',
        ],
        encoding='UTF-8',
        input=q_content.decode_contents(),
        capture_output=True
        )
    if pd_proc.returncode != 0:
        exit_err('pandoc returned {}'.format(pd_proc.returncode))
    cm_page = pd_proc.stdout

    md_question_dir = os.path.join(content_dir, str(question.number), question.slug)
    os.makedirs(md_question_dir)
#     with open(os.path.join(md_question_dir, '_index.md'), 'w', encoding='utf-8') as index_f:
#         index_f.write(f'''\
# +++
# transparent = true
# redirect_to = "questions/{question.number}/{question.slug}"
# +++
# ''')
#     with open(os.path.join(md_question_dir, 'index.md'), 'w', encoding='utf-8') as index_f:
#         index_f.write(f'''\
# +++
# template = "page-redirect.html"
# title = "{question.title}"
# [extra]
# redirect_to = "{question.number}/{question.slug}"
# +++
# ''')
    with open(os.path.join(md_question_dir, 'index.md'), 'w', encoding='utf-8') as question_f:
        question_f.write(f'''\
+++
type = "question"
title = "{question.title}"
description = \'''{q_description}\'''
date = "{time.strftime('%Y-%m-%dT%H:%M:%SZ', question.date)}"
lastmod = "{time.strftime('%Y-%m-%dT%H:%M:%SZ', question.lastmod)}"
weight = {question.number}
keywords = [ "{'", "'.join(q_keywords.split(','))}" ]
aliases = [ "/questions/{question.number}" ]
osqa_answers = {question.answers}
osqa_accepted = {('false', 'true')[question.accepted]}
+++

{cm_page}
''')


def main():
    top_dir = os.path.join(os.path.dirname(__file__), '..')

    parser = argparse.ArgumentParser(description='OSQA question and upfile import')
    parser.add_argument('--import-directory', default=os.path.join(top_dir, 'import'), help='Import directory')
    parser.add_argument('--markdown-directory', default=os.path.join(top_dir, 'site'), help='Exported Markdown (Hugo) content directory')
    parser.add_argument('--log-file', default=None, help='Log file')
    parser.add_argument('--parallel', type=int, default=4, help='Number of concurrent workers to use.')
    parser.add_argument('--start-question', type=int, default=1, help='First question to import')
    parser.add_argument('--stop-question', type=int, default=64400, help='Last question to import')
    args = parser.parse_args()

    args.import_directory = os.path.normpath(args.import_directory)
    osqa_questions_dir = os.path.join(args.import_directory, 'questions')
    # log_dir = os.path.join(top_dir, 'logs')
    args.markdown_directory = os.path.normpath(args.markdown_directory)
    hugo_content_directory = os.path.join(args.markdown_directory, 'content')
    hugo_questions_directory = os.path.join(hugo_content_directory, 'questions')
    try:
        # os.makedirs(osqa_questions_dir)
        # os.makedirs(osqa_upfiles_dir)
        # os.makedirs(log_dir)
        os.makedirs(hugo_questions_directory)
    except FileExistsError:
        pass

    # if not args.log_file:
    #     args.log_file = os.path.join(log_dir, 'osqa_import.log')
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s',
        handlers=[
            # logging.FileHandler(args.log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )

    logging.info(f'Starting with {args.start_question}')
    logging.info(f'Stopping after {args.stop_question}')

    questions = []
    for import_file in os.listdir(osqa_questions_dir):
        q = Question(import_file)
        if q.number >= args.start_question and q.number <= args.stop_question:
            questions.append(q)

    if args.parallel > 1:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.parallel) as executor:
            future_to_question = {}
            for question in questions:
                future_to_question.update({executor.submit(convert_question, question, osqa_questions_dir, hugo_questions_directory): question})
            for future in concurrent.futures.as_completed(future_to_question):
                question = future_to_question[future]
                future.result()
                # try:
                #     future.result()
                # except Exception as e:
                #     logging.critical(f'Question {question.number} generated exception {e}')
                #     raise
    else:
        for question in questions:
            convert_question(question, osqa_questions_dir, hugo_questions_directory)

    # questions.sort(key=lambda qnum: question.number, reverse=True)

#     with open(os.path.join(hugo_questions_directory, '_index.md'), 'w', encoding='utf-8') as index_f:
#         index_f.write(f'''\
# +++
# transparent = true
# redirect_to = ".."
# +++
# ''')

#     with open(os.path.join(hugo_content_directory, '_index.md'), 'w', encoding='utf-8') as index_f:
#         index_f.write(f'''\
# +++
# title = "Wireshark Q&amp;A"
# sort_by = "weight"
# pagingate_by = 5
# paginate_reversed = true
# +++
# ''')

#     with open(os.path.join(hugo_content_directory, 'index.md'), 'w', encoding='utf-8') as index_f:
#         index_f.write(f'''\
# +++
# template = "page-redirect.html"
# title = "Questions"
# [extra]
# redirect_to = ".."
# +++
# ''')
#         for q in questions[:30]:
#             a_status = ('unanswered', 'answered')[q.accepted]
#             datestamp = time.strftime('%Y-%m-%d %H:%M', q.time)
#             index_f.write(f'''\
# <div class="short-summary">
#     <div class="counts">
#         <div class="status {a_status}">
#             <div class="item-count">{q.answers}</div>
#             <div>answers</div>
#         </div>
#     </div>

#     <div class="question-summary-wrapper">
#         <h2><a href="/questions/{q.number}/{q.slug}">{q.title}</a></h2>

#         <div class="userinfo">
#             <span class="relativetime" title="{datestamp}">{datestamp}</span>
#         </div>
#     </div>

# </div>
# ''')

if __name__ == '__main__':
    main()
