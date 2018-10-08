# coding:utf-8
import json
import unittest
import time
import os
from common.readexcel import ExcelUtil
from common.Api_request import ApiRequest 
import conf


testxlsx = r"E:\mysoft\myworksapce\project\API_py_scripts_demo2\myapidata.xlsx"

testxlsx=conf.testxlsx
print(testxlsx)

class testAPI(unittest.TestCase):

    def test_bdh_api(self):
        #获取数据
        data,key_names= ExcelUtil(testxlsx).dict_data()
        print(key_names)
        reals=[]
        count=len(data)
        print('count',count)
        suc_num=0
        for i in range(len(data)):
            print('--正在进行接口测试，开始第%d个请求---------------'%(i+1))
            datalist=[]    
            datalist=data[i]
            
            url="http://"+datalist['url'].strip()+ datalist['path'].strip()
            datas=datalist['params']
            method=datalist['method']
            headers={}
            headers['content-type']=datalist['headers']
            if datalist['tokenname']=='BDHAuthorization':
                tokenname=datalist['tokenname']
                headers[tokenname]=datalist['token']
            
            
            print("-------请求参数-----------------") 
            print(method)
            print(url)
            print('header:',headers)
            print('data',datas)

            print("-------返回参数-----------------") 
            my_request=ApiRequest(method,url,datas,headers)
            r=my_request.api_request()

            print('code',my_request.get_code())
            print('response',r.json())
            res=r.json()
            datalist['realresult']=r.json()
            #期望结果
            ex_result=datalist['expectedresult']
            
            if ex_result in res:
                print('第{0}个接口，{1}:测试成功。\njson数据为:{2}'.format(i + 1, datalist['casename'], r.json()))
                datalist['result']='测试成功'
                suc_num=suc_num+1
            else:
                print('第{0}个接口，{1}:测试失败。\njson数据为:{2}'.format(i + 1, datalist['casename'], r.json()))
                datalist['result']='测试失败'

            #保存所有数据
            reals.append(datalist)
            #print(datalist)
        return suc_num,reals,key_names

    
if __name__=="__main__":
    unittest.main()
    

    
    
