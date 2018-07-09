#   dev
from utils import db_mysql
print("testmdev")
sql = "SELECT * FROM tb_scm_goods limit 0,10"
sql = "SELECT goods_code,goods_name,is_delete FROM `tb_scm_goods` where goods_code = '100000005'"
sql2 = "update tb_scm_goods set is_delete = 1 where goods_code = '100000005'"
ss = db_mysql.dbSeeMysql(sql)
ss2 = db_mysql.dbHandleMysql(sql2)
ss3 = db_mysql.dbSeeMysql(sql)
for s in ss:
    print('==数据为==', s)
    print(s[0], s[1])
    print(type(s))

for s in ss2:
    print('==数据为==', s)

for s in ss3:
    print('==数据为==', s)

