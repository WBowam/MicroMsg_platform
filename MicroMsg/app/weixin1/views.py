# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse
import hashlib
import xml.etree.ElementTree as ET
###
from django.views.decorators.csrf import csrf_exempt  
import logging
import time
from django.utils.encoding import smart_str, smart_unicode
from app.weixin1.if_item import if_item


logging.basicConfig(filename='develop.log',level=logging.DEBUG)
logging.debug('This message should go to the log file --*%s*',time.ctime())
logging.info('So should this %s',time.ctime())
logging.warning('And this %s %d, too','123',1)

TOKEN="tulpar"
##################################-----level 1

@csrf_exempt
def main(request):  
    #
    #logging.debug('begin --*%s*',time.ctime())
    #line 1
    if request.method == 'GET':  
        #response = HttpResponse(request.GET['echostr'],content_type="text/plain")  
        response = HttpResponse(checkSignature(request),content_type="text/plain")
    #line 2
    elif request.method == 'POST': 
    	logging.debug('begin --*%s*',time.ctime())   
        response = HttpResponse(myresponse(request),content_type="application/xml")
    else:  
        response=None
    return response

##################################-----level 2
#line 1
def checkSignature(request):  
    global TOKEN
    signature = request.GET.get("signature", None)  
    timestamp = request.GET.get("timestamp", None)  
    nonce = request.GET.get("nonce", None)  
    echoStr = request.GET.get("echostr",None)  
  
    token = TOKEN  
    tmpList = [token,timestamp,nonce]  
    tmpList.sort()  
    tmpstr = "%s%s%s" % tuple(tmpList)  
    tmpstr = hashlib.sha1(tmpstr).hexdigest()  
    if tmpstr == signature:  
        return echoStr
    else:  
        return None

#line 2
def myresponse(request):
	msg=userMsg(request)
	text='''<xml>
		<ToUserName><![CDATA[%s]]></ToUserName>
		<FromUserName><![CDATA[%s]]></FromUserName>
		<CreateTime>12345678</CreateTime>
		<MsgType><![CDATA[text]]></MsgType>
		<Content><![CDATA[%s]]></Content>
		</xml>'''
	response=text %(msg['FromUserName'],msg['ToUserName'],if_item(msg))
	return response


def userMsg(request):
    #最终返回信息
    rawStr = smart_str(request.raw_post_data)#工具函数
    formet=ET.fromstring(rawStr)
    msg = {}
    for child in formet:
    	msg[child.tag] = smart_str(child.text)
    logging.debug('msg:%s --*%s*',msg,time.ctime())
    return msg