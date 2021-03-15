#coding:utf-8
import requests
import json
import mock
import yaml


def mock_request(mock_method,method,url,request_data,response_data):
    '''
    mock虚拟对象模拟请求接口方法
    :mock_method: 接口请求方法
    :param method: POST/GET
    :param url: url
    :param request_data: 请求体
    :param response_data: 响应体
    :return: 返回响应体
    '''
    mock_method = mock.Mock(return_value=response_data)
    res = mock_method(url,method,request_data)
    #res = mock_request(RunMethod,'POST',url,test_data,test_data)
    return res

"""
·需要二次封装requests，对请求进行定制化
·将请求结构体url从一个写死ip替换成动态域名
·使用env配置文件，存放环境配置信息
·将请求结构中的url替换未env配置文件中的url
·将env配置文件使用yaml进行管理
"""
class Api:

    req_data = {
        "method": "get",
        "url": "register/",
        "headers": None,
        "json": None,
        "data": None,
        "encoding": "base64"
    }

    with open('../common/env.yaml','r')as f:
        env = yaml.safe_load(f)

    '''
    def __init__(self):
        #初始化token信息写入session
        self.token = requests.get(self.req_data['url']).json()['access_token']  # 拿到token信息
        self.req_session = requests.Session()
        self.req_session.params = {'access_token': self.token}
    '''

    def send(self, data:dict):
        # data['url'] = str(data['url']).replace('test', self.env['test_studio'][self.env['defult']])#字符串替换
        data['url'] = self.env['test_studio'][self.env['defult']]+data['url']
        res = requests.request(method=data['method'], url=data['url'], headers=data['headers'], json=data['json'],data=data['data'])
        return res

if __name__ == '__main__':
    req_data1 = {
        "method": "get",
        "url": "data/stocklevel.json",
        "headers": None,
        "json": None,
        "data": None,
        "encoding": "base64"
    }
    print(Api().send(req_data1).json())

