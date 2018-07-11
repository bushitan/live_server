# -*- coding: utf-8 -*-
from lib.query_base import *
from speak.models import *
class QuerySpeakTheme(QueryBase):
	def __init__(self):
		super(QuerySpeakTheme,self).__init__(SpeakTheme)

	#获取文章详细内容
	def _PackDict(self,obj):
		return  {
			"id":obj.id,
			"title":obj.title,
			"content":obj.content,
			#直播间ID
			"voice_url":obj.voice.url if obj.voice is not None else "",
			"issue_time":obj.issue_time.strftime("%Y-%m-%d"),
			"create_time":obj.create_time.strftime("%Y-%m-%d"),
		}


if __name__ == "__main__":
	q = QuerySpeakTheme()
	print q.Filter(
		# session = "12321321"
	)
	# print query_user.GetDict(session = "12321321")