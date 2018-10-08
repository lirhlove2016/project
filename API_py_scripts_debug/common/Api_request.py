# coding:utf-8
import requests
import json

from common.readexcel import ExcelUtil

#readfile = r"E:\mysoft\myworksapce\project\API_PY_scripts\casedata\myapidata.xlsx"


#封装requests
class  ApiRequest(object):
    def __init__(self,method,url,data,headers={}):
        self.url=url
        self.method=method
        self.data=data
        self.headers=headers

    #根据不同方法访问接口
    def api_request(self):
        #print('start request-----------------------------------------------')
        #print(self.method,self.url,self.data,self.headers)
        
        if self.method=='post':
            
            r=requests.post(self.url,data=self.data,headers=self.headers)
            return r

        elif self.method=='get':
            r=requests.get(self.url,params=self.data,headers=self.headers)
            return r
        elif self.method=='put':
            r=requests.put(self.url,params=self.data,headers=self.headers)
            return r
        elif self.method=='delete':
            r=requests.delete(self.url,headers=self.headers)
            return r
        else:
            print('%s is error.'%method)
        

    def get_code(self):
        #获取返回接口的状态码
        code=self.api_request().status_code
        return code

    def get_json(self):
        #获取返回信息json数据
        json_data=self.api_request().json()
        return json_data


if __name__=="__main__":
    #获取数据
    filepath = r"E:\mysoft\myworksapce\project\API_py_scripts_demo2\myapidata.xlsx"
    data = ExcelUtil(filepath).dict_data()

    count=len(data)
    print('count',count)
    for i in range(len(data)-3):
        print('----正在进行接口测试，开始第%d个请求---------------'%(i+1))
        datalist=[]    
        datalist=data[0]
        
        url="http://"+datalist['url'].strip()+ datalist['path'].strip()
        datas=datalist['params']
        method=datalist['method']
        headers={}
        headers['content-type']=datalist['headers']
        if datalist['tokenname']=='BDHAuthorization':
            tokenname=datalist['tokenname']
            headers[tokenname]=datalist['token']
        
        #print(method,url,datas,headers)
        
        my_request=ApiRequest(method,url,datas,headers)
        r=my_request.api_request()

        print('status_code',my_request.get_code())
        print('response',r.json())

            
        datalist['realresult']=r.json()
        #期望结果
        #ac_res=json.dumps(r.json)
        #print(ac_res)
        ex_result=datalist['expectedresult']
        if ex_result in r.json():
                print('{0}、{1}:测试成功。json数据为:{2}'.format(i + 1, datalist['casename'], r.json))
                datalist['result']='测试成功'
        else:
                print('{0}、{1}:测试失败'.format(i + 1, datalist['casename']))
                datalist['result']='测试失败'

        #保存所有数据
        reals.append(datalist)


