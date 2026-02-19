#First install psycopg2 using cmd:pip install psycopg2-binary
import psycopg2
conn=psycopg2.connect(
    host="localhost",
    database="psq1",
    user="postgres",
    password="1234"
)

print("Connected successfully")

cur=conn.cursor()
#
# cur.execute("""CREATE TABLE employee(id int,name varchar(50),salary int)""")
cur.execute("""INSERT INTO employee VALUES(1,'RAHUL',50000)""")
conn.commit()
cur.execute("""select * from employee""")
rows=cur.fetchall()
for i in rows:
    print(i)
conn.close() 



