import sqlite3
conn = sqlite3.connect("employee.db")
print("Connection Created Successfully!")

cursor = conn.cursor()
cursor.execute("create table if not exists employee(emp_id int,dept_id int,emp_name char(20),salary int)")

print("Table Created Successfully!")

conn.execute("insert into employee values (1,1,'Ankur',10000)")
conn.execute("insert into employee values (2,2,'Milan',10000)")
conn.execute("insert into employee values (3,3,'Pankaj',10000)")
conn.execute("insert into employee values (4,2,'Ruchika',10000)")
conn.execute("insert into employee values (5,1,'Rahul',10000)")
conn.execute("insert into employee values (6,5,'Nikhil',10000)")

conn.commit()
print("Records Inserted Successfully!")

conn.close()

