# _*_coding:utf-8_*_
__author__ = 'wmx'
__date__ = '2019/4/18 10:52'

import  MySQLdb,uuid

class DBHelper():
    #插入数据
    def insert_api(line):
        MYSQL_HOST = 'localhost'
        MYSQL_DBNAME = 'mysql'
        MYSQL_USER = 'root'
        MYSQL_PASSWD = 'root12#$'
        # host = settings['MYSQL_HOST']
        # db = settings['MYSQL_DBNAME']
        # user = settings['MYSQL_USER']
        # passwd = settings['MYSQL_PASSWD']
        db = MySQLdb.connect(host=MYSQL_HOST,user=MYSQL_USER,passwd=MYSQL_PASSWD,db=MYSQL_DBNAME,port=3306)
        cur = db.cursor()
        insert_sql = """
            insert into interface_details(id,trs_code_id,trs_name,fuc_desc,eng_name,chinese_name,data_type,required,remark,flag)
              values (%s,%s, %s, %s,%s,%s,%s, %s,%s,%s)
                """
        cur.execute(insert_sql,
                    (str(uuid.uuid1()), line[0], line[1], line[2], line[3], line[4], line[5], line[6],
                     line[7], line[8])
                    )
        db.commit();



