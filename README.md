# telegram-notifications-bot

#### Python script to get entries from rss feeds. Checks if there are new entries and post them in a group.

### How to use:
1. Change `config_dummy.py` to `config.py` and configure the bot settings to get notifications.
2. Run `reset.py` to create and fill the database. Running `main.py` **will only send new entries** to the bot.
   * _(optional)_ Run `create.py` to create the database. Running `main.py` **will send all entries** to the bot.
3. Run `main.py` periodically to fetch new entries and receive notifications.
   * _(example)_ Run in Linux using cron:
     * Run: `crontab -e`
     * New line: `0 * * * * cd /path/to/ && /usr/bin/python3 /path/to/main.py`

* Test notifications with the functions in `test.py`.