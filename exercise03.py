"""
create table words(
id int primary key auto_crement,
word varchar(32) not null,
mean varchar(1024) not null
);
create unique index w_k on words(word);
"""
import re
from socket import *
import pymysql

args_list=[]
while True:
    f = open('dict.txt')
    # 每次取一行
    for line in f:
        # w = line.split(' ', 1)[0]  # 提取单词
        # m = line.split(' ', 1)[1]  # 提取解释
        # print(w,"---",m.strip())
        l=re.findall(r"(\w+)\s+(.*)",line)
        args_list.extend(l)#合并列表




        # f.close()

    # 连接数据库
    db=pymysql.connect(host="localhost",
                       port=3306,
                       user="root",
                       password="123456",
                       database="dict",
                       charset="utf8")

    #生成游标对象（操作数据库，执行sql语句，获取结果）
    cur=db.cursor()

    sql="insert into cls (word,mean) values(%s,%s);"
    # cur.execute(sql,[w,m])

    # 关闭游标和数据库连接
    cur.close()
    db.close()
