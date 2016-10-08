import sqlite3

def swap(A,i,j):
	temp = A[i]
	A[i] = A[j]
	A[j] = temp


def selection_sort(A):
	for i in range(len(A)):
		least = i
	for k in range(i+1,len(A)):
		if A[k][0] < A[least][0]: #selects id from tuple
			least = k

	swap(A,least,i)





conn = sqlite3.connect('test.db')
# print "DB CONN SUCCESS"
# conn.execute('CREATE TABLE STUDENT(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,CLASS INT NOT NULL,AGE INT NOT NULL);')
# print 'table created successfully'
# conn.execute("INSERT INTO STUDENT(ID,NAME,CLASS,AGE) VALUES(1,'SANTHOSH',3,'10');")
# conn.execute("INSERT INTO STUDENT(ID,NAME,CLASS,AGE) VALUES(2,'SANTHOSH2',3,'10');")
# conn.execute("INSERT INTO STUDENT(ID,NAME,CLASS,AGE) VALUES(3,'SANTHOSH3',4,'10');")
# conn.execute("INSERT INTO STUDENT(ID,NAME,CLASS,AGE) VALUES(4,'SANTHOSH5',3,'10');")
# conn.commit()

# print "DB CONN SUCCESS"
c = conn.cursor()
lst = c.execute('SELECT id,name,class,age FROM STUDENT').fetchall()
print lst
for i in range(len(lst)):
	print str(lst[i][0]) + str(lst[i][1])
selection_sort(lst)
for i in range(len(lst)):
	print str(lst[i][0]) + str(lst[i][1])
conn.close()