# coding=gbk
import time
import csv
import sys
import os
from util.Open_DB import MYSQL
from util.config import MySQL_CONFIG, file_path, scheduler_file_path
from util.get_result_file_name import get_result_file_name


current_path = os.path.abspath(os.path.dirname(__file__))
root_path = os.path.split(current_path)[0]
sys.path.append(root_path)


class GetExecutionStatus(object):
    """
    该类用来获取批量创建的scheduler对应的execution，
    并查询到execution的最终执行状态，写入到一个CSV文件中
    """

    def __init__(self):
        """初始化数据库连接"""
        self.ms = MYSQL(MySQL_CONFIG["HOST"], MySQL_CONFIG["USER"], MySQL_CONFIG["PASSWORD"], MySQL_CONFIG["DB"])

    def exec_sql(self, scheduler_id):
        """
        根据schedulers id 查询出execution id
        创建scheduler后查询execution有延迟，需要加等待时间
        """
        time.sleep(3)
        # if scheduler:
        execution_sql = "select id,status_type, flow_name, flow_id from merce_flow_execution where flow_scheduler_id = '%s'" % scheduler_id
        try:
            result = self.ms.ExecuQuery(execution_sql)
            return result[0]
        except Exception:
            return

    def get_execution_status(self):
        # csv表的header: scheduler_id,execution_id,status,flow_name,flow_id
        # 读取jmeter脚本创建scheduler后保存scheduler id的CSV文件，依次查询到其对应的execution信息，并写入一个新的file中
        header = ('scheduler_id', 'execution_id', 'status', 'flow_name', 'flow_id')
        print("------开始执行get_execution_status(self)------\n")
        with open(scheduler_file_path, "r") as f:
            readers = csv.reader(f)
            headers = next(readers)  # 抛去header行
            executions = []
            executions.append(header)
            for scheduler_id in readers:
                # print('scheduler_id:', scheduler_id)
                e_info = self.exec_sql(scheduler_id[0])
                print(e_info)
                while not e_info:
                    time.sleep(5)
                    e_info = self.exec_sql(scheduler_id[0])
                    print(e_info)
                if e_info:
                    # 使用元祖存储execution信息，方便后续向csv中写数据
                    print('sql第一次查询后返回的execution信息', e_info)
                    count = 0
                    while e_info["status_type"] in ("PREPARE", "READY", "RUNNING"):
                        print("------进入while循环------\n")
                        # 状态为 ready 或者 RUNNING时，再次查询e_final_status
                        print("------查询前等待5S------\n")
                        time.sleep(5)
                        # 调用get_e_finial_status(e_scheduler_id)再次查询状态
                        e_info = self.exec_sql(scheduler_id[0])
                        # count += 1
                        # if count == 100:
                        #     break
                        print('再次查询后的execution"status_type"]', e_info)
                # 获取execution的最终执行状态后，将信息存入元祖，并依次append到列表executions中
                if e_info["status_type"] in ("SUCCEEDED", "FAILED", "KILLED"):
                    tp_execution = (scheduler_id[0],) + (e_info["id"],) + (e_info["status_type"],) + (
                    e_info["flow_name"],) + (e_info["flow_id"],)
                    # print("tp_execution", tp_execution)
                    executions.append(tp_execution)
                    print("executions", executions)

            # 依次从列表executions中读取元祖数据，并写入一个新的csv表中
            file_name = get_result_file_name(file_path)
            self.write_execution(file_name, executions)
            print('write over')

    @staticmethod
    def write_execution(file, executions):  # 向csv文件中写数据
        with open(file, 'a', newline='') as f:
            new_file = csv.writer(f, dialect='excel')
            m = len(executions)
            for i in range(m):
                print(executions[i])
                new_file.writerow(executions[i])


if __name__ == '__main__':
    g = GetExecutionStatus()

    g.get_execution_status()


