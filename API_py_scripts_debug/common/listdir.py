#_*_coding:utf-8_*_
import os

"""
实现
1.获取数据目录下的data文件，不算result文件

"""

#1
def Listdir(path,list_name,result):
    for f in os.listdir(path):
        #print(f)
        file_path=os.path.join(path,f)
        if os.path.isdir(file_path):
                listdir(file_path,list_name,result)
                
        elif file_path.split('.')[1]=='xlsx' or file_path.split('.')[1]=='xls':            
            if not result in file_path:
                list_name.append(file_path)
    return list_name

#2
def Scan_excel_file(path,result):
    list_name=[]
    listname=listdir(path,list_name,result)
    '''
    for i in listname:
        print(i)    
    '''
    for file_name in listname:        
        file_name_result=file_name.split('.')[0]+'_result.xlsx'
        print(file_name,file_name_result)
        if os.path.exists(file_name_result):
            os.remove(file_name_result)
             
    
if __name__=="__main__":
    path="E:\\download"
    list_name=[]
    #1
    names=listdir(path,list_name,"_result")
    for i in names:
        print(i)
    #2    
    print('-----')    
    scan_excel_file(path,"_result")
