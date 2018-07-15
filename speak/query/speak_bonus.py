# -*- coding: utf-8 -*-
from lib.query_base import *
from speak.models import *

from django.db.models import Q
from django.db.models import Sum
from django.db.models import Count


class QuerySpeakBonus(QueryBase):
	def __init__(self):
		super(QuerySpeakBonus,self).__init__(SpeakBonus)

	def Remain(self,self_id):
		#打卡的统计
		_own = SpeakBonus.objects.filter(
			Q(user_self_id = self_id),
			Q(action=SPEAK_ACTION_CHECK)| Q(action=SPEAK_ACTION_SHARE)
		).values('user_self').annotate(sum_score = Sum('score'))
		if len(_own) > 0:
			_own_bonus = _own[0]["sum_score"]
		else :
			_own_bonus = 0

		#花费的统计
		_cost = SpeakBonus.objects.filter(
			Q(action=SPEAK_ACTION_COST)
		).values('user_self').annotate(sum_score = Sum('score'))
		if len(_own) > 0:
			_cost_bonus = _cost[0]["sum_score"]
		else :
			_cost_bonus = 0
		return _own_bonus - _cost_bonus


	#用于封面展示的数据
	def _PackDict(self,obj):
		return {
			"id":obj.id,
			"self_id":obj.user_self_id,
			"self_logo":obj.user_self.avatar_url if obj.user_self is not None else "",
			"other_id":obj.user_other_id,
			"other_logo":obj.user_other.avatar_url if obj.user_other is not None else "",
			"theme_id":obj.theme_id,
			"theme_title":obj.theme.title if obj.theme is not None else "",
			"action":obj.action,
			"score":obj.score,
			"issue_time":obj.issue_time.strftime("%Y-%m-%d"),
			"create_time":obj.create_time.strftime("%Y-%m-%d"),
		}
if __name__ == "__main__":
	import django
	django.setup()
	q = QuerySpeakBonus()
	print q.Remain(2)
	# print query.query
	# print q.Filter(theme_id=1
	# 	# session = "12321321"
	# )
	# print q.Filter(theme_id=1)
	# print query_user.GetDict(session = "12321321")


















