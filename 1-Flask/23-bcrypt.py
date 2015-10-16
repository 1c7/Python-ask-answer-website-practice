#coding=utf-8
import bcrypt 
# 加密用的模块
# https://github.com/pyca/bcrypt/

password = "super secret password"
print(password)


# Hash a password for the first time, with a randomly-generated salt
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)


# Check that a unhashed password matches one that has previously been
#   hashed
if bcrypt.hashpw(password, hashed) == hashed:
    print("It Matches!")
else:
    print("It Does not Match :(")
    
    
a = bcrypt.hashpw(password, hashed)
print (a)








































