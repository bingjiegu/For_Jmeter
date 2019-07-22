# coding:utf-8
import os
from util.encrypt import encrypt_rf
from util.get_host import HOST

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


MY_LOGIN_INFO = {
 "HEADERS": {'Content-Type': 'application/x-www-form-urlencoded'},
 "URL": "%s/api/auth/login" % HOST,
 "DATA": {'name': encrypt_rf('admin'), 'password': encrypt_rf('123456'), 'version': 'Europa-3.0.0.19 - 20180428', 'tenant': encrypt_rf('default')},
 "DATA_ERROR_NAME": {'name': encrypt_rf('adminn'), 'password': encrypt_rf('123456'), 'version': 'Europa-3.0.0.19 - 20180428', 'tenant': encrypt_rf('default')},
 "HOST": "%s" % HOST
}

MY_LOGIN_INFO_dam = {
 "HEADERS": {'Content-Type': 'application/x-www-form-urlencoded'},
 "URL": "%s/api/auth/login" % HOST,
 "DATA": {'name': '13ec4fe486e87d0b1145f2248a090db5', 'password': '3cde4fd05c58aee9937bfb2db12c9a91', 'version': 'Baymax-3.0.0.23-20180606', 'tenant': '1463a3ec85fbfbeb2fe07183d7518a48'},
 "DATA_ERROR_NAME": {'name': encrypt_rf('adminn'), 'password': encrypt_rf('123456'), 'version': 'Europa-3.0.0.19 - 20180428', 'tenant': encrypt_rf('default')},
 "HOST": "%s" % HOST
}


file_path = "D://git//For_Jmeter//for_jmeter//result//"

scheduler_file_path = "E://jmeter//cases//creates_scheduler_200//57//scheduler_id_57.csv"









# file_path = "D://git//For_Jmeter//for_jmeter//result//"
# scheduler_file_path = "E://jmeter//cases//creates_scheduler_200//81//jmeter_script//scheduler_id_81.csv"