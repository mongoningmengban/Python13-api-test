# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""
"""
hTTP 协议两大部分
Request：
请求方法：
GET  查--获取资源
POST 改---修改资源
PUT  增加
DELETE 删除
OPTION
HEADER
请求URL： 协议://服务器IP地址：端口号/接口路径
请求参数：传参方式？
header 请求头： Content-type
cookie

response：
状态码
•1XX－信息类(Information),表示收到Web浏览器请求，正在进一步的处理中

•2XX－成功类（Successful）,表示用户请求被正确接收，理解和处理例如：200 OK

•3XX-重定向类(Redirection),表示请求没有成功，客户必须采取进一步的动作。

•4XX-客户端错误(Client
Error)，表示客户端提交的请求有错误 例如：404 NOT
Found。

•5XX-服务器错误(Server
Error)表示服务器不能完成对请求的处理：如 500

响应信息
cookie
header
"""

""""
requests 使用总结
根据不同的请求方式调用不同的requests函数
比如说get： requests.get(),requests.post(),requests.delete() 依次类推。。。。
请求参数说明：
method,
url,
params=None,
data=None, 
headers=None, 
cookies=None, 
files=None,
auth=None, 
timeout=None, 
allow_redirects=True, 
proxies=None,
hooks=None,
stream=None, 
verify=None, 
cert=None, 
json=None):

"""

# 构造请求
# resp = requests.get('http://cn.python-requests.org/zh_CN/latest/')
# resp.encoding = 'utf-8'  # 解决乱码
# print('响应码', resp.status_code)
# print('响应信息', resp.text)
# with open('index.html', 'w+', encoding='utf-8') as file:
#     file.write(resp.text)


# 登录接口 get ---url传参 ---params
# data = {'mobilephone':'15810447656',"pwd":"123456"}
# resp = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/login',params=data)  # PARAMS url 传参
# print('请求url',resp.request.url)
# print('请求参数',resp.request.body)
# print('响应码', resp.status_code)
# print('响应信息', resp.text)

# 登录接口 post ---表单传参 ---data
# data = {'mobilephone': '15810447656', "pwd": "123456"}
# resp = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/login', data=data)
# print('请求url', resp.request.url)
# print('请求参数', resp.request.body)
# print('请求headers', resp.request.headers)
# print('请求cookies', resp.request._cookies)
# print('响应码', resp.status_code)
# print('响应信息', type(resp.text))
# print('响应信息字典', type(resp.json()))
# print('响应信息字典', resp.json()['status'])
# print('响应信息', resp.text)
# print('响应cookies', resp.cookies)
# print('响应headers', resp.headers)
#
# # 充值
# resp = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/recharge', data=data, cookies=resp.cookies)
# print(resp.text)
# from common.do_excel import DoExcel
#
# do_excel = DoExcel("..//datas//cases.xlsx")


data = '{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'


