#!/usr/bin/env python3
# -*-encoding:utf-8-*-

import sqlite3 as sqlite

def create_table_now():
    con = sqlite.connect("WordsList.db")

    with con:

        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS words")
        cur.execute(
            '''CREATE TABLE words
            (word TEXT, 
            nature TEXT, 
            anglais TEXT, 
            chinois TEXT, 
            note TEXT, 
            level INT, 
            date INT)'''
        )
    