#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
version=1.0

'''
1.datafile
2.timeout
3.token设置,引用-TOKEN["BDH"]["token"]
4.环境参数
5.目录自动获取
'''

#设置目录
#filepath=r"E:\mysoftware\mygitwork\project\API_py_scripts_debug"
filepath=os.path.abspath(os.path.join(os.getcwd(), ".."))
dataDir=os.path.join(filepath,'datadir')
reportDir=os.path.join(filepath,'report')
#timeout
TIMEOUT=10
#token
TOKEN={
    "BDH":{"name":"BDHAuthorization","location":"header","token":"B94ftK1WY6JSUe7hBTfmgOsGckPFbW8dRASuVNQ52ag5f9pS//4V5E66NZNgQq9tnw2GwdcnZgG7Nz6SEv/klZB+VHjS3DzMCKDb92L",},
    "YWB":{"name":"token","location":"param","token":"B94ftK1WY6JSUe7hBTfmgOsGckPFbW8dRASuVNQ52ag5f9pS//4V5E66NZNgQq9tnw2GwdcnZgG7Nz6SEv/klZB+VHjS3DzMCKDb92L",},
    "FSD":{"name":"token","location":"param","token":"kPFbW8dRASuVNQ52ag5f9pS",},
    "SYS_FF":{"name":"FARMFRIEND","location":"param","token":"B94ftK1WY6JSUe7hBTfmgOsGckPFbW8dRASuVNQ52ag5f9pS",},
    "SYS_SG":{"name":"FRIENDFRIEND","location":"param","token":"B94ftK1WY6JSUe7hBTfmgOsGckPFbW8dRASuVNQ52ag5f9pS",},    
}

#domain
API_ENV_ON=False #切换环境用,false,使用数据表
API_ENV_NOW="ceshi"

API_ENV={
    "ceshi":"ceshi.farmfiend.cn",
    "bdh":"dev01.bdhlan.com:8080/bdhsystem",
    "dev":"dev.farmfiend.cn",
    "api":"",
}


if __name__=="__main__":
    print(dataDir)
    print(reportDir)
    print(TOKEN["BDH"]["token"])
    
