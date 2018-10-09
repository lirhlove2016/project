# coding:utf-8
import json
from conf.conf import TOKEN
from conf.conf import API_ENV,API_ENV_ON,API_ENV_NOW

class DataUtil:
    
    def get_url(self,url):
        if API_ENV_ON:
            url=API_ENV[API_ENV_NOW]
        else:
            if url=="BDH" or url=="bdh":
                url=API_ENV['bdh']
            elif url=="ceshi" or url=="CESHI":
                url=API_ENV['ceshi']
            elif url=="dev" or url=="DEV":
                url=API_ENV['dev']
                
        return url
     
    def save_token(self,savetoken):
        pass

    
    def get_token(self,tokenname,token):
        name=tokenname.upper()
        location=""
        if  name=="BDH":
                tokenname=TOKEN["BDH"]["name"]
                token=TOKEN["BDH"]["token"]
                location=TOKEN["BDH"]["location"]
        elif  name=="FSD":
                tokenname=TOKEN["FSD"]["name"]
                location=TOKEN["FSD"]["location"]
                token=TOKEN["FSD"]["token"]
        elif  name=="YWB":
                tokenname=TOKEN["YWB"]["name"]
                location=TOKEN["YWB"]["location"]
                token=TOKEN["YWB"]["token"]
        elif  name=="SYS_FF":
                tokenname=TOKEN["SYS_FF"]["name"]
                location=TOKEN["SYS_FF"]["location"]
                token=TOKEN["SYS_FF"]["token"]
        elif  name=="SYS_SG":
                tokenname=TOKEN["SYS_SG"]["name"]
                location=TOKEN["SYS_SG"]["location"]
                token=TOKEN["SYS_SG"]["token"]
        return tokenname,token,location     

if __name__=="__main__":
    f= DataUtil()
    f.get_url("ceshi")
    f.get_token('BDH','token')
