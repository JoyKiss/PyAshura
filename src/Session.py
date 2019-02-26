import requests
s = requests.session()
data = {'email':'958685878@qq.com','password':'958685878***'}
s.post('http://yun.itheima.com/course/1.html',data)

print s.html
