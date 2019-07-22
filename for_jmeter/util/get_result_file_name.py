# encoding:utf-8
import time
import sys
import os
from util.get_host import HOST
from util.get_env_num import get_env_num

current_path = os.path.abspath(os.path.dirname(__file__))
root_path = os.path.split(current_path)[0]
sys.path.append(root_path)


def get_result_file_name(path, host):
    # HOST = get_host()[0]
    time_format = time.strftime(time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime()))
    if '57' in host:
        file_name = path + '57//'+time_format + "&env" + get_env_num(HOST) + ".csv"
        return file_name
    elif '81' in host:
        file_name = path + '81//'+time_format + "&env" + get_env_num(HOST) + ".csv"
        return file_name
    else:
        print('目前只有57和81环境的result信息')

# path =  "D://git//For_Jmeter//for_jmeter//result//"
# from util.get_host import HOST
# print(get_result_file_name(path, HOST))