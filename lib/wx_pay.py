# -*- coding: utf-8 -*-



import json,urllib2,urllib

import hashlib
import datetime,time
import math
import random

import xml.sax
import xml.sax.handler
#XML解析类
class XMLHandler(xml.sax.handler.ContentHandler):
    timeStamp = ''
    nonceStr =''
    package = ''
    paySign = ''
    def __init__(self):
        self.buffer = ""
        self.mapping = {}

    def startElement(self, name, attributes):
        self.buffer = ""

    def characters(self, data):
        self.buffer += data

    def endElement(self, name):
        self.mapping[name] = self.buffer

    def getDict(self):
        return self.mapping
class WXPay():
    def __init__(self,APP_ID, APP_SECRET , MACH_ID, MACH_KEY,open_id,order_id,fee,callback_url):
        #一致的商铺信息
        self.APP_ID = APP_ID
        AppId = APP_ID
        app_secret = APP_SECRET
        MachId = MACH_ID
        # OpenId = "oI1IJ0cyiH_hLqVdc5ISKlfT6Lbc"
        OpenId = open_id
        # key = "283fc3d9d4b8ba3b58601145466d4417"
        # key = "gxhxweihuaxuntong077155533360000"
        key = MACH_KEY

        # NotifUrl = "https://www.lwdweb.top/Pay/PayNotify"
        # NotifUrl = "https://xcx.308308.com/test/api/order/wx_notift/"
        # NotifUrl = "https://xcx.308308.com/huaxun/api/order/wx_notify/"
        NotifUrl = callback_url

        # orderId = "123asd" #商铺订单号
        orderId = order_id#商铺订单号
        device_info = 'WEB'
        body = 'test_body'

        # total_fee = '1' #支付金额
        total_fee = fee #支付金额

        ip = '113.16.147.89'
        prodId = '1235'

        nonce_str =  self.randomString()
        nonce = nonce_str
        start = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        temp = datetime.datetime.now() + datetime.timedelta(seconds = 900)
        end = str(temp.strftime("%Y%m%d%H%M%S"))

        #签名
        stringA="appid="+AppId+"&body=test&device_info="+device_info+"&mch_id="+MachId+"&nonce_str=" + nonce_str
        stringSignTemp = stringA + "&key="+app_secret  #注：key为商户平台设置的密钥key

        pmStr = "appid=" + AppId + "&body=" + body + "&device_info=WEB&mch_id=" + MachId
        pmStr += "&nonce_str=" + nonce
        pmStr += "&notify_url=" + NotifUrl  #异步通知地址不做了
        pmStr += "&openid=" + OpenId
        pmStr += "&out_trade_no=" + orderId + "&product_id=" + prodId + "&spbill_create_ip=" + ip
        pmStr += "&time_expire=" + end + "&time_start=" + start + "&total_fee=" + total_fee
        pmStr += "&trade_type=JSAPI&key=" + key
        sign = self.md5(pmStr)
        print 'MD5:',sign

        self.data = "<xml>"
        self.data += "<appid>" + AppId + "</appid>"
        self.data += "<body>" + body + "</body>"
        self.data += "<device_info>WEB</device_info>"
        self.data += "<mch_id>" + MachId + "</mch_id>"
        self.data += "<nonce_str>" + nonce + "</nonce_str>"
        self.data += "<notify_url>" + NotifUrl + "</notify_url>"  #不做异步通知地址了
        self.data += "<openid>" + OpenId + "</openid>"
        self.data += "<out_trade_no>" + orderId + "</out_trade_no>"
        self.data += "<product_id>" + prodId + "</product_id>"
        self.data += "<spbill_create_ip>" + ip + "</spbill_create_ip>"
        self.data += "<time_expire>" + end + "</time_expire>"
        self.data += "<time_start>" + start + "</time_start>"
        self.data += "<total_fee>" + total_fee + "</total_fee>"
        self.data += "<trade_type>JSAPI</trade_type>"
        self.data += "<sign>" + sign + "</sign>"
        self.data += "</xml>"


        # self.nonceStr = nonce
        # self.paySign = sign
    def md5(self,str):
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest().upper()

    def randomString (self,):

        chars = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678"    #/****默认去掉了容易混淆的字符oOLl,9gq,Vv,Uu,I1****/
        maxPos = len(chars)
        pwd = ''
        for i in range(0,32) :
            pwd += chars[int((math.floor(random.random() * maxPos)))]
        return pwd

    #获取预支付交易会话标识
    def get_request_payment(self):
        _wx_url = "https://api.mch.weixin.qq.com/pay/unifiedorder"

        # print data
        opener = urllib2.build_opener()
        request = urllib2.Request(
            url = _wx_url,
            headers = {'Content-Type' : 'application/xml','charset':'UTF-8'},
            data = self.data)
        f=opener.open(request)
        # print f.read().decode('utf-8')
        xh = XMLHandler()
        # xml.sax.parseString( f.read().decode('utf-8'), xh)
        xml.sax.parseString( f.read(), xh)
        ret = xh.getDict()
        print ret
        # print ret['err_code_des']
        # print ret['xml']
        # print ret['err_code']
        # print ret['prepay_id']
        # print ret['nonce_str']



        self.timeStamp = str( int(round( time.time() * 1000)) )
        self.package = 'prepay_id=' + ret['prepay_id']
        # self.nonceStr = ret['nonce_str']

        self.nonceStr =  self.randomString()

        pmStr = "appId="+ self.APP_ID +"&nonceStr=" + self.nonceStr + "&package=prepay_id=" + ret['prepay_id'] + "&signType=MD5&timeStamp=" +  self.timeStamp + "&key=283fc3d9d4b8ba3b58601145466d4417"
        self.paySign =  self.md5(pmStr)
        # self.paySign =  paySign
        return {
            'timeStamp':  self.timeStamp,
            'nonceStr':  self.nonceStr,
            'package': self.package,
            'paySign':  self.paySign,
        }

    # WxHttp(data)

if __name__ == "__main__":

    # from api.models.user import *
    # from api.models.order import *
	#
    # import django
    # django.setup()
	#
	#
    # session = 'XFTGjxhyrUpZTGyesAz/Lg=='
    # _user = User.objects.get( session = session)
	#
    # print _user
    # _order = Order.objects.get(user_id = _user.id,is_payment = IS_PAYMENT_FALSE)  #  AddMemberOrder
	#
    # #生成微信wx_out_trade_no
    # # 当前时间 + order_id + 随机数
    # # _order.wx_out_trade_no = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")) + str(_order.id) + str(int(random.random() * 1000))
	#
    # wx_out_trade_no = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")) + str(_order.id) + str(int(random.random() * 1000))
    # print  wx_out_trade_no  #2017091212253017904
    # print _order.payment_fee, type(_order.payment_fee)
	#
    # fee = str( int( _order.payment_fee * 100) )
    # _wx_pay = wx_pay( _user.wx_open_id , wx_out_trade_no , fee)  #  每次重新生成order.wx_out_trade_no
    # _dict  =  _wx_pay.get_request_payment()
    # print _dict

    #TODO
    # 三个步骤
    # 1 server接收小程序的Member or Single ，创建订单    do
    # 2 订单返回小程序，支付    do
    # 3 支付notify_url异步成功通知server，订单生效  TODO
    # 4 小获得成功通知，做成功跳转（看文章 or 返回订单列表 TODO
    dom = '''<table style="border: 1px solid #e0e0e0;" border="1" width="507" cellspacing="0" cellpadding="0" align="center">
    <colgroup > <col width="72" /> <col width="116" /> <col width="102" /> <col span="2" width="72" /> <col width="89" /> <col width="86" /></colgroup>
<tbody >
<tr >
<td colspan="7" width="609" height="45">1．报价均以带票价格为主；标准为：02普级或优级食用酒精；报价地区为原料主产区即酒精价格主导区。如玉米酒精以东北、华北为主；木薯酒精以两广、云南、华东为主；糖蜜酒精以两广、云南为主。</td>
</tr>
<tr>
<td style="border: 1px solid #e0e0e0;" colspan="7" width="609" height="39">2．报价以低端---高端为额度，取中间大趋势价，涨跌50以上报出。如：吉林3600--3750，跌50。表示低端普级玉米酒精价格3600，高端玉米酒精3750，高低端各跌50以后的价格。</td>
</tr>
<tr>
<td style="border: 1px solid #e0e0e0;" colspan="7" width="609" height="19"><strong>10月10<strong>日</strong>玉米酒精报价：</strong></td>
</tr>
</tbody>
</table> '''

    # dom.replace("<td",'<td style="border: 32px solid #e0e0e0;"')
    import re
    _style = 'style="border: 1px solid #e0e0e0;"'
    _str_style = re.compile(_style)
    _str_table = re.compile('<table')
    _str_colgroup = re.compile('<colgroup')
    _str_tr = re.compile('<tr')
    _str_td = re.compile('<td')
    _str_td = re.compile('<td')
    b = _str_style.sub('',dom)
    b = _str_table.sub('<table '+_style,b)
    b = _str_colgroup.sub('<colgroup '+_style,b)
    b = _str_tr.sub('<tr '+_style ,b)
    b = _str_td.sub('<td '+_style,b)
    # dom.replace("table",'1')
    print b

    # import xml.etree.ElementTree as ET
    # xml_file='config.xml'
    # # root=ET.ElementTree(dom).getroot()
    # root=ET.fromstring(dom)
	#
    # root.set('style',"border: 12px solid #e0e0e0;")
    # print root.tag , root.attrib
    # save_xml = ET.tostring(root[0])
    # print save_xml



    # for child in root:
    #     print child.tag, child.attrib
    # #         print s
    # for neighbor in root.iter('tr'):
    #     print neighbor.text , neighbor.attrib

    # for child in root.findall('tr'):
    #     print  child
        # if country.attrib['name'] == 'Singapore':
        #     year = country.find('year')  # 使用Element.find()
        #     print year.text
    # print xml.find("td")
    # print xml
    # xml.find('id').text=1



_wx_request_xnl = '''
<xml>
<appid><![CDATA[wxff79e25befbb413d]]></appid>
<bank_type><![CDATA[CMB_CREDIT]]></bank_type>
<cash_fee><![CDATA[1]]></cash_fee>
<device_info><![CDATA[WEB]]></device_info>
<fee_type><![CDATA[CNY]]></fee_type>
<is_subscribe><![CDATA[Y]]></is_subscribe>
<mch_id><![CDATA[1480337772]]></mch_id>
<nonce_str><![CDATA[b7drxiGAnM76KySNtpTAY3xGfw6kewHG]]></nonce_str>
<openid><![CDATA[oI1IJ0cyiH_hLqVdc5ISKlfT6Lbc]]></openid>
<out_trade_no><![CDATA[20170912132516297]]></out_trade_no>
<result_code><![CDATA[SUCCESS]]></result_code>
<return_code><![CDATA[SUCCESS]]></return_code>
<sign><![CDATA[370DCE954CA77A2EDD5D62E40BFB05B4]]></sign>
<time_end><![CDATA[20170912132835]]></time_end>
<total_fee>1</total_fee>
<trade_type><![CDATA[JSAPI]]></trade_type>
<transaction_id><![CDATA[4010212001201709121665257357]]></transaction_id>
</xml>
'''











