import pymysql
connect = pymysql.connect(host='localhost',port=3306, user='root', password='password', db='mytest', charset='utf8')
#conn = mysql.connector.connect(user='root', password='password', database='mytest')
cursor = connect.cursor()
cursor.execute('select id,name from student')
# fetchall返回的数据是一个tuple.
values = cursor.fetchall()

# 删除name 相同的数据
print(values)
list_1=[]
list_2=[]
for i in range(len(values)):
    if values[i][1] in list_2:
        list_1.append(values[i][0])
    else:
        list_2.append(values[i][1])
for k in list_1:
    cursor.execute('delete from student where id=%s', [k, ])

# cursor.execute('insert into student(name, sex, date, content) values(%s, %s, %s, %s)',
             #  ['nihao', 'female','1994','none'])

connect.commit()
cursor.close()
connect.close()


#cursor.execute('select * from student')

