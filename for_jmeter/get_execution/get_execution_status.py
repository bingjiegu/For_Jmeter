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
    ����������ȡ����������scheduler��Ӧ��execution��
    ����ѯ��execution������ִ��״̬��д�뵽һ��CSV�ļ���
    """

    def __init__(self):
        """��ʼ�����ݿ�����"""
        self.ms = MYSQL(MySQL_CONFIG["HOST"], MySQL_CONFIG["USER"], MySQL_CONFIG["PASSWORD"], MySQL_CONFIG["DB"])

    def exec_sql(self, scheduler_id):
        """
        ����schedulers id ��ѯ��execution id
        ����scheduler���ѯexecution���ӳ٣���Ҫ�ӵȴ�ʱ��
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
        # csv���header: scheduler_id,execution_id,status,flow_name,flow_id
        # ��ȡjmeter�ű�����scheduler�󱣴�scheduler id��CSV�ļ������β�ѯ�����Ӧ��execution��Ϣ����д��һ���µ�file��
        header = ('scheduler_id', 'execution_id', 'status', 'flow_name', 'flow_id')
        print("------��ʼִ��get_execution_status(self)------\n")
        with open(scheduler_file_path, "r") as f:
            readers = csv.reader(f)
            headers = next(readers)  # ��ȥheader��
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
                    # ʹ��Ԫ��洢execution��Ϣ�����������csv��д����
                    print('sql��һ�β�ѯ�󷵻ص�execution��Ϣ', e_info)
                    count = 0
                    while e_info["status_type"] in ("PREPARE", "READY", "RUNNING"):
                        print("------����whileѭ��------\n")
                        # ״̬Ϊ ready ���� RUNNINGʱ���ٴβ�ѯe_final_status
                        print("------��ѯǰ�ȴ�5S------\n")
                        time.sleep(5)
                        # ����get_e_finial_status(e_scheduler_id)�ٴβ�ѯ״̬
                        e_info = self.exec_sql(scheduler_id[0])
                        # count += 1
                        # if count == 100:
                        #     break
                        print('�ٴβ�ѯ���execution"status_type"]', e_info)
                # ��ȡexecution������ִ��״̬�󣬽���Ϣ����Ԫ�棬������append���б�executions��
                if e_info["status_type"] in ("SUCCEEDED", "FAILED", "KILLED"):
                    tp_execution = (scheduler_id[0],) + (e_info["id"],) + (e_info["status_type"],) + (
                    e_info["flow_name"],) + (e_info["flow_id"],)
                    # print("tp_execution", tp_execution)
                    executions.append(tp_execution)
                    print("executions", executions)

            # ���δ��б�executions�ж�ȡԪ�����ݣ���д��һ���µ�csv����
            file_name = get_result_file_name(file_path)
            self.write_execution(file_name, executions)
            print('write over')

    @staticmethod
    def write_execution(file, executions):  # ��csv�ļ���д����
        with open(file, 'a', newline='') as f:
            new_file = csv.writer(f, dialect='excel')
            m = len(executions)
            for i in range(m):
                print(executions[i])
                new_file.writerow(executions[i])


if __name__ == '__main__':
    g = GetExecutionStatus()

    g.get_execution_status()


