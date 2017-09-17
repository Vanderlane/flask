#homework probeersel


conn = sqlite3.connect("new.db")

cursor=conn.cursor()

cursor.execute("""create table inventory (naam, leeftijd,groep)""")

conn.commit()

conn.close()