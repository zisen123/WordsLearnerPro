#!/usr/bin/env python3
# -*-encoding:utf-8-*-

import csv
import sqlite3 as sqlite
import time

localday = time.time() // 86400
new_file=input("请输入你需要背诵的单词表，例如'mywords.csv'\n")
csvFile = open(new_file, "r", encoding="utf-8-sig")

dict_reader = csv.DictReader(csvFile)
# for row in dict_reader:
#     print(row)

con = sqlite.connect("WordsList.db")

with con:

    cur = con.cursor()
    for row in dict_reader:
        cur.execute(
            "INSERT INTO words VALUES (?,?,?,?,?,?,?)",
            [row["单词"], row["词性"], row["English"], row["释义"], row["备注"], 0, localday],
        )