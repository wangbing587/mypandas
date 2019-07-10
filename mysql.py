#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : WangBing
@Email   : wangbing587@163.com
@Time    : 2019/7/10 10:07
@File    : mysql.py
@Desc  : 数据库的保存和读取
"""

import pandas as pd
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()
host = '127.0.0.1'
port = 3306
db = 'edu'
user = 'root'
password = 'bing'

# 存储
engine = create_engine(r'mysql+mysqldb://{}:{}@localhost:{}/{}?charset=utf8'.format(user, password, port, db))
df = pd.DataFrame({'名字': ['张三', '李四', '王五'],
                   'name': ['ZhangSan', 'LiSi', 'WangWu'],
                   'age': [16, 25, 35],
                   '体重': [55.5, 65.23, 60.12]})
df.to_sql(name='result', con=engine,  if_exists='replace', index=None)

# 读取
con = pymysql.connect(host=host, user=user, password=password, db=db)
data = pd.read_sql('select * from result', con=con)
print(data)