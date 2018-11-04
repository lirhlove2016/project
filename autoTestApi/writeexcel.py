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
    pass