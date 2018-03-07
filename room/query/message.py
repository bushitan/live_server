# -*- coding: utf-8 -*-
from lib.query_base import *
from room.models import *
class QueryMessage(QueryBase):
	def __init__(self):
		super(QueryMessage,self).__init__(Message)


	#获取文章详细内容
	def _PackDict(self,obj):
		return {
			"nick_name":obj.user.nick_name if obj.user is not None else "",
			"logo":obj.user.logo if obj.user is not None else "",
			"im_num":obj.room.im_num if obj.room is not None else "",
			"style":obj.style,
			"text":obj.text,
			"image_url":obj.image.url if obj.image is not None else "",
			"audio_url":obj.audio.url if obj.audio is not None else "",
		}

if __name__ == "__main__":
	q = QueryMessage()
	print q.Filter()