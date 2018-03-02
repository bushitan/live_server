#coding:utf-8
import json
# 回复信息
NET_ERROR = u'网络连接失败'
LOGGER_METHO = u'Method:'

from django.http import HttpResponse
import json
import logging
logger = logging.getLogger("django") # 为loggers中定义的名称


	# return LOGGER_METHO + class_name + "," + str(error)
def MESSAGE_LOGGER( func):
	def MESSAGE_LOGGER(class_name ,error):
		print MESSAGE_LOGGER, class_name ,error
		logger.error( LOGGER_METHO + str(class_name) + "," + str(error) )
		func(class_name ,error)
	return MESSAGE_LOGGER

def MESSAGE_RESPONSE_SUCCESS( message_dict ):
	_dict = message_dict
	_dict["status"] = "true"
	# return json.dump(_dict)
	return HttpResponse( json.dumps( _dict ),content_type="application/json" )

def MESSAGE_RESPONSE_FAIL( message_dict ):
	_dict = message_dict
	_dict["status"] = 'false'
	return HttpResponse(json.dumps( _dict ),content_type="application/json")


def MESSAGE_RESPONSE_LOGIN_OUT(  ):
	_dict = {
		"status":"false",
		"msg":u"用户不存在,请重新登录"
	}
	return HttpResponse(json.dumps( _dict ),content_type="application/json")

# @MESSAGE_LOGGER
def MESSAGE_RESPONSE_NET_ERROR ( class_name ,error):
	logger.error( LOGGER_METHO + class_name + "," + str(error) )
	print 'MESSAGE_RESPONSE_NET_ERROR'
	_dict = {
		"status" : 'false',
		"msg":NET_ERROR
	}
	r = HttpResponse(json.dumps( _dict ),content_type="application/json")
	print r
	return r