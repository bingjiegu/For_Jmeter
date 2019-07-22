import urllib.parse
import sys, os

current_path = os.path.abspath(os.path.dirname(__file__))
root_path = os.path.split(current_path)[0]
sys.path.append(root_path)


def get_env_num(host):
    host_netloc = urllib.parse.urlparse(host).netloc
    # print(host_netloc)
    no_port_host = host_netloc.split(":")
    # print(no_port_host)
    env_num = no_port_host[0].split(".")[-1]
    # print(env_num)
    return env_num

# host = "http://192.168.1.57:8515/api/datasets"
# print(get_env_num(host))