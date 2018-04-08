# -*- coding: utf-8 -*-
from lite.query.user import *
from ppt.query.ppt_file import *
from ppt.query.ppt_tag import *


class ActionOnline():
	pvpRoomDict = {}
	key = 0
	def __init__(self):
		self.user = QueryUser()
		self.ppt_file = QueryPPTFile()
		self.ppt_tag = QueryPPTTag()

	# 用户获取自己的图片
	def GetListPPTFile(self,session):
		# return self.ppt_file.Filter(user__session = session)
		return self.ppt_file.Filter()

	def GetListPPTTag(self,session):
		return self.ppt_tag.Filter(user__session = session)


if __name__ == "__main__":
	import os,django
	django.setup()
	a = ActionOnline()

	# a.pvpRoomDict