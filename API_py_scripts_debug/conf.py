#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


#1手动设置
curpath=os.path.split(os.path.realpath(__file__))[0]
#testxlsx=curpath+"\\myapidata.xlsx"
testxlsx=curpath+"\\myapidata-all.xlsx"
newfile=curpath+"\\result.xls"                    
#print(curpath,testxlsx,newfile)

#2设置目录
filepath="E:\\mysoftware\\mygitwork\\project\\API_py_scripts_debug"
dataDir=os.path.join(filepath,'datadir')
reportDir=os.path.join(filepath,'report')
  
if __name__=="__main__":
    print(dataDir)
    print(reportDir)