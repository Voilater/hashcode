#! /usr/bin/env python3


from hashlib import * 
import sys 


hashvalue = sys.argv[1]

print(''' 

 |   |            |                    |      
 |   |  _` |  __| __ \   __|  _ \   _` |  _ \ 
 ___ | (   |\__ \ | | | (    (   | (   |  __/ 
_|  _|\__,_|____/_| |_|\___|\___/ \__,_|\___| 

                                       made by @voilater
    ''')

for passwd in open('/home/zeus/SecLists-master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt', 'r').readlines():
    if hashvalue == md5(passwd.strip().encode('utf-8')).hexdigest(): 
        print(passwd)
        break
    elif hashvalue == sha1(passwd.strip().encode('utf-8')).hexdigest():
        print(passwd)
        break
    elif hashvalue == sha224(passwd.strip().encode('utf-8')).hexdigest():
        print(passwd)
        break
    elif hashvalue == sha256(passwd.strip().encode('utf-8')).hexdigest():
        print(passwd)
        break
    elif hashvalue == sha512(passwd.strip().encode('utf-8')).hexdigest():
        print(passwd)
        break
    elif hashvalue == sha384(passwd.strip().encode('utf-8')).hexdigest():
        print(passwd)
        break 

else:
    print("not found")
