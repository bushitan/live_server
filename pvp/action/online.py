# -*- coding: utf-8 -*-
from lite.query.user import *
from pvp.query.background import *
from pvp.query.stage import *
from pvp.query.stage_tag import *
from pvp.query.pvp_member import *


class ActionOnline():
	pvpRoomDict = {}
	key = 0
	def __init__(self):
		self.user = QueryUser()
		self.stage = QueryStage()
		self.stage_tag = QueryStageTag()
		self.background = QueryBackground()
		self.pvp_member = QueryPVPMember()

	def CheckMember(self,session):
		return self.pvp_member.IsExists(user__session = session)
	# 用户获取自己的图片
	def GetListBackgroundBySelf(self,session):
		return self.background.Filter(user__session = session)
	def GetListStage(self):
		_tag_list = self.stage_tag.FilterQuery()
		_matrix = []
		for tag in _tag_list:
			_stage_list = self.stage.Filter(tag_id = tag.id)
			_matrix.append({
				"name":tag.name,
				"description":tag.description,
				"list":_stage_list,
			})
		return _matrix
	def CreatePvpRoom(self,session):
		_user = self.user.Get(session = session)
		_uid = str(_user['user_id'])
		_room_config = {
			"teacher_pusher":"http://teacher_pusher" + _uid,
			"teacher_player":"http://teacher_player" + _uid,
			"student_pusher":"http://student_pusher" + _uid,
			"student_player":"http://student_player" + _uid,
		}
		# self.key = self.key + 1
		self.pvpRoomDict[_uid] = _room_config
		# print self.pvpRoomDict
		print self.pvpRoomDict
		return _uid , _room_config
	def JoinPvpRoom(self,key):
		if self.pvpRoomDict.has_key(key) is True:
			# _room_config = self.pvpRoomDict.pop(key)
			_room_config = self.pvpRoomDict[key]
			print  True,_room_config
			print self.pvpRoomDict

			return True,_room_config
		else:
			print  False,u"房间不存在"
			print self.pvpRoomDict
			return False,u"房间不存在"
if __name__ == "__main__":
	import os,django
	django.setup()
	a = ActionOnline()
	a.CreatePvpRoom("9GEUS5/0FMeW2hnRpBOBzg==")
	a.CreatePvpRoom("9GEUS5/0FMeW2hnRpBOBzg==")
	a.JoinPvpRoom("1")
	a.JoinPvpRoom("2")
	a.JoinPvpRoom("1")
	# a.pvpRoomDict