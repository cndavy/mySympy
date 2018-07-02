

from urllib import request
from urllib import parse
from urllib.request import urlopen

from http import cookiejar
values = {'username': '962457839@qq.com', 'password': 'XXXX'}
headers = {

}
data = parse.urlencode(values).encode('utf-8')  # 提交类型不能为str，需要为byte类型
url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'

cookie = cookiejar.CookieJar()
# 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
handler = request.HTTPCookieProcessor(cookie)
# 通过CookieHandler创建opener
opener = request.build_opener(handler)
rsp=opener.open(url, data )
#r = request.Request(url, data , headers=headers)
#response = urlopen(r)
print(rsp.read().decode())
for item in cookie:
    print(item.name,item.value)