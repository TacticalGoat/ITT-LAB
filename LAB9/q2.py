import sqlite3

conn = sqlite3.connect('test.db')

name = None
while name is None:
	name = str(raw_input())
	if name == '' or name is None:
		print 'name required'
		name = None

roll = None
while roll is None:
	roll = int(raw_input())
	if name is None:
		print 'roll number required'

age = None
while age is None:
	age = int(raw_input())
	if age is None:
		print 'Age is required'

class_ = None
while class_ is None:
	class_ = int(raw_input())
	if class_ is None:
		print 'Class is required'

x = [(roll,name,class_,age)]

conn.executemany("INSERT INTO STUDENT(ID,NAME,CLASS,AGE) VALUES(?,?,?,?);",x)
print "Success"
conn.commit()

