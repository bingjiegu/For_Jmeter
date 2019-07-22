# encoding:utf-8


def get_host():
    print('请输入任务执行环境：')
    int_host = str(input())
    if int_host == '84':
        host = "http://192.168.1.84:8515"
        mysql_config = {"HOST": "192.168.1.189", "PORT": 3306, "USER": 'merce',  "PASSWORD": 'merce',  "DB": 'info4_merce', 'case_db': 'test'}
        return host, mysql_config
    elif int_host == '83':
        host = "http://192.168.1.83:8515"
        mysql_config = {"HOST": "192.168.1.189", "PORT": 3306, "USER": 'merce',  "PASSWORD": 'merce',  "DB": 'wac'}
        return host, mysql_config
    elif int_host == '189':
        host = "http://192.168.1.189:8515"
        mysql_config = {"HOST": "192.168.1.199", "PORT": 3306, "USER": 'merce', "PASSWORD": '123456', "DB": 'merce'}
        return host, mysql_config
    elif int_host == "57":
        host = "http://192.168.1.57:8515"
        mysql_config = {"HOST": "192.168.1.57", "PORT": 3306, "USER": 'merce', "PASSWORD": 'merce', "DB": 'merce'}
        return host, mysql_config
    elif int_host == '81':
        host = "http://192.168.1.81:8515"
        mysql_config = {"HOST": "192.168.1.57", "PORT": 3306, "USER": 'merce', "PASSWORD": 'merce', "DB": 'database_81'}
        return host, mysql_config
    elif int_host == '76':
        host = "http://192.168.1.76:8515"
        mysql_config = {"HOST": "192.168.1.76", "PORT": 3306, "USER": 'merce', "PASSWORD": 'merce', "DB": 'merce_76'}
        # print(host,mysql_config)
        return host, mysql_config
    else:
        print('输入的环境地址不存在，请再次输入')
        return get_host()


get_host = get_host()
HOST = get_host[0]
mysql_config = get_host[1]
