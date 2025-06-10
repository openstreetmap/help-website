#!/usr/bin/env python3
#
# fetch-questions.py
# Import questions from an OSQA site.
# Copyright 2020 Gerald Combs <gerald@wireshark.org>
#
# SPDX-License-Identifier: MIT
#

import argparse
import concurrent.futures
import logging
import os
import os.path
import re
import sys
import time
import urllib.request, urllib.error, urllib.parse


osqa_ask_url = 'https://help.openstreetmap.org'
invalid_chars_re = re.compile('[^A-Za-z0-9-_=+,.%~]')
manual_fixes = {
#    63646: {'from': 'THIS-IS-PCAP-file.jpg]', 'to': 'THIS-IS-PCAP-file.jpg'},
}

def exit_err(message):
    logging.critical(message)
    sys.exit(1)

def open_url(url, encoding=None):
    '''Open a URL.
    Returns the tuple (body, response_url, status).
    '''
    req_headers = { 'User-Agent': 'OpenStreetMap import-from-osqa' }
    try:
        req = urllib.request.Request(url, headers=req_headers)
        response = urllib.request.urlopen(req)
        if encoding:
            body = response.read().decode(encoding, 'replace')
        else:
            body = response.read()
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return(None, url, 404)
        logging.critical('Error {} opening {}'.format(err.code, url))
        raise
    except Exception as err:
        logging.critical('Error opening {}: {}'.format(url, err))
        raise

    return (body, response.geturl(), response.getcode())


def fetch_question(question, questions_dir):
    max_retries = 3
    for attempt in range(1, max_retries + 1):
        question_url = f'{osqa_ask_url}/questions/{question}'
        try:
            (body, response_url, status) = open_url(question_url, encoding='UTF-8')
        except Exception as e:
            if attempt < max_retries:
                logging.warning(f'Error fetching question {question} (attempt {attempt}): {e}. Retrying...')
                time.sleep(2)
                continue
            else:
                logging.critical(f'Failed to fetch question {question} after {max_retries} attempts: {e}')
                return False

        if status == 200:
            q_filename = ''
            if response_url.startswith(question_url + '/'):
                q_filename = response_url[len(question_url)+1:]
            # if len(q_filename) < 1:
            #     exit_err(f"Invalid response URL for question {question}: {response_url}")
            q_filename = f'{question}.' + invalid_chars_re.sub('_', q_filename).lower() + '.html'
            q_filename = q_filename.replace('..', '.')
            if question in manual_fixes:
                replace = manual_fixes[question]
                body = body.replace(replace['from'], replace['to'])
                logging.info(f'Replaced {replace["from"]} with {replace["to"]} in question {question}')
            with open(os.path.join(questions_dir, q_filename), 'w') as html_f:
                html_f.write(body)
            logging.info(f'Fetched {question} as {q_filename}, {len(body)} bytes.')
            return True
        elif status == 404:
            logging.info(f'Question {question} returned 404.')
            return False
        else:
            if attempt < max_retries:
                logging.warning(f'Question {question_url} returned {status} (attempt {attempt}). Retrying...')
                time.sleep(2)
                continue
            else:
                logging.critical(f'Question {question_url} returned {status} after {max_retries} attempts.')
                return False

def main():
    # exit_err('This script is no longer relevant.')

    top_dir = os.path.join(os.path.dirname(__file__), '..')

    parser = argparse.ArgumentParser(description='OSQA question import')
    parser.add_argument('--import-directory', default=os.path.join(top_dir, 'import'), help='Import directory')
    parser.add_argument('--log-file', default=None, help='Log file')
    parser.add_argument('--parallel', type=int, default=4, help='Number of concurrent workers to use.')
    parser.add_argument('--start-question', type=int, default=1, help='First question to import')
    parser.add_argument('--stop-question', type=int, default=64400, help='Last question to import')
    args = parser.parse_args()

    args.import_directory = os.path.normpath(args.import_directory)
    osqa_questions_dir = os.path.join(args.import_directory, 'questions')
    log_dir = os.path.join(top_dir, 'logs')
    try:
        os.makedirs(osqa_questions_dir)
        os.makedirs(log_dir)
    except FileExistsError:
        pass

    if not args.log_file:
        args.log_file = os.path.join(log_dir, 'osqa_question_import.log')
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s',
        handlers=[
            logging.FileHandler(args.log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )

    logging.info(f'Starting with {args.start_question}')
    logging.info(f'Stopping after {args.stop_question}')

    fetched = 0
    total = len(range(args.start_question, args.stop_question+1))
    if args.parallel > 1:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.parallel) as executor:
            future_to_question = {}
            for question in range(args.start_question, args.stop_question+1):
                future_to_question.update({executor.submit(fetch_question, question, osqa_questions_dir): question})
            for future in concurrent.futures.as_completed(future_to_question):
                question = future_to_question[future]
                try:
                    if future.result():
                        fetched += 1
                except Exception as e:
                    print(f'Question {question} generated exception {e}')
                    raise
    else:
        for question in range(args.start_question, args.stop_question+1):
            if fetch_question(question, osqa_questions_dir):
                fetched += 1

    logging.info(f'Fetched {fetched} questions out of {total} total')

if __name__ == '__main__':
    main()
