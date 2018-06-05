
from mysqlpython import mysqlpython

sqlh = mysqlpython("localhost",3306,"db4","root","tarena")

sql_update = "update sheng set id=150 where id=5;"
sqlh.command(sql_update)

