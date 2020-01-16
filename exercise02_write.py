import pymysql

# 连接数据库
db=pymysql.connect(host="localhost",
                   port=3306,
                   user="root",
                   password="123456",
                   database="stu",
                   charset="utf8")

#生成游标对象（操作数据库，执行sql语句，获取结果）
cur=db.cursor()
# 执行各种sql操作

sql = "insert into cls (name,age,sex,score) values(%s,%s,%s,%s);"
l=[('Dave', 17, 'm',81),('Ala',18,'w',84),('Eva',19,'w',91)]
try:
    # 法1
    # for i in l:
    #     cur.execute(sql,i)
    # 法2
    cur.executemany(sql,l)

    db.commit()
except:
    db.rollback()




# 关闭游标和数据库连接
cur.close()
db.close()