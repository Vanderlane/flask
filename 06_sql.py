#homework probeersel

import sqlite3
import random

with sqlite3.connect("new.db") as connection:
	cursor=connection.cursor()
	
	cursor.execute("drop table if exists numbers")
	cursor.execute("create table numbers(num int)")
	
	for i in range(100):
		cursor.execute("insert into numbers VALUES(?)",(random.randint(0,100),))


connection.close()