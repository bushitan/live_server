# -*- coding: utf-8 -*-
from room.models import *
from lib.query_base import *
class QueryMessage(QueryBase):
	def __init__(self):
		super(QueryMessage,self).__init__(Message)


	#获取文章详细内容
	def _PackDict(self,obj):
		return {
			"id":obj.id,
			"nick_name":obj.user.nick_name if obj.user is not None else "",
			"avatar_url":obj.user.avatar_url if obj.user is not None else "",
			"is_teacher":obj.user.is_teacher if obj.user is not None else "",
			"style":obj.style,
			"content":obj.text,
			"image_url":obj.image,
			"audio_url":obj.audio,
		}

if __name__ == "__main__":
	q = QueryMessage()
	print q.Filter()