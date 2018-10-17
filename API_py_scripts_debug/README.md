#rest接口测试
# v1.0
## 一、操作步骤
> 1.将项目下载到本地 

> 2.需要python环境python 3.x 

> 3.需要安装库,xlrd,xlwt,xlutils
>> 库文件安装命令参考：pip install xlrd 

> 4.自己数据，存到myapidata.xlsx文件中，各数据说明
>>	1）url,传入url地址，如，dev01.bdhlan.com:8080/bdhsystem     
>>	2）path,url后请求的路径，如，/farmplantend/farmlands/count  
>>	3）params：传入参入，如：page=1&rows=10；或
```
{ \"farmlandName\": \"3号地块\", \"farmlandArea\": \"10\", \"type\": 1, \"farmlandLevel\": 2, \"farmlandSoilQuality\": 2, \"pictures\": [ \"http://farmlandbucketstest.oss-cn-beijing.aliyuncs.com/21B7F1920D734078898AD63088736D55\" ], \"userId\": \"1\", \"otherInstructions\": \"\" }    
```
>>	4）headers,传入的header['content-type'],值，如1，application/json   
>>	5）expectedresult：期望的校验值，如，{ "errno" : 0, "errmsg" : null, "data" : null }；如2，登陆成功     
>>	6）realresult，不用输入，实际的返回值   
>>	7）result，校验结果，测试成功 ，测试失败    
>>	8）tokenname，需要传入的token的名，如，BDHAuthorization；   
	             注意：目前token传入header  
>>	9）token：token的值 
		           	           
> 4.本地运行方法：  
>>	cmd进入命令行       
>>	cd 项目所在目录         
>>	python  test_bdh_api_write.py   
	
> 5.查看结果
>>	查看excel:result文件	
>> 	查看html:report目录下x.html，查看最新的报告即可。
	
## 二、集成jenkins后，
>  1、先把自己的数据替换myapidata.xlsx文件    
>  2、再直接执行job，查看结果文件

## 三、TODOLIST
>  1、excel格式校验以及错误提示         
>  2、excel中增加request设置超时、expectedresult和realresult增加json级别比对  
>  3、token能够每次动态获取           
>  4、增加setup.py自动依赖      
>  5、conf文件中的项目路径不需要每次人工配置