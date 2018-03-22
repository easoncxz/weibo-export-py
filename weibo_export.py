
import datetime
import itertools
import json
import random
import threading
import time
import os

import requests
import click

def load_statuses(cookie, page=None):
    ''' Perform API request '''
    return requests.get(
            'https://m.weibo.cn/index/my',
            params={
                **{'format': 'cards'},
                **({} if page is None else {'page': page})},
            headers={'cookie': cookie })

def has_statuses(response):
    ''' Does the response contain any statuses? '''
    try:
        return json.loads(response.content)[0]['mod_type'] == 'mod/pagelist'
    except (KeyError, IndexError) as _:
        return False

def clean_status_response(raw_json):
    ''' Get rid of scruff in HTTP response '''
    return [c['mblog'] for c in raw_json[0]['card_group']]

def save_statuses(raw_json, page, directory):
    ''' Save the given response into a file on disk '''
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    filename = 'weibo-export-{}-page-{}.json'.format(date, page)
    print('Saving page {} to {}'.format(page, filename))
    if not os.path.isdir(directory):
        os.makedirs(directory)
    with open(os.path.join(directory, filename), 'w') as f:
        f.write(json.dumps(clean_status_response(raw_json)))

@click.command()
@click.argument('cookie')
@click.option(
        '--starting-page',
        '-s',
        default=1,
        help='which page to start from, e.g. 5 (default: 1)')
@click.option(
        '--directory',
        '-d',
        default='downloaded',
        help='directory to save downloaded JSON files (default: downloaded)',
        type=click.Path())
def run_download(cookie, starting_page, directory):
    ''' Download Weibo statuses

    COOKIE should be the HTTP header value sent in the request, in URL-encoded
    form (RFC 3986).  This means it would contain information for all cookie
    key-value pairs.  Copying from the Chrome dev console's `cookie` field
    would work.

    '''
    for page in itertools.count(starting_page):
        response = load_statuses(cookie, page=page)
        if has_statuses(response):
            save_statuses(json.loads(response.content), page, directory)
        else:
            print('Page {} is empty. The download is probably done.'.format(page))
            break

if __name__ == '__main__':
    run_download()
