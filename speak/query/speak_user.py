# -*- coding: utf-8 -*-
from lib.query_base import *
from speak.models import *
class QuerySpeakUser(QueryBase):
	def __init__(self):
		super(QuerySpeakUser,self).__init__(SpeakUser)

	#用于封面展示的数据
	def _PackDict(self,obj):
		return {
			"id":obj.id,
			"user_id":obj.user_id,
			"user_logo":obj.user.avatar_url,
			"voice_url":obj.voice.url if obj.voice is not None else "",
			"issue_time":obj.issue_time.strftime("%Y-%m-%d"),
			"create_time":obj.create_time.strftime("%Y-%m-%d"),
		}
if __name__ == "__main__":
	import django
	django.setup()
	q = QuerySpeakUser()
	# print q.Filter(theme_id=1
	# 	# session = "12321321"
	# )
	# print q.Filter(theme_id=1)
	# print query_user.GetDict(session = "12321321")