#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3 as sqlite
import time

localday = time.time() // 86400
con = sqlite.connect("WordsList.db")


def date_caculator(x):
    if x == 1:
        return 0
    elif x == 2:
        return 1
    elif x == 3:
        return 2
    elif x == 4:
        return 5
    elif x == 5:
        return 11
    elif x == 6:
        return 25
    elif x == 7:
        return 56
    elif x == 8:
        return 126
    elif x == 9:
        return 284
    elif x == 10:
        return 639
    else:
        return 0

# print(date_caculator(10))
with con:

    # con.row_factory = sqlite.Row

    cur = con.cursor()
    # cur.execute("SELECT * FROM words WHERE date = ?", (localday,))
    # cur.execute("SELECT * FROM words")
    rows = cur.fetchall()

    # cur.execute("UPDATE words SET level = 1 WHERE word = 'protocole'")
    # for row in rows:
    #     print(
    #         f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]}"
    #     )

    for row in rows:
        print(f"{row[0]}")
        input("请回车查看单词释义")

        print(f"{row[1]} {row[2]} {row[3]} {row[4]} ")
        is_know = input("记忆正确输入y，记忆错误输入n\n")
        if is_know == "y":
            cur.execute(
                "UPDATE words SET level = ?, date = ? WHERE word = ?",
                (row[5] + 1, row[6] + date_caculator(int(row[5] + 1)), row[0]),
            )
        elif is_know == "n":
            cur.execute("UPDATE words SET level = 0 WHERE word = ?", (row[0],))
        else:
            print("input invalid!")
            break

    # for row in rows:
    #     print(row[0], row[5],row[6])
    #     cur.execute("UPDATE words SET level = ? WHERE word = ?",(row[5]+1, row[0]))