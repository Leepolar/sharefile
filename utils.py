import pymysql


def get_conn():
    # 建立连接
    conn = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="cov", charset="utf8")
    # c创建游标A
    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()


class FILE(object):
    def __init__(self):
        self.__conn, self.__cursor = get_conn()

        sql = "create files"
        self.__cursor.execute(sql, )

    def download_file(self):
        sql = "select * from files"
        self.__cursor.execute(sql, )
        res = self.__cursor.fetchall()
        close_conn(self.__conn, self.__cursor)
        return res
        pass

    def upload_file(self):
        sql = "insert into files"
        self.__cursor.execute(sql, )
        close_conn(self.__conn, self.__cursor)
        res = True
        return res
        pass


def download_file():
    file = FILE()
    f = file.download_file()
    return f


def upload_file():
    file = FILE()
    f = file.upload_file()
    return f

