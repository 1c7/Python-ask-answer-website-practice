#coding=utf-8
''''
Flask-MySQL
https://flask-mysql.readthedocs.org/en/latest/  
http://codehandbook.org/python-web-application-development-using-flask-and-mysql/  
'''


from flask import Flask
from flaskext.mysql import MySQL
 
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'tophot'

mysql.init_app(app)
 
@app.route("/")
def hello():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SET NAMES utf8mb4;") #or utf8 or any other charset you want to handle

    cursor.execute("SET CHARACTER SET utf8mb4;") #same as above

    cursor.execute("SET character_set_connection=utf8mb4;") #same as above
    a = cursor.execute("SELECT * FROM question") # 返回记录条数
    print (a)
    print (cursor.fetchone())

    for x in cursor.fetchall():
      print (x)

    return "Welcome to Python Flask App!"
    
    
    
 
if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    
    
    
