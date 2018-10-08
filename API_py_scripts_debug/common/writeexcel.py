#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlwt
from  xlrd import *
from xlutils.copy import copy



def write_excel_m(old,newfile,datas,names):
    """修改数据"""
    rb =open_workbook(old)
    wb = copy(rb)
    sheet = wb.get_sheet(0)    
    #sheet.write(0,1,"new data")
    for i in range(len(names)):
            sheet.write(0,i,names[i])
    
    wb.save(newfile)
    print ("write finished")

def write_excel(filepath,datas,names):
    """写入数据"""
    f = xlwt.Workbook(encoding='utf-8', style_compression=0)             
    sheet= f.add_sheet(u'sheet1',cell_overwrite_ok=True) 
    n=[]
    for i in range(len(names)):
        
        sheet.write(0,i,names[i])
        n.append(names[i])
   
    #写入数据
    d=[]
    for i in range(len(datas)):
        value=datas[i]
        #print("正在写入第{0}行，数据{1}".format(i+1,value)) 
        for j in range(len(names)):         
            key=names[j]
            if key=='Id':
                strValue=int(value[key])
            else:
                strValue=str(value[key])               
            sheet.write(i+1,j,strValue)       

        d.append(datas[i])                 
    f.save(filepath)
    print ("write finished")

if __name__=="__main__":
    #write_excel_m(old,newfile,datas,key_names)
    '''
    oldfile=r"E:\mysoft\myworksapce\project\API_py_scripts_demo2\myapidata.xlsx"
    newfile=r"E:\mysoft\myworksapce\project\API_py_scripts_demo2\result.xls"

    names=['Id', 'casename', 'url', 'path', 'method', 'params', 'headers', 'expectedresult', 'realresult', 'result', 'tokenname', 'token']
    datas=[{'realresult': '', 'rowNum': 1, 'method': 'get', 'casename': '根据id获取地块', 'Id': 1, 'path': '/farmplantend/farmlands/count', 'url': 'dev01.bdhlan.com:8080/bdhsystem', 'token': '', 'expectedresult': '', 'params': '', 'tokenname': '', 'headers': 'application/x-www-form-urlencoded', 'result': ''}, {'realresult': '', 'rowNum': 2, 'method': 'post', 'casename': 'bdh用户登录', 'Id': 2, 'path': '/farmplantend/plantUser/loginOrReg', 'url': ' dev01.bdhlan.com:8080/bdhsystem', 'token': '', 'expectedresult': '登陆成功', 'params': 'checkCode=9331&mobilePhone=18301212965', 'tokenname': '', 'headers': 'application/x-www-form-urlencoded;charset=utf-8', 'result': ''}, {'realresult': '', 'rowNum': 3, 'method': 'get', 'casename': 'bdh获取钱包余额', 'Id': 3, 'path': '/farmplantend/plantUserWallet', 'url': ' dev01.bdhlan.com:8080/bdhsystem', 'token': '', 'expectedresult': '', 'params': '', 'tokenname': 'BDHAuthorization', 'headers': 'application/x-www-form-urlencoded;charset=utf-8', 'result': ''}]
    my_request=testAPI()
    suc_num,datas,names=my_request.test_bdh_api()

    #write_excel_m(oldfile,newfile,datas,names)  
    write_excel(newfile,datas,names)
    '''
