# -*- coding: utf-8 -*-
from lib.query_base import *
from speak.models import *
class QuerySpeakBonus(QueryBase):
	def __init__(self):
		super(QuerySpeakBonus,self).__init__(SpeakBonus)

	#用于封面展示的数据
	def _PackDict(self,obj):
		return {
			"id":obj.id,
			"self_id":obj.user_id,
			"self_logo":obj.self_logo,
			"other_id":obj.other_id,
			"other_logo":obj.other_logo,
			"theme_id":obj.theme_id,
			"theme_title":obj.theme.title,
			"action":obj.action,
			"score":obj.score,
			"issue_time":obj.issue_time.strftime("%Y-%m-%d"),
			"create_time":obj.create_time.strftime("%Y-%m-%d"),
		}
if __name__ == "__main__":
	import django
	django.setup()
	q = QuerySpeakBonus()
	print q.FilterQuery()
	# print q.Filter(theme_id=1
	# 	# session = "12321321"
	# )
	# print q.Filter(theme_id=1)
	# print query_user.GetDict(session = "12321321")