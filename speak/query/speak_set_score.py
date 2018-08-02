# -*- coding: utf-8 -*-
from lib.query_base import *
from speak.models import *
from lib.util import *

from django.db.models import Q
from django.db.models import Sum
from django.db.models import Count


class QuerySpeakSetScore(QueryBase):
	def __init__(self):
		super(QuerySpeakSetScore,self).__init__(SpeakSetScore)

	def GetScore(self,action):
		if self.IsExists(action = action) is True:
			return self.GetQuery(action = action).score
		else:
			return 0
	#用于封面展示的数据
	def _PackDict(self,obj):
		return {
			"id":obj.id,
			"action":obj.action,
			"score":obj.score,
		}
if __name__ == "__main__":
	import django
	django.setup()
	q = QuerySpeakSetScore()
	print q.GetQuery(action = SPEAK_ACTION_SIGN_IN).score
	# print q.Remain(2)
	# print query.query
	# print q.Filter(theme_id=1
	# 	# session = "12321321"
	# )
	# print q.Filter(theme_id=1)
	# print query_user.GetDict(session = "12321321")


















