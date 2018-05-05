# -*- coding: utf-8 -*-
from lite.query.user import *
from lite.query.app import *
from ppt.query.ppt_tag import *
from ppt.query.ppt_team import *


class ActionTag():
	def __init__(self):
		self.app = QueryApp()
		self.user = QueryUser()
		self.team = QueryPPTTeam()
		# self.ppt_file = QueryPPTFile()
		self.ppt_tag = QueryPPTTag()

		self.app = self.app.GetQuery(id = 6)
	# 查询标签
	def GetListBySession(self,session):
		return self.ppt_tag.Filter(user__session = session)

	def GetListByTeam(self,team_id):
		return self.ppt_tag.Filter(team_id = team_id)

	# 增加标签
	def AddBySession(self,session,tag_name):
		_user = self.user.GetQuery(session = session)
		return self.ppt_tag.Add(user = _user ,name=tag_name ,app= self.app)

	def AddByTeam(self,team_id ,tag_name):
		_team = self.team.GetQuery(id = team_id)
		return self.ppt_tag.Add(team = _team ,name=tag_name ,app= self.app)

	# 删除标签
	def Delete(self,tag_id):
		return self.ppt_tag.Delete(id=tag_id )
	# 更改
	def Update(self,tag_id,tag_name):
		_query = self.ppt_tag.FilterQuery(id=tag_id )
		return self.ppt_tag.Update(_query,name=tag_name )



if __name__ == "__main__":
	import os,django
	django.setup()
	a = ActionTag()
	# print a.GetListByTeam(team_id=1)
	# print a.GetListBySession('AeSca0HgU8O/5sGzT+nmsA==',)
	print a.AddBySession('AeSca0HgU8O/5sGzT+nmsA==',"aa")
	# a.pvpRoomDict