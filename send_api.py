# -*-coding:utf-8-*-
def send_sms(tel, seat, train, go_date, arrival_time):
    req = top.api.AlibabaAliqinFcSmsNumSendRequest()
    req.set_app_info(top.appinfo(key_date.sms_appkey, key_date.sms_secret))
    req.extend = ""
    req.sms_type = "normal"
    req.sms_free_sign_name = "Python社区"
    req.sms_param = '{"seat":"%s","train":"%s","go_date":"%s","arrival_time":"%s"}'
    req.rec_num = tel
    req.sms_template_code="SMS_69080608"
    try:
        resp=req.getResponse()
        return resp
    except Exception,e:
        return e
if __name__='__main__':
    print send_sms('18173119351','K557')


