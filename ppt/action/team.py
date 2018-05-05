# -*- coding: utf-8 -*-
from lite.query.user import *
from lite.query.app import *
# from ppt.query.ppt_tag import *
from ppt.query.ppt_team import *
from ppt.query.ppt_team_user import *
from ppt.query.ppt_roster import *
from ppt.query.ppt_roster_tag import *

class ActionTeam():
	def __init__(self):
		self.app = QueryApp()
		self.user = QueryUser()
		# self.ppt_file = QueryPPTFile()
		self.ppt_team = QueryPPTTeam()
		self.ppt_team_user = QueryPPTTeamUser()

		# 通讯录
		self.ppt_roster = QueryPPTRoster()
		self.ppt_roster_tag = QueryPPTRosterTag()

		self.app = self.app.GetQuery(id = 5)

	# 检测用户是否在团队
	def CheckBySession(self,session):
		_check_team = self.ppt_team_user.IsExists(member_user__session = session)
		if _check_team is False:
			return _check_team
		else:
			_team_user = self.ppt_team_user.Get(member_user__session = session)
			return _team_user['team_id']
	# 退出
	def Quit(self,session):
		if self.ppt_team_user.IsExists(member_user__session = session) is False:
			return  False
		else:
			_query = self.ppt_team_user.GetQuery(member_user__session = session)
			return self.ppt_team_user.Delete(_query )
	# 加入团队
	def JoinBySession(self,session,team_id):
		_member_user = self.user.GetQuery(session = session)
		_team = self.ppt_team.GetQuery(id = team_id)
		_team_user = self.ppt_team_user.Add(
			member_user = _member_user ,
			team = _team,
			app= self.app
		)
		return _team_user["team_id"]

	def GetRosterTag(self,team_id):
		return self.ppt_roster_tag.Filter(team_id = team_id)
	def GetRoster(self,roster_tag_id):
		return self.ppt_roster.Filter(roster_tag = roster_tag_id)





	# 创建团队
	def CreateBySession(self,session):
		_create_user = self.user.GetQuery(session = session)
		return self.ppt_team.Add(
			create_user = _create_user ,
			app= self.app
		)

	# 解散
	def Delete(self,team_id):
		return self.ppt_team_user.Delete(team_id = team_id)

	# 改名字
	def UpdateName(self,team_id,team_name):
		_query = self.ppt_team.FilterQuery(id = team_id)
		return self.ppt_team.Update(_query,name=team_name )

	# 查询所属团队信息
	def GetInfoBySession(self,session):
		dict_team = False
		is_leader = False
		if self.ppt_team_user.IsExists(member_user__session = session) is True:
			team = self.ppt_team_user.Get(member_user__session = session)
			# 查Team的用户信息
			team_id = team["team_id"]
			dict_team = self.ppt_team.Get(id = team_id)
			# 检查是否群主
			_create_user = self.user.Get(session = session)
			if  _create_user["user_id"] == dict_team["create_user_id"]:
				is_leader = True
		return {
			"is_leader":is_leader,
			"dict_team":dict_team,
		}
if __name__ == "__main__":
	import django
	django.setup()
	a = ActionTeam()
	# print a.CheckBySession('AeSca0HgU8O/5sGzT+nmsA==',)
	print a.Quit('AeSca0HgU8O/5sGzT+nmsA==',)

	# print a.GetInfoBySession('VwxAkbm7G8dvhgrVuq2A4w==',)
