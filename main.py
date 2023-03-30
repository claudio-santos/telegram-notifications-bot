import time

import config
import feed


def main():
    for x in config.sources:
        entries = feed.get_feed(x['url'])
        new_entries = feed.get_new_entries(entries, x)
        posted_entries = feed.get_posted_entries(new_entries, x)
        feed.feed_entries_insert(x, posted_entries)
        print(x['url'])
        time.sleep(1)


def test_post_entry():
    source = {
        'url': 'url',
        'api': config.test_api,
        'chat_id': config.test_chat_id,
        'message_thread_id': config.test_message_thread_id,
        'media': False
    }
    entry = {
        'title': 'title',
        'author': 'author',
        'link': 'link'
    }
    feed.post_entry(entry, source)


if __name__ == "__main__":
    main()
    # test_post_entry()
