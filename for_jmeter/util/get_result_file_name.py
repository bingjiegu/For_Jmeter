import time
import sys, os

current_path = os.path.abspath(os.path.dirname(__file__))
root_path = os.path.split(current_path)[0]
sys.path.append(root_path)

from util.config import HOST_189
from util.get_env_num import get_env_num


def get_result_file_name(path):
    time_format = time.strftime(time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime()))
    file_name = path + time_format + "&env" + get_env_num(HOST_189) + ".csv"
    return file_name
