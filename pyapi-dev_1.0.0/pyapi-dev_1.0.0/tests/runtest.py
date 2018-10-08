# coding:utf-8
import os
import sys
import time
import unittest

from pyapi.common.apirequest import ApiRequest
from pyapi.common.excelutil import ExcelUtil
from pyapi.common.fileutil import FileUtil
from pyapi.common.htmltestrunner import HTMLTestRunner
from pyapi.conf.global_settings import DATADIR, REPORTDIR

reload(sys)
sys.setdefaultencoding('utf-8')


class TestFramework(unittest.TestCase):
    def scan_datadir_xlsx_call(self):
        list_file_name = []
        FileUtil.listdir(DATADIR, list_file_name, '_result')
        for file_name in list_file_name:
            file_name_result = "{0}_result.{1}".format(file_name.split('.')[0], file_name.split('.')[1])
            if os.path.exists(file_name_result):
                os.remove(file_name_result)
            f = open(file_name_result, 'w')
            f.close()

            # 获取数据
            data, key_names = ExcelUtil.dict_data(file_name)
            reals = []
            count = len(data)
            print('接口总数', count)
            suc_num = 0
            for i in range(len(data)):
                print('--正在进行接口测试，开始第%d个请求---------------' % (i + 1))
                datalist = data[i]

                url = "http://" + datalist['url'].strip() + datalist['path'].strip()
                datas = datalist['params']
                method = datalist['method']
                headers = {'content-type': datalist['headers']}
                if datalist['tokenname'] == 'BDHAuthorization':
                    tokenname = datalist['tokenname']
                    headers[tokenname] = datalist['token']
                print("-------请求参数-----------------")
                print(method)
                print(url)
                print('header:', headers)
                print('data', datas)

                print("-------返回参数-----------------")
                my_request = ApiRequest(method, url, datas, headers)
                r = my_request.api_request()

                print('code', my_request.get_code())
                print('response', r.json())
                datalist['realresult'] = str(r.json())
                # 期望结果
                ex_result = datalist['expectedresult']
                ac_result = datalist['realresult']

                if ex_result in ac_result:
                    print('第{0}个接口，{1}:测试成功。\njson数据为:{2}'.format(i + 1, datalist['casename'], r.json()))
                    datalist['result'] = '测试成功'
                    suc_num = suc_num + 1
                else:
                    print('第{0}个接口，{1}:测试失败。\njson数据为:{2}'.format(i + 1, datalist['casename'], r.json()))
                    datalist['result'] = '测试失败'

                # 保存所有数据
                reals.append(datalist)

        ExcelUtil.write_excel(file_name_result, reals, key_names)
        return suc_num, reals, key_names


if __name__ == "__main__":
    suite = unittest.TestSuite()

    suite.addTest(TestFramework('scan_datadir_xlsx_call'))
    now = time.strftime("%Y-%m-%d %M-%H_%M_%S", time.localtime(time.time()))
    htmlreport = os.path.join(REPORTDIR, "{0}_result.html".format(now))

    fp = open(htmlreport, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            verbosity=2,
                            title="测试报告",
                            description="用例执行情况")
    # 调用add_case函数返回值
    runner.run(suite)
    fp.close()
