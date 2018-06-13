# -*- coding:utf-8 -*-
'''12306的模拟登陆
特点：
先访问验证码图片模块，头部信息的referer，产生cookie
下载图片 选择合适的位置
将位置信息等写入data中
接着再访问验证码校验模块
访问账号密码登陆模块，登陆
'''
import urllib2
import urllib
import ssl
import cookielib
import user_name_ps
import json

# 使用cookie
c = cookielib.LWPCookieJar()
cookie = urllib2.HTTPCookieProcessor(c)
opener = urllib2.build_opener(cookie)
# 12306没有安全证书，sll不进行检验
ssl._create_default_https_context = ssl._create_unverified_context

# 先访问12306图片 并且下载下来
req = urllib2.Request('https://kyfw.12306.cn/passport/captcha/captcha-image'
                      '?login_site=E&module=login&rand=sjrand&0.6987933702923887')
req.add_header('User-Agent',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
               ' (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
req.add_header('Referer', 'https://kyfw.12306.cn/otn/login/init')

# 下载图片到当前文件夹
codeimg = opener.open(req).read()
with open('code.png', 'wb') as fp:
    fp.write(codeimg)
# 输入图片的位置信息
code = raw_input('>>>')
# 携带cookie信息，再进行12306图片校验
req = urllib2.Request('https://kyfw.12306.cn/passport/captcha/captcha-check')
data = {
    'answer': code,
    'login_site': 'E',
    'rand': 'sjrand'
}
data = urllib.urlencode(data)
req.add_header('User-Agent',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
               ' (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
req.add_header('Referer', 'https://kyfw.12306.cn/otn/login/init')
html = opener.open(req, data=data).read()
result = json.loads(html)
if result['result_code'] == '4':
    print '校验成功'
else:
    print '校验失败'

# 使用账号密码进行校验
req = urllib2.Request('https://kyfw.12306.cn/passport/web/login')
req.add_header('User-Agent',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
               ' (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
req.add_header('Referer', 'https://kyfw.12306.cn/otn/login/init')
data = {
    'username': user_name_ps.name,
    'password': user_name_ps.password,
    'appid': 'otn'
}
data = urllib.urlencode(data)
html = opener.open(req, data=data).read()
result = json.loads(html)
if result['result_code'] == 0:
    print '登陆成功'
else:
    print '登陆失败'