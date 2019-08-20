import pymysql
import configparser
import os
import json


def get_conn():
    conf = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/cfg.ini")
    conf.read(config_path, encoding="utf-8")
    conn = pymysql.connect(
        host=conf.get("db", "host"),
        port=int(conf.get("db", "port")),
        user=conf.get("db", "user"),
        password=conf.get("db", "password"),
        database=conf.get("db", "db"),
        charset="utf8")
    return conn


def invoke_sql(sql):
    conn = get_conn()
    # 获取一个光标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 返回字典数据类型

    # 定义将要执行的sql语句
    print(sql)
    # 拼接并执行sql语句
    cursor.execute(sql)
    # 取到查询结果
    ret = cursor.fetchall()  # 取一条
    print(ret)
    cursor.close()
    conn.close()
    return ret


def invoke_sql_file(file_paths):
    """
    执行某一个文件里面的SQL 一行一个SQL
    :param file_paths: 传入一个文件数组!!!
    :return:
    """
    for file_path in file_paths:
        conn = get_conn()
        cursor = conn.cursor()
        with open(file_path, encoding="utf-8") as f:
            try:
                for line in f:
                    cursor.execute(line)
            except Exception as e:
                print(e)
                # 失败回滚
                conn.rollback()
            else:
                conn.commit()
        cursor.close()
        conn.close()


if __name__ == '__main__':
    # ret = invoke_sql("SELECT * FROM gt_invoice_goods_type ")
    # for i in ret:
    #     print(i)
    # 执行SQL文件DEMO
    # invoke_sql_file(["E:\\test\\test_xietong\data\sql.txt"])
    sql = "SELECT * FROM  op_notice  where id= '%s'" %340796193636352
    results = invoke_sql(sql)
    for i in results:
        print(i['id'])
