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


if __name__ == "__main__":
    main()
