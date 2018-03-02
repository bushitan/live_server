# -*- coding: utf-8 -*-
from lib.query_base import *
from lite.models import *
from django.db.models import Q
class QueryUser(QueryBase):
	def __init__(self):
		super(QueryUser,self).__init__(User)

	def _PackDict(self,query_get):
		_dict = {
			'session':query_get.session,
			'logo':query_get.logo,
			'nick_name':query_get.nick_name,
		}
		return _dict

if __name__ == "__main__":
	query_user = QueryUser()
	print query_user.Filter(
		session = "12321321"
	)
	# print query_user.GetDict(session = "12321321")