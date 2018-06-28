#!/usr/bin/env python3 
#coding=utf-8 

from socket import *
import sys 
import traceback
import getpass

#主控制流程函数
def main():
    if len(sys.argv) < 3:
        print('argv is error')
        return 
    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket()
    try:
        s.connect((host,port))
    except Exception:
        traceback.print_exc()
        return 

    while True:
        print('''
            =============Welcome============
            -- 1.注册　　2.登录　　 3.退出--
            ================================
            ''')
        try:
            cmd = int(input("请输入选项>>"))
        except Exception:
            print("命令错误！！")
            continue

        if cmd not in [1,2,3]:
            print("没有该选项！！")
            continue
        elif cmd == 1:
            if do_register(s) == 0:
                print("注册成功！可以登录")
            else:
                print("注册失败！")
        elif cmd == 2:
            if do_login(s) == 0:
                print("登录成功！！")
                login(s)
            else:
                print("登录失败！！")
        elif cmd == 3:
            s.send(b'E')
            sys.exit("谢谢使用")

def do_register(s):
    while True:
        name = input("User:")
        passwd = getpass.getpass()
        passwd1 = getpass.getpass('Confirm:')

        if (' ' in name) or (' ' in passwd):
            print("用户名或密码不能有空格")
            continue 
        if passwd != passwd1:
            print("两次密码不一致")
            continue 

        #将注册信息发送给服务器
        msg = 'R {} {}'.format(name,passwd)
        s.send(msg.encode())

        data = s.recv(128).decode()

        if data == 'OK':
            return 0
        elif data == 'EXISTS':
            print("用户名已存在")
            return 1
        else:
            return 1


def do_login(s):
    name = input("User:")
    passwd = getpass.getpass()
    msg = "L {} {}".format(name,passwd)
    s.send(msg.encode())

    data = s.recv(128).decode()
    if data == 'OK':
        return 0
    else: 
        print("用户名或密码不正确")
        return 1 

#登录后进入二级界面
def login(s):
    while True:
        print('''
            ============查询界面=============
            --1.查词　 2.历史记录　 3.退出--
            ================================
            ''')
        try:
            cmd = int(input("请输入选项>>"))
        except Exception:
            print("命令错误！！")
            continue

        if cmd not in [1,2,3]:
            print("没有该选项！！")
            continue
        elif cmd == 1:
            do_query(s)
        elif cmd == 2:
            do_history(s)
        elif cmd == 3:
            return
def do_query(s):
    while True:
        word = input('单词:')
        #退出查词
        if word == '##':
            break
        msg = 'Q {}'.format(word)
        s.send(msg.encode())
        data = s.recv(128).decode()
        if data == 'OK':
            data = s.recv(2048).decode()
            print(data)
        else:
            print("没有找到该单词")


def do_history(s):
    s.send(b'H')
    data = s.recv(123).decode()
    if data == 'OK':
        while True:
            data = s.recv(1024).decode()
            if data == '##':
                break
            print(data)
    else:
        print("没有历史记录")


if __name__ == "__main__":
    main()
