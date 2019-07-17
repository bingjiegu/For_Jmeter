# coding:utf-8
import os


BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__name__)))
DATA_PATH = os.path.join(BASE_PATH, 'test_cases')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
email_user = 'ruifan_test@163.com'  # 发送者账号
email_pwd = 'ruifantest'       # 发送者密码
email_list = {
    'gubingjie': "bingjie.gu@inforefiner.com"
}
email_to = {
    "gubingjie": "bingjie.gu@inforefiner.com",
    "daming": "zhiming.wang@inforefiner.com",
            }

# ------84环境使用--------
#  HOST
# HOST_189 = "http://192.168.1.84:8515"
# # 数据库连接信息
# MySQL_CONFIG = {
#     'HOST': '192.168.1.189',
#     "PORT": 3306,
#     "USER": 'merce',
#     "PASSWORD": 'merce',
#     "DB": 'info4_merce',
#     'case_db': 'test'
# }

# ------83环境使用--------
# #  HOST
# HOST_189 = "http://192.168.1.83:8515"
# # 数据库连接信息
# MySQL_CONFIG = {
#     'HOST': '192.168.1.189',
#     "PORT": 3306,
#     "USER": 'merce',
#     "PASSWORD": 'merce',
#     "DB": 'wac',
#     'case_db': 'test'
# }

# # -------189环境使用-------
# HOST
# HOST_189 = "http://192.168.1.189:8515"
# # 数据库的连接配置，需要根据不同环境进行变更
# MySQL_CONFIG = {
#     'HOST': '192.168.1.199',
#     "PORT": 3306,
#     "USER": 'merce',
#     "PASSWORD": '123456',
#     "DB": 'merce',
#     'case_db': 'test'}

# # -------57环境使用-------
# HOST
# HOST_189 = "http://192.168.1.57:8515"
# # # # # 数据库连接信息
# MySQL_CONFIG = {
#     'HOST': '192.168.1.57',
#     "PORT": 3306,
#     "USER": 'merce',
#     "PASSWORD": 'merce',
#     "DB": 'merce'
# }

# MySQL_CONFIG = {
#     'HOST': '192.168.1.199',
#     "PORT": 3306,
#     "USER": 'merce',
#     "PASSWORD": '123456',
#     "DB": 'merce',
#     'case_db': 'test'
# }

# -------57环境使用-------
# HOST
# HOST_189 = "http://192.168.1.57:8515"
# # # # # 数据库连接信息
# MySQL_CONFIG = {
#     'HOST': '192.168.1.57',
#     "PORT": 3306,
#     "USER": 'merce',
#     "PASSWORD": 'merce',
#     "DB": 'merce'
# }
# file_path = "D://git//for_jmeter//result//"
# scheduler_file_path = "E://jmeter//cases//creates_scheduler_200//57//scheduler_id_57.csv"


# -------81环境使用-------
# HOST
HOST_189 = "http://192.168.1.81:8515"
# # # # 数据库连接信息
MySQL_CONFIG = {
    'HOST': '192.168.1.57',
    "PORT": 3306,
    "USER": 'merce',
    "PASSWORD": 'merce',
    "DB": 'database_81'
}
file_path = "D://git//For_Jmeter//for_jmeter//result//"
scheduler_file_path = "E://jmeter//cases//creates_scheduler_200//81//jmeter_script//scheduler_id_81.csv"