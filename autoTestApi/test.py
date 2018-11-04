# coding:utf-8
from common import Http

Http.post("http://ceshi.farmfriend.com.cn/management/sys/login","")


Http.saveJson('errmsg','token')

Http.add_header('token','errmsg')

Http.assert_equals('errno','13')

Http.saveJson('errmsg','token')
Http.assert_equals('errno','{id}')
#Http.post("http:params//ceshi.farmfriend.com.cn/management/sys/login","userName=123")
