#coding=utf-8


'''

http://www.cnblogs.com/rollenholt/archive/2012/05/29/2524327.html
http://mysql-python.sourceforge.net/MySQLdb.html

http://mysql-python.sourceforge.net/MySQLdb-1.2.2/public/MySQLdb-module.html



'''


import MySQLdb

try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='admin',db='tophot',port=3306)
    cur=conn.cursor()
    x = cur.execute('select * from question')
    result = cur.fetchone()
    print(result)
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])









