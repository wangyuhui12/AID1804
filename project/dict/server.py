#!/usr/bin/env python3
#coding=utf-8 

'''
name:Levi
MODULES:　python3.5  mysql  pymysql
This is a dict project for AID 
'''

from socket import *
import os 
import signal 
import time 
import sys
import pymysql 

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)
DICT_TEXT = "./dict.txt"  #文本路径

#主控制流程
def main():
    #数据库链接
    db = pymysql.connect('localhost','root','123456','dict')

    #创建tcp套接字
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    #忽略子进程退出
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    while True:
        try:
            c,addr = s.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            sys.exit("服务器退出")      
        except Exception:
            continue 

        #创建子进程
        pid = os.fork()

        if pid == 0:
            s.close()
            do_child(c,db)
        else:
            c.close()
            continue  

def do_child(c,db):
    #循环接收客户请求
    while True:
        data = c.recv(128).decode()
        print("Request:",data)

        if data[0] == 'R':
            do_register(c,db,data)
        elif data[0] == 'L':
            name = do_login(c,db,data)
        elif data[0] == 'E':
            c.close()
            sys.exit(0)
        elif data[0] == 'Q':
            do_query(c,db,name,data)
        elif data[0] == 'H':
            do_history(c,db,name)


def do_register(c,db,data):
    print(">>>>>执行注册操作<<<<<")
    l = data.split(' ')
    name = l[1]
    passwd = l[2]

    cursor = db.cursor()

    #判断是否name是否存在
    sql = "select name from user where name='%s'"%name
    cursor.execute(sql)
    r = cursor.fetchone()

    if r != None:
        c.send(b"EXISTS")
        return 

    #插入到数据库
    sql = "insert into user (name,passwd) values ('%s','%s')"%(name,passwd)
    try:
        cursor.execute(sql)
        db.commit()
        c.send(b'OK')
    except:
        c.send(b"FALL")
        db.rollback()
        return 
    else:
        print("注册成功")

def do_login(c,db,data):
    print("登录操作")
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()

    sql = "select * from user where name='%s' and passwd='%s'"%(name,passwd)
    cursor.execute(sql)
    r = cursor.fetchone()
    if r == None:
        c.send(b"FALL")
    else:
        c.send(b'OK')
        return name 


def do_query(c,db,name,data):
    print("查询操作")
    word = data.split(' ')[1]
    cursor = db.cursor()

    def insert_history():
        tm = time.ctime()
        sql = "insert into hist (name,word,time) \
        values ('%s','%s','%s')"%(name,word,tm)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            return

    #使用数据库查询
    sql = "select * from words where word='%s'"%word
    try:
        cursor.execute(sql)
        r = cursor.fetchone()
    except:
        pass 

    if not r:
        c.send(b'FALL')
    else:
        c.send(b'OK')
        time.sleep(0.1)
        msg = "{} 　:　 {}".format(r[1],r[2])
        c.send(msg.encode())
        insert_history()

    #　使用文件查询
    # try:
    #     f = open(DICT_TEXT)
    # except:
    #     print("打开文件失败")
    #     c.send(b'FALL')
    #     return 

    # for line in f:
    #     w =  line.split(' ')[0]
    #     if w > word:
    #         c.send(b'FALL')
    #         break
    #     if w == word:
    #         c.send(b'OK')
    #         time.sleep(0.1)
    #         c.send(line.encode())
    #         #调用内部函数完成插入历史记录
    #         insert_history()
    #         break
    # f.close()

def do_history(c,db,name):
    print("历史记录")
    cursor = db.cursor()
    sql = "select * from hist where name='%s'"%name
    try:
        cursor.execute(sql)
        r = cursor.fetchall()
    except:
        pass 

    if not r:
        c.send(b'FALL')
    else:
        c.send(b'OK')
        time.sleep(0.1)
        for i in r:
            msg = "{} {} {}\n".format(i[1],i[2],i[3])
            c.send(msg.encode())
        time.sleep(0.1)
        c.send(b'##')

if __name__ == "__main__":
    main()


