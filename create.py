import sqlite3

import config

drop_entries = 'DROP TABLE IF EXISTS "entries";'

create_entries = 'CREATE TABLE "entries" (' \
                 '"url" TEXT,' \
                 '"chat_id" TEXT,' \
                 '"message_thread_id" TEXT,' \
                 '"id" TEXT,' \
                 '"timestamp" TIMESTAMP,' \
                 'PRIMARY KEY("url","chat_id","message_thread_id","id")' \
                 ');'


def create():
    """drops and creates the table from the database"""
    con = sqlite3.connect(config.db)
    cur = con.cursor()
    cur.execute(drop_entries)
    cur.execute(create_entries)
    cur.close()
    con.close()
    print(create_entries)


if __name__ == "__main__":
    create()
