# 数据库操作
import pymysql


# 查数据
def dbSeeMysql(SQL):
    """
    :param SQL:传入SQL
    :return:返回结果
    如：ss = db_mysql.dbMysql(sql)
    """

    # 数据准备
    HOST = '10.18.75.230'
    PORT = 3307
    username = 'tomato_scm'
    password = 'rsAz9ydTd52A0E5J'
    DB = 'test_tomato_scm'
    # 打开数据库连接，生成数据库对象
    db = pymysql.Connect(host=HOST, port=PORT, user=username, passwd=password, db=DB, charset='utf8')
    print('=======操作数据库======')
    cursor = db.cursor()                    # 使用 cursor() 方法创建一个游标对象 cursor
    # 使用 execute()  方法执行 SQL 查询
    try:
        cursor.execute(SQL)                 # 执行SQL语句
    except:
        db.rollback()                       # 发生错误时回滚
    results = cursor.fetchall()             # 获取所有记录列表
    n = cursor.rowcount                     # 获取最近一次execute返回数据的行数或影响行数
    print('==涉及%d条数据==' % n)
    db.close()                              # 关闭数据库连接
    return results

# 操作数据
def dbHandleMysql(SQL):
    """
    :param SQL:传入SQL
    :return:返回结果
    如：ss = db_mysql.dbMysql(sql)
    """

    # 数据准备
    HOST = '10.18.75.230'
    PORT = 3307
    username = 'tomato_scm'
    password = 'rsAz9ydTd52A0E5J'
    DB = 'test_tomato_scm'
    # 打开数据库连接，生成数据库对象
    db = pymysql.Connect(host=HOST, port=PORT, user=username, passwd=password, db=DB, charset='utf8')
    print('=======操作数据库======')
    cursor = db.cursor()                    # 使用 cursor() 方法创建一个游标对象 cursor
    # 使用 execute()  方法执行 SQL 查询
    try:
        cursor.execute(SQL)                 # 执行SQL语句
        db.commit()                         # 保存修改
    except:
        db.rollback()                       # 发生错误时回滚
    results = cursor.fetchall()             # 获取所有记录列表
    n = cursor.rowcount                     # 获取最近一次execute返回数据的行数或影响行数
    print('==涉及%d条数据==' % n)
    db.close()                              # 关闭数据库连接
    return results

if __name__ == "__main__":
    # 查询sql
    sql = "SELECT * FROM tb_scm_shop_stock where shop_id = '7366536722120704' and is_delete = 0"
    sql3 = "SELECT * FROM tb_scm_goods limit 0,10"

    ss = dbSeeMysql(sql)
    for s in ss:
        print('======', s)

    ss = dbSeeMysql(sql3)
    for s in ss:
        print('======', s)

