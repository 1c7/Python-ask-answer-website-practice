#coding=utf-8
#https://github.com/PyMySQL/PyMySQL



import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             db='tophot',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:

    with connection.cursor() as cursor:
        sql = "SELECT * FROM question"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
        
finally:
    connection.close()





