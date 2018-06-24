# encoding = utf-8
import pymysql
"""
1、下载并导入数据库：pymysql
2、获取数据连接：mymsql.Connect()
3、获取数据库游标：connet.cursor()
4、编写sql语句，比如查询用户表中所有元素：select  *  from  hd_user
5、通过游标执行语句:cursor.execute(select  *  from  hd_user)
6、通过游标执行结果:cursor.fetchall()
7、
8、
"""


class DBConnection:

    def execute_sql_command(self):
        conn = pymysql.Connect(host="127.0.0.1", user="root", password="root", database="pirate",
                    port=3306, charset='utf8')
        try:
            cursor = conn.cursor()
            sql = 'select username,email,mobile_phone  from  hd_user order by id desc;'
            cursor.execute(sql)
            # all_result = cursor.fetchall()
            # for raw in all_result:
            #     print(raw)
            raw = cursor.fetchone()
            conn.commit()
            print(raw)
            # return raw
        finally:
            conn.close()


if __name__ == '__main__':
    DBConnection().execute_sql_command()