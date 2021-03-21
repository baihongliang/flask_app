import pymysql

db = pymysql.connect(
    host='localhost',
    user='root',
    password='rootroot',
    db='test',
    charset='utf8mb4',
    # cursorclass=pymysql.cursors.DictCursor
)


def test_conn():
    with db.cursor() as cursor:
        sql = "show tables;"
        cursor.execute(sql)
        print(sql)
        print(cursor.fetchall())


def test_select():
    with db.cursor() as c:
        sql = "select * from test where sex=%s"
        c.execute(sql, ["男"])
        print(c.fetchall())

        #default
        #cursorclass=pymysql.cursors.DictCursor

        # ((1, 'xiaoming', '男'), (3, '校长', '男'))
        # [{'id': 1, 'name': 'xiaoming', 'sex': '男'}, {'id': 3, 'name': '校长', 'sex': '男'}]