# -*- coding: utf-8 -*-
from lite.query.user import *
from pvp.query.background import *
from pvp.query.stage import *


class ActionOnline():
	pvpRoomDict = {}
	key = 0
	def __init__(self):
		self.user = QueryUser()
		self.stage = QueryStage()
		self.background = QueryBackground()

	# 用户获取自己的图片
	def GetListBackgroundBySelf(self,session):
		return self.background.Filter(user__session = session)
	def GetListStage(self):
		return self.stage.Filter()
	def CreatePvpRoom(self,session):
		_user = self.user.Get(session = session)
		# _user['user_id']
		_room_config = {
			"teacher_pusher":"1",
			"teacher_player":"2",
			"student_pusher":"3",
			"student_player":"4",
		}
		self.key = self.key + 1
		self.pvpRoomDict[str(self.key)] = _room_config
		print self.pvpRoomDict
		return self.key , _room_config
	def JoinPvpRoom(self,key):
		if self.pvpRoomDict.has_key(key) is True:
			_room_config = self.pvpRoomDict.pop(key)
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