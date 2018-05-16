# -*- coding: utf-8 -*-
from lite.query.user import *
from lite.query.app import *
from ppt.query.ppt_tag import *
from ppt.query.ppt_file import *
from ppt.src.qi_niu import *
import time
import hashlib


ROOM_DICT = {}
class ActionRoom():
	def __init__(self):
		self.user = QueryUser()
		pass


	def LiveUrl(self,txTime,style,user_name,role):
		key = "87416c13d3f5cf4590615bb1f0138715"
		stream_id = "15628_" + user_name + "_" + role

		#MD5 加密
		m2 = hashlib.md5()
		m2.update(key + stream_id + txTime)
		txSecret = m2.hexdigest()

		# txSecret = MD5.hex_md5(key + stream_id + txTime)
		base = "rtmp://15628.live" + style + ".myqcloud.com/live/" + stream_id
		secret = "?txSecret=" + txSecret + "&txTime=" + txTime
		return base + secret

	# 获取房主名字
	def getHostName(self,session):
		_user = self.user.Get(session = session)
		host_name = "live_ppt_user_" + str(_user['user_id'])
		return host_name

	def Add(self,session):
		teacherName = self.getHostName(session)
		#直播时长
		dtime = datetime.datetime.now()+datetime.timedelta(minutes=20)
		unix = int(time.mktime(dtime.timetuple()))
		txTime = format(unix, 'x')

		liveConfig = {
			'teacherName': teacherName,
			'teacherPusher': self.LiveUrl(txTime, "push", teacherName,"teacher"),
			'teacherPlayer': self.LiveUrl(txTime, "play", teacherName, "teacher"),
			'studentPusher': self.LiveUrl(txTime, "push", teacherName, "student"),
			'studentPlayer': self.LiveUrl(txTime, "play", teacherName, "student"),
		}
		ROOM_DICT[teacherName] = liveConfig
		print ROOM_DICT
		return liveConfig

	def Delete(self,session):
		_host_name = self.getHostName(session)
		if ROOM_DICT.has_key(_host_name):
			ROOM_DICT.pop(_host_name)
		return True
	def Check(self,host_name):
		if ROOM_DICT.has_key(host_name):
			return ROOM_DICT.pop(host_name)
		else:
			return False

if __name__ == "__main__":
	import os,django
	django.setup()
	a = ActionRoom()
	print a.UploadGetToken("iRPP5reRQanRZN5sbbNFAg==",1,'jpg')

	# print a.GetListByTag(6)

	# print a.GetListByTeam(team_id=1)
	# a.pvpRoomDict