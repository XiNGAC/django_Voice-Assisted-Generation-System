import  pymysql
pymysql.install_as_MySQLdb()

# 打开数据库链接
db = pymysql.connect("localhost", "root", "123456", "sql_db",)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用fetchone()方法获取亿条数据库
data = cursor.fetchone()

print("database version: %s " % data)

db.close()

