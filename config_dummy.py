db = 'database.db'

sources = [
    {  # 0
        'url': '<RSS_FEED_URL_1>',
        'api': 'https://api.telegram.org/bot<BOT_TOKEN>/sendMessage',
        'chat_id': '<GROUP_CHAT_ID>',
        'message_thread_id': '<TOPIC_MESSAGE_ID>',
        'media': False
    },
    {  # 1
        'url': '<RSS_FEED_URL_2>',
        'api': 'https://api.telegram.org/bot<BOT_TOKEN>/sendMessage',
        'chat_id': '<GROUP_CHAT_ID>',
        'message_thread_id': '<TOPIC_MESSAGE_ID>',
        'media': True
    }
]

test_api = 'https://api.telegram.org/bot<BOT_TOKEN>/sendMessage'
test_chat_id = '<TEST_GROUP_CHAT_ID>'
test_message_thread_id = '<TEST_TOPIC_MESSAGE_ID>'


def test():
    for x in sources:
        print(x['url'])


if __name__ == "__main__":
    test()
