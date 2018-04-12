# -*- coding: utf-8 -*-
from lib.query_base import *
from room.models import *
class QueryRoom(QueryBase):
	def __init__(self):
		super(QueryRoom,self).__init__(Room)

	#用于封面展示的数据
	def _PackDict(self,obj):
		return {
			"room_id":obj.id,
			"status":obj.status,
			# "pusher_url":obj.pusher,
			# "player_url":obj.player,
			"style":obj.style,
			"cover_url":obj.cover.url if obj.cover is not None else "",
			"name":obj.name,
			"title":obj.title,
			"description":obj.description,
			"content_url":obj.content.url if obj.content is not None else "",
			"serial":obj.serial, # 七牛云自动缩略图
			"create_time":obj.create_time.strftime("%Y-%m-%d"),
		}
if __name__ == "__main__":
	# import os,django
	# django.setup()
	q = QueryRoom()
	print q.Filter(	)
	# print query_user.GetDict(session = "12321321")