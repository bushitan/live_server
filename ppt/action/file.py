# -*- coding: utf-8 -*-
from lite.query.user import *
from lite.query.app import *
from ppt.query.ppt_tag import *
from ppt.query.ppt_file import *


class ActionFile():
	def __init__(self):
		self.app = QueryApp()
		self.user = QueryUser()
		self.ppt_file = QueryPPTFile()
		self.ppt_tag = QueryPPTTag()

		self.app = self.app.GetQuery(id = 5)
	# 查询
	def GetListByTag(self,tag_id):
		return self.ppt_file.Filter(tag_id = tag_id)

	# 增加
	def AddBySession(self,session,tag_id):
		_user = self.user.GetQuery(session = session)
		_tag = self.ppt_tag.GetQuery(id = tag_id)
		return self.ppt_file.Add(
			upload_user = _user ,
			tag = _tag ,
			app= self.app
		)

	# 删除
	def Delete(self,file_id):
		return self.ppt_file.Delete(id = file_id)

	# 更改
	def Update(self,file_id,tag_id):
		_query = self.ppt_file.FilterQuery(id = file_id)
		return self.ppt_file.Update(_query,tag_id=tag_id )


if __name__ == "__main__":
	import os,django
	django.setup()
	a = ActionFile()
	print a.GetListByTag(6)
	# print a.GetListByTeam(team_id=1)
	# a.pvpRoomDict