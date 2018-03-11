# -*- coding: utf-8 -*-
from lib.query_base import *
from room.models import *
class QueryPusherUser(QueryBase):
	def __init__(self):
		super(QueryPusherUser,self).__init__(PusherUser)

	#用于封面展示的数据
	def _PackDict(self,obj):
		return {
			"room_id":obj.room_id,
			"user_id":obj.user_id,
		}
if __name__ == "__main__":
	import os,django
	django.setup()
	q = QueryPusherUser()
	print q.IsExists(room_id='1',user__session = "9GEUS5/0FMeW2hnRpBOBzg=="	)
	# print query_user.GetDict(session = "12321321")