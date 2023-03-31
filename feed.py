import sqlite3
import time
from datetime import datetime
from pprint import pprint

import feedparser
import requests
from bs4 import BeautifulSoup

import config


def get_feed(url):
    """
    returns feed entries \n
    url: url of the feed \n
    """
    feed = feedparser.parse(url)
    return feed['entries']


def get_new_entries(feed, source):
    """
    returns new entries not in the database \n
    feed: entries of the feed (from get_feed) \n
    source: source from the config file \n
    """
    new_entries = []
    con = sqlite3.connect(config.db)
    for entry in feed:
        cur = con.cursor()
        if not cur.execute(
                'SELECT 1 FROM entries WHERE url=? AND chat_id=? AND message_thread_id=? AND id=?;',
                (source['url'], source['chat_id'], source['message_thread_id'], entry['link'])
        ).fetchone():
            new_entries.append(entry)
        cur.close()
    con.close()
    return new_entries


def get_posted_entries(entries, source):
    """
    posts all entries and returns posted entries (uses post_entry) \n
    entries: entries of the feed (from get_new_entries) \n
    source: source from the config file \n
    """
    posted_entries = []
    for entry in entries:
        if post_entry(entry, source):
            posted_entries.append(entry)
    return posted_entries


def post_entry(entry, source):
    """
    posts an entry and returns if it was posted (called by get_posted_entries) \n
    entry: an entry from the feed \n
    source: source from the config file \n
    """
    title = ''
    try:
        title = '<b>' + strip_html(entry['title']) + '</b>\n'
    except:
        pass

    author = ''
    try:
        author = '<i>' + strip_html(entry['author']) + '</i>'
    except:
        pass

    media = ''
    if source['media']:
        try:
            media = '<a href="' + strip_html(entry['media_content'][0]['url']) + '">.</a>'
        except:
            pass
        try:
            media = '<a href="' + strip_html(entry['media_content'][0]['url']) + '">.</a>'
        except:
            pass

    link = ''
    try:
        link = '\n\n' + strip_html(entry['link'])
    except:
        pass

    text = title + author + media + link

    data = {
        'chat_id': source['chat_id'],
        'message_thread_id': source['message_thread_id'],
        'text': text,
        'parse_mode': 'HTML'
    }

    time.sleep(1)
    r = requests.post(source['api'], data=data)
    if not r.ok:
        print(text)
        print(r.text)
    return r.ok


def strip_html(text):
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text()


def feed_entries_insert(source, entries):
    """
    inserts entries into the database \n
    source: source from the config file \n
    entries: entries of the feed (from get_posted_entries) \n
    """
    values = []
    timestamp = datetime.now().timestamp()
    for entry in entries:
        values.append((source['url'], source['chat_id'], source['message_thread_id'], entry['link'], timestamp))
    con = sqlite3.connect(config.db)
    cur = con.cursor()
    cur.executemany(
        'INSERT OR IGNORE INTO entries (url, chat_id, message_thread_id, id, timestamp) VALUES (?, ?, ?, ?, ?);',
        values
    )
    cur.close()
    con.commit()
    con.close()


def test(i):
    x = config.sources[i]
    print('---- ')
    print('---- ' + x['url'])
    print('---- ')
    pprint(get_feed(x['url']))


if __name__ == "__main__":
    test(0)
