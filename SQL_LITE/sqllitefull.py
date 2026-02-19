import sqlite3
# #connect() create or opens database
# connection=sqlite3.connect("school.db")
# print("Database connected")
# connection.close()

connection1=sqlite3.connect("school.db")
#cursor()-->run sql
cur=connection1.cursor()
cur.executescript("""Create Table prani( id INTEGER,name TEXT,marks INTEGER);
                    Insert into prani values (1,"amit",90),(2,"Gajanan",100);
                    Update prani set marks=80 where id=2;
                    Alter table prani add age INTEGER;
                    """)
print("Table created successfully")
cur.execute("SELECT * FROM prani")
for row in cur.fetchall():
      print(row)

connection1.commit()
connection1.close()

# connection1=sqlite3.connect("school.db")
# cur=connection1.cursor()
# cur.execute("""Insert into studentts values (1,"amit",90),(2,"Gajanan",100)""")
# print("values insserted ")
# connection1.commit()
# connection1.close()

# connection1=sqlite3.connect("school.db")
# cur=connection1.cursor()
# cur.execute("""select * from studentts""")

# for row in cur.fetchall():
#     print(row)
# connection1.commit()
# connection1.close()

            