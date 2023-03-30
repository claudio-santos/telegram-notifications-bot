import config
import create
import feed


def reset():
    """resets the database and inserts all feed entries"""
    create.create()
    for x in config.sources:
        entries = feed.get_feed(x['url'])
        feed.feed_entries_insert(x, entries)
        print(x['url'])


if __name__ == "__main__":
    reset()
