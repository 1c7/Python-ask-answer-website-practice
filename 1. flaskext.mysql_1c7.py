''''
Flask-MySQL
https://flask-mysql.readthedocs.org/en/latest/  
http://codehandbook.org/python-web-application-development-using-flask-and-mysql/  


'''

from flask import Flask
from flaskext.mysql import MySQL
 
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'tophot'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
 
@app.route("/")
def hello():
    conn = mysql.connect()
    cursor = conn.cursor()
    return "Welcome to Python Flask App!"
    
    
    
 
if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    
    
    
