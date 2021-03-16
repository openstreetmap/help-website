#!usr/bin/env python3
#
# fetch-upfiles.py
# Import uploads from an OSQA site based on imported questions.
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


osqa_ask_url = 'https://osqa-ask.wireshark.org'
invalid_chars_re = re.compile('[^A-Za-z0-9-_=+,.%~]')


def exit_err(message):
    logging.critical(message)
    sys.exit(1)

def open_url(url, encoding=None):
    '''Open a URL.
    Returns the tuple (body, status).
    '''
    req_headers = { 'User-Agent': 'Wireshark import-from-osqa' }
    body = ''
    try:
        req = urllib.request.Request(url, headers=req_headers)
        response = urllib.request.urlopen(req)
        if encoding:
            body = response.read().decode(encoding, 'replace')
        else:
            body = response.read()
        return (body, response.getcode())
    except urllib.error.HTTPError as err:
        logging.critical('Error {} opening {}'.format(err.code, url))
        return (None, err.code)
    except Exception as err:
        exit_err('Error opening {}: {}'.format(url, err))
        return (None, 0)


def fetch_upfile(upfile_name, upfiles_dir):
    (uf_body, status) = open_url(f'{osqa_ask_url}/upfiles/{urllib.parse.quote(upfile_name)}')

    if not uf_body or status != 200:
        logging.critical(f'Failed to fetch {upfile_name}: {status}')
        return

    with open(os.path.join(upfiles_dir, upfile_name), 'wb') as upfile_f:
        upfile_f.write(uf_body)
    logging.info(f'Fetched upfile {upfile_name}, {len(uf_body)} bytes.')


def find_upfiles(question_file):
    upfiles = set()
    with open(question_file, mode='r', encoding='utf-8') as q_f:
        body = q_f.read()
        upfiles |= set(re.findall(f'"[^< ]+/upfiles/([^"/<]+)"', body))

    return upfiles


def main():
    top_dir = os.path.join(os.path.dirname(__file__), '..')

    parser = argparse.ArgumentParser(description='OSQA upfile import')
    parser.add_argument('--import-directory', default=os.path.join(top_dir, 'import'), help='Import directory')
    parser.add_argument('--log-file', default=None, help='Log file')
    parser.add_argument('--parallel', type=int, default=4, help='Number of concurrent workers to use.')
    args = parser.parse_args()

    args.import_directory = os.path.normpath(args.import_directory)
    osqa_questions_dir = os.path.join(args.import_directory, 'questions')
    osqa_upfiles_dir = os.path.join(args.import_directory, 'upfiles')
    log_dir = os.path.join(top_dir, 'logs')
    try:
        os.makedirs(osqa_upfiles_dir)
        os.makedirs(log_dir)
    except FileExistsError:
        pass

    if not args.log_file:
        args.log_file = os.path.join(log_dir, 'osqa_upfile_import.log')
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s',
        handlers=[
            logging.FileHandler(args.log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )

    logging.info(f'Finding upfile links in {osqa_questions_dir}')

    upfiles = set()

    question_files = os.listdir(osqa_questions_dir)
    for question_file in question_files:
        question = question_file.split('.')[0]
        upfiles |= find_upfiles(os.path.join(osqa_questions_dir, question_file))

    logging.info(f'Found {len(upfiles)} upfiles in {len(question_files)} questions')

    if args.parallel > 1:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.parallel) as executor:
            future_to_upfile = {}
            for upfile in upfiles:
                future_to_upfile.update({executor.submit(fetch_upfile, upfile, osqa_upfiles_dir): upfile})
            for future in concurrent.futures.as_completed(future_to_upfile):
                upfile = future_to_upfile[future]
                future.result()
                # try:
                #     future.result()
                # except Exception as e:
                #     logging.critical(f'Upfile {upfile} generated exception {e}')
                #     raise
    else:
        for upfile in upfiles:
            upfiles |= fetch_upfile(upfile, osqa_upfiles_dir)

    logging.info(f'Fetched {len(upfiles)} upfiles')


if __name__ == '__main__':
    main()
