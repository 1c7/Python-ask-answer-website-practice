#coding=utf-8
# run on python2.7

import sys  
print( sys.getdefaultencoding() )


a = "老王"
print(a)

'''
a_gb2312 = a.encode('gb2312') #以gb2312编码对unicode对像进行编码
print(a_gb2312)
'''



a_utf8 = a.encode('utf-8')#如果以utf-8的编码对str进行解码得到的结果，将无法还原原来的unicode类型

print(a_utf8)

























