import config
import feed


def test_post_entry():
    source = {
        'url': 'url',
        'api': config.test_api,
        'chat_id': config.test_chat_id,
        'message_thread_id': config.test_message_thread_id,
        'media': True
    }
    entry = {
        'title': 'Gastronomia de Portugal',
        'author': 'Wikipédia',
        'media_content': [
            {'url': 'https://upload.wikimedia.org/wikipedia/commons/2/2b/MargaretCafe_PasteisDeNata.JPG'}
        ],
        'link': 'https://pt.wikipedia.org/wiki/Gastronomia_de_Portugal'
    }
    feed.post_entry(entry, source)


def test_source(i):
    source = config.sources[i]
    entries = feed.get_feed(source['url'])
    entry = entries[0]
    print(source)
    feed.post_entry(entry, source)


if __name__ == "__main__":
    # test_post_entry()
    test_source(4)
