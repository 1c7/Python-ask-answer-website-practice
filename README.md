### 这里放的代码是啥?  
是我用各个 Web 框架去问答网站的代码  
(肯定不会写一个完整能用的, 费时间且没必要, 大概写写而已, 主要是了解框架整个文件夹结构, 怎么操作 cookie session, 怎么连数据库, 操作模板, 实现个登陆系统(注册页面+登陆页面) 等等这类事情摸清楚就差不多了)  


<br/>
### 我写这些目的: 试用并了解各个 Web 框架
通过看网上文章 + 各个都尝试下, 写点小东西.   
然后对各个框架之间的差异, 优势劣势, 是重型还是轻巧有个更深的概念.  
没了, 就这目的  


<br/>
#### 当前状态: 未完成, 还没有结论



<br/>
### Python 框架列表
Django  
bottle  
Flask  
Tornado  
Pyrmaid  
web.py  


<br/>
##### 目录说明  
根目录下的 python 文件主要是各种测试用的短小代码  

文件夹和文件的序号啥意思?  

  没啥特别含义, 就是看起来有顺序一点  
  因为我看别人的代码的时候总是觉得不知道从哪里看起, 有种奇怪的蛋疼感  
  而且标了序号之后再命令行里面补全也挺方便的, 所以就加了数字序号上去  


<br/>
#### 社区  
http://www.pycon.org/  

http://wiki.woodpecker.org.cn/moin/%E9%A6%96%E9%A1%B5  

http://v2ex.com/go/python  

http://weekly.pychina.org/  

https://python-china.org/  

https://groups.google.com/forum/#!forum/python-cn  



<br/>
#### 学习  
怎么用最短时间高效而踏实地学习 Python？  
http://www.zhihu.com/question/28530832  


如何面试Python后端工程师？  
http://www.zhihu.com/question/33398583  



Python 有哪些好的学习资料或者博客？  
http://www.zhihu.com/question/34907211  


在大型项目上，Python 是个烂语言吗？  
http://www.zhihu.com/question/21017354  


<br/>
### 部署
http://docs.jinkan.org/docs/flask/deploying/index.html  


<br/>
### Python & MySQL
MySQLdb 模块
要先自己安装, 默认是不带的  
下载地址是 http://sourceforge.net/projects/mysql-python/  
对, 没错, 这个模块没有官网...
然后 这个 sourceforge 这边下面的描述里, 可以看到 github 地址
https://github.com/farcepest/MySQLdb1  




相关教程:
http://www.tutorialspoint.com/python/python_database_access.htm
http://zetcode.com/db/mysqlpython/



<br/>
### Virtualenv



<br/>
### 其他资料
How to install Python MySQLdb module using pip?  
http://stackoverflow.com/questions/25865270/how-to-install-python-mysqldb-module-using-pip  

How do I connect to a MySQL Database in Python?
http://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python

__(on my reading list)Django vs Flask vs Pyramid: Choosing a Python Web Framework__
https://www.airpair.com/python/posts/django-flask-pyramid


浅谈Python web框架 -- 2011年  
http://feilong.me/2011/01/talk-about-python-web-framework  


<br/>
### 对比


#### Flask
```Python

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

```

#### Tornado
```

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    port = 8888
    print("Listening at localhost:"+ str(port))
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
    
```


#### Web.py
```
import web
        
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:        
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()

```

<br />
### Web Framework 列表

https://wiki.python.org/moin/WebFrameworks


Falcon  
http://falconframework.org/  


cherrypy﻿ http://cherrypy.org/  






















