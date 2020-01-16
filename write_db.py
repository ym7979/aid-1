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


# 写sql操作
try:
    # 法1
    # sql="insert into cls (name,age,score) values('Tom',17,96);"
    # cur.execute(sql)
    # 法2
    sql="insert into cls (name,age,score) values(%s,%s,%s);"
    cur.execute(sql,['Alex',18,85])

    # sql="update cls set sex='m' where name='aa'"
    # cur.execute(sql)

    # sql="delete from cls where sex is null"
    # cur.execute(sql)


    db.commit()#同步到数据库
except Exception:
    db.rollback()#数据库回滚

# 关闭游标和数据库连接
cur.close()
db.close()