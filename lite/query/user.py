# -*- coding: utf-8 -*-
from lib.query_base import *
from lite.models import *
from django.db.models import Q
class QueryUser(QueryBase):
	def __init__(self):
		super(QueryUser,self).__init__(User)

	def _PackDict(self,query_get):
		_dict = {
			'user_id':query_get.id,
			'session':query_get.session,
			'avatar_url':query_get.avatar_url,
			'nick_name':query_get.nick_name,
			'is_teacher':query_get.is_teacher,
		}
		return _dict

if __name__ == "__main__":
	query_user = QueryUser()
	print query_user.Filter(
		session = "12321321"
	)
	# print query_user.GetDict(session = "12321321")