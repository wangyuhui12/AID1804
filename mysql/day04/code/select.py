

import pymysql

conn = pymysql.connect(host="localhost", user="root",
    password="tarena",database='db4',charset="utf8")

cursor1 = conn.cursor()

try:
    sql_select = 'select * from sheng;'

    cursor1.execute(sql_select)
    print(cursor1.fetchone())
    print("*********************************")
    #print(cursor1.fetchmany(3))
    data2 = cursor1.fetchmany(3)
    for i in data2:
        print(i)
    print("-----------------------------------")
    data3 = cursor1.fetchall()
    for i in data3:
        print(i)
    # print(cursor1.fetchall())
    print("finish")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("出现错误，已回滚",e)

cursor1.close()
conn.close()