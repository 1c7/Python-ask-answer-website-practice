#coding=utf-8

from flask import Flask, request, abort, redirect, url_for, render_template
from flaskext.mysql import MySQL
#import MySQLdb
import json
import bcrypt 
# 加密用的模块

app = Flask(__name__)



mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'tophot'
mysql.init_app(app)


# 基础
@app.route('/login')
def hello_world():
    return render_template('login.html')
    #Flask will look for templates in the templates folder.



@app.route('/handle_login', methods=['POST'])
def handle_login():
    
    # http://stackoverflow.com/questions/8552675/form-sending-error-flask
    if request.form.get('email', None) == None:
      return '用户名不能为空'
      
    if request.form.get('pwd', None) == None:
      return '密码不能为空'
    
    email = request.form['email']
    pwd = request.form['pwd']
    
    print(email)
    print(pwd)

    return 'xxxx'

#
# 注册
#

@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/handle_signup', methods=['POST'])
def handle_signup():
    
    # http://stackoverflow.com/questions/8552675/form-sending-error-flask
    if request.form.get('email', None) == None:
      return '用户名不能为空'
      
    if request.form.get('pwd', None) == None:
      return '密码不能为空'
      
    if request.form.get('confirm_pwd', None) == None:
      return '重输密码不能为空' 
         
    email = request.form['email']
    pwd = request.form['pwd']
    confirm_pwd = request.form['confirm_pwd']
    
    hashed = bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt())
    
    # 连接数据库
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
    
    print(email)
    print(pwd)
    print(hashed)
    return 'xxxx'


# 模板
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


# 文件上传
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
    


# Cookies
@app.route('/c')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.



# 重定向
@app.route('/r')
def r_index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
    
    
    







if __name__ == '__main__':
    #app.run()
    app.run(debug=True)
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
