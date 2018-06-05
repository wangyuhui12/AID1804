
import pymysql

#　创建数据库连接对象
conn = pymysql.connect(host="localhost",user="root",
    password="tarena",database="db4",charset="utf8")

# 创建游标对象
cursor1 = conn.cursor()

try:
    # 利用execute方法执行sql命令
    sql_insert = "insert into sheng(s_name) values('台湾省');"
    cursor1.execute(sql_insert)

    # 删除数据
    sql_delete = "delete from sheng where id=2;"
    cursor1.execute(sql_delete)

    #　修改记录
    sql_update = "update sheng set s_name='修改' where id=1;"
    cursor1.execute(sql_update)
    print("ok")
    conn.commit()

except Exception as e:
    conn.rollback()
    print("出现错误，已回滚",e)

cursor1.close()
conn.close()
