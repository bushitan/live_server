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
			"stage_background_image":obj.background_image.url if obj.background_image is not None else "",
			"stage_background_audio":obj.background_audio.url if obj.background_audio is not None else "",
			"stage_cover":obj.cover_image.url if obj.cover_image is not None else "",
			"stage_audio":obj.audio_image.url if obj.audio_image is not None else "",
			"stage_orientation":obj.orientation,
			"stage_width":obj.width,
			"stage_height":obj.height,

			"pusher_image":obj.pusher_image.url if obj.pusher_image is not None else "",
			"pusher_x":obj.pusher_x,
			"pusher_y":obj.pusher_y,
			"pusher_width":obj.pusher_width,
			"pusher_height":obj.pusher_height,

			"player_image":obj.player_image.url if obj.player_image is not None else "",
			"player_x":obj.player_x,
			"player_y":obj.player_y,
			"player_width":obj.player_width,
			"player_height":obj.player_height,


			# "create_time":obj.create_time.strftime("%Y-%m-%d"),
		}
if __name__ == "__main__":
	# import os,django
	# django.setup()
	q = QueryStage()
	print q.Filter(	)
	# print query_user.GetDict(session = "12321321")