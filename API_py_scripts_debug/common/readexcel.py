# coding:utf-8
import xlrd

class ExcelUtil():
    def __init__(self, excelPath, sheetName="Sheet1"):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in list(range(self.rowNum-1)):
                s = {}
                # 从第二行取对应values值
                s['rowNum'] = i+1
                
                #print(s['rowNum'])
                
                values = self.table.row_values(j)
                for x in list(range(self.colNum)):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
                
            return r,self.keys
        
if __name__ == "__main__":
    '''
    filepath = r"E:\mysoft\myworksapce\project\API_py_scripts_demo2\myapidata.xlsx"
    sheetName = "Sheet1"
    data= ExcelUtil(filepath,sheetName)
    datas,keys=data.dict_data()
    print(keys)

    '''
    '''
    print(data.dict_data())
    print(type(data.dict_data()))

    d=data.dict_data()
    print(d[0]['url'])
    print(len(d))
    '''
    
