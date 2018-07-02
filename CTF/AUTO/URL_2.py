#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request, urllib.parse, urllib.error
import http.cookiejar

global postdata, headers, cookie, handler, opener, request
LOGIN_URL = 'https://github.com/'
values = {"login":"cndavy",
          "password":"",
        }
def putFlag(flag):

    # 创建一个MozillaCookieJar对象
    cookie = http.cookiejar.MozillaCookieJar()
    # 从文件中的读取cookie内容到变量
    cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
    get_url = 'http://www.baidu.com'  # 利用cookie请求訪问还有一个网址
    # 利用获取到的cookie创建一个opener
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    values = {
        "flag": flag}
    postdata = urllib.parse.urlencode(values).encode()
    request = urllib.request.Request(get_url, postdata, headers)
    get_response = opener.open(request)
    print(get_response.read().decode())

def login(LOGIN_URL  ,  values  ):

    postdata = urllib.parse.urlencode(values).encode()
    user_agent = r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}
    cookie_filename = 'cookie.txt'
    cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    request = urllib.request.Request(LOGIN_URL, postdata, headers)
    try:
        response = opener.open(request)
        page = response.read().decode()
        # print(page)
    except urllib.error.URLError as e:
        print(e.errno, ':', e.reason)
    cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
    print(cookie)
    for item in cookie:
        print('Name = ' + item.name)
        print('Value = ' + item.value)

login(LOGIN_URL,values)


def getFlagFrom(ip):



    return "flag:{%s}"%ip
    pass


for i in range(255):
    ip='172.168.1.%s'%i
    if (i!=12): # my ip
        flag=getFlagFrom(ip)
        putFlag(flag)

