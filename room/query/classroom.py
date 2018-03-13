# -*- coding: utf-8 -*-
from lib.query_base import *
from room.models import *
class QueryClassroom(QueryBase):
	def __init__(self):
		super(QueryClassroom,self).__init__(Classroom)

	#用于封面展示的数据
	def _PackDict(self,obj):
		return {
			"classroom_id":obj.id,
			"app_id":obj.app_id,
			"teacher_id":obj.teacher_id,
			"teacher_pusher_url":obj.teacher_pusher,
			"teacher_player_url":obj.teacher_player,
			"student_pusher_url":obj.student_pusher,
			"student_player_url":obj.student_player,
			"key":obj.key,
			"create_time":obj.create_time.strftime("%Y-%m-%d"),
		}
if __name__ == "__main__":
	# import os,django
	# django.setup()
	q = QueryClassroom()
	print q.Filter(	)
	# print query_user.GetDict(session = "12321321")