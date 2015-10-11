#coding=utf-8
from flask import Flask
app = Flask(__name__)
from flask import request
from flask import abort, redirect, url_for
import MySQLdb
import json

# 连接数据库的之后 print() 中文是乱码
# 输出到网页也是乱码, 看看怎么回事


# 基础
@app.route('/')
def hello_world():
    try:
        conn=MySQLdb.connect(host='localhost',user='root',passwd='admin',db='tophot',port=3306)
        cur=conn.cursor()
        x = cur.execute('select title, description from question')
        result = cur.fetchone()
        print(result)
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    
    a = json.dumps(result)
    return a
    #return result + 'Hello World!'





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
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
