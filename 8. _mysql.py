#encoding=utf-8 

import sys
import _mysql
# https://github.com/PyMySQL/mysqlclient-python/blob/master/doc/user_guide.rst
# 读读上面这个文档吧, 很有用




# 连接
db=_mysql.connect(host="localhost",user="root",
                  passwd="admin",db="tophot")
                
                
                
                
                
# 查询       
db.query("""SET NAMES utf8""")
db.query("""SELECT * FROM question""")

r=db.store_result()


'''
for x in r.fetch_row():
  print(x[1])
  print(x[2])
  # 直接输入就支持中文, tuple 输出就是乱码
  #print(x.encode('utf-8'))
  print( type(x) )
#print( r.fetch_row() )
'''


 
# import mysqlclient
# mysqlclient == MySQLdb
# but mysqlclient support Python3


   
# 写入  
'''  
sql = "insert into question(title,description) values('3213', '32131')"   
re = db.query(sql)
r = db.store_result()

aff_row = db.affected_rows()
#print (aff_row)

'''


# 写入 2
'''
x = '标题'
y = '内容'

sql222 = "insert into question(title,description) values('"+x+"', '"+y+"')"  
print(sql222)
re = db.query(sql222)
r = db.store_result()

aff_row = db.affected_rows()
print (aff_row)
'''

#更新  
'''
sql_update = "UPDATE question SET title='更新' where qid = 1"  
r_q = db.query(sql_update)
r_s = db.store_result()
aff_row = db.affected_rows()
print (r_q)
print (r_s)
print (aff_row)
'''
# sys.exit()

   
sql_DELETE = "DELETE FROM question where qid = 1"  
db.query(sql_DELETE) # 返回 None
r_s = db.store_result()  # 返回 None
aff_row = db.affected_rows() # 返回影响的行数

print (aff_row)

   






