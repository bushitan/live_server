# -*- coding: utf-8 -*-
from lib.query_base import *
from pvp.models import *
class QueryStage(QueryBase):
	def __init__(self):
		super(QueryStage,self).__init__(Stage)

	#用于封面展示的数据
	def _PackDict(self,obj):
		return {
			"stage_id":obj.id,
			# "im_num":obj.im_num,
			# "pusher_url":obj.pusher,
			# "player_url":obj.player,
			"config":obj.config,
			"background_url":obj.background.url if obj.background is not None else "",
			"create_time":obj.create_time.strftime("%Y-%m-%d"),
		}
if __name__ == "__main__":
	# import os,django
	# django.setup()
	q = QueryStage()
	print q.Filter(	)
	# print query_user.GetDict(session = "12321321")