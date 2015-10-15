#coding=utf-8
import MySQLdb

'''

http://www.cnblogs.com/rollenholt/archive/2012/05/29/2524327.html
http://mysql-python.sourceforge.net/MySQLdb.html
http://mysql-python.sourceforge.net/MySQLdb-1.2.2/public/MySQLdb-module.html


The DB API specification PEP-249 should be your primary guide for using this module. Only deviations from the spec and other database-dependent things will be documented here.
https://www.python.org/dev/peps/pep-0249/#cursor-methods

'''




db = MySQLdb.connect(host='localhost',user='root',passwd='admin',db='tophot',port=3306) #don't use charset here

# setup a cursor object using cursor() method
cursor = db.cursor()

cursor.execute("SET NAMES utf8mb4;") #or utf8 or any other charset you want to handle

cursor.execute("SET CHARACTER SET utf8mb4;") #same as above

cursor.execute("SET character_set_connection=utf8mb4;") #same as above








a = cursor.execute("SELECT * FROM question") # 返回记录条数
print (a)
print (cursor.fetchone())

for x in cursor.fetchall():
  print (x)






