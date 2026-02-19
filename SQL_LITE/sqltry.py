import sqlite3
# connection=sqlite3.connect("school.db")
# print("Database connected")
# connection.close()

# connection1=sqlite3.connect("school.db")
# #cursor()-->run sql
# cur=connection1.cursor()
# cur.execute("""Create Table employee( emp_id INTEGER,emp_name TEXT,salary INTEGER)""")
# print("Table created successfully")
# connection1.commit()
# connection1.close()

# connection1=sqlite3.connect("school.db")
# cur=connection1.cursor()
# cur.execute("""Insert into employee values (1,"amit",50000),(2,"Gajanan",10000)""")
# print("values insserted ")
# connection1.commit()
# connection1.close()

connection1=sqlite3.connect("school.db")
cur=connection1.cursor()
cur.execute("""select * from employee""")

for row in cur.fetchall():
    print(row)
connection1.commit()
connection1.close()
