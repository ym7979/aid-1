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
st_name=input("输入学生姓名：")
# 读操作
# 方法1
# sql="select name,hobby,price from interest where name='%s';"%st_name
# print(sql)
# cur.execute(sql,[st_name])#执行sql语句

# 方法2
# sql="select name,hobby,price from interest where name=%s;"
# print(sql)
# cur.execute(sql,[st_name])#通过参数列表给sql传值


sql="select name,age,score from cls where score>%s and age<%s;"
print(sql)
cur.execute(sql,[80,18])#通过参数列表给sql传值
print(cur.fetchall())

# #获取结果 方法2
# one_row=cur.fetchone()#获取一条记录
# print(one_row)



# 关闭游标和数据库连接
cur.close()
db.close()