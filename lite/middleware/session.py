# -*- coding: utf-8 -*-
from lib.message import *
from lite.models import *

class SessionMiddleware(object):
	def process_request(self, request):
		#检查是否有session值传入
		#有，则判断是否存在
		_items = request.GET.dict()

		if _items.has_key("session"):  	#session字段存在
			session = request.GET.get('session',"") #获取session
			if  User.objects.filter( session = session).exists() is False: #用户不存在
				if _items.has_key("js_code") is False: # js_code为登陆验证字段，若不存在，返回登陆失败
					return MESSAGE_RESPONSE_LOGIN_OUT()
		return

	def process_response(self, request, response):
		# print "process_response"
		return response

