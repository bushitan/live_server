# -*- coding: utf-8 -*-
from lite.query.user import *
from lite.query.app import *
from ppt.query.ppt_tag import *
from ppt.query.ppt_file import *
from ppt.src.qi_niu import *

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

	def UploadGetToken(self,session,tag_id,_suffix):
		#按照当前时间和用户生成名字
		_user = self.user.Get(session = session)
		_user_id = _user["user_id"]
		_file_name = "team_helper_" + str(_user_id) + "_" + datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + "." + _suffix
		_token,_key,_url = QiNiuGetToken(_file_name)
		_hash = {
			"user_id":_user_id,
			"url":_url,
			"tag_id":tag_id,
		}
		return _token,_key ,_hash

	def UploadComplete(self,user_id,url,tag_id):
		_user = self.user.GetQuery(id = user_id)
		_tag = self.ppt_tag.GetQuery(id = tag_id)
		return self.ppt_file.Add(
			upload_user = _user,
			tag = _tag ,
			url = url
		)


if __name__ == "__main__":
	import os,django
	django.setup()
	a = ActionFile()
	print a.UploadGetToken("iRPP5reRQanRZN5sbbNFAg==",1,'jpg')

	# print a.GetListByTag(6)

	# print a.GetListByTeam(team_id=1)
	# a.pvpRoomDict