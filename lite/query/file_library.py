# -*- coding: utf-8 -*-
from lib.query_base import *
from lite.models import *
class QueryFileLibrary(QueryBase):
	def __init__(self):
		super(QueryFileLibrary,self).__init__(FileLibrary)

	def _PackDict(self,query_get):
		_dict = {
			'user_id':query_get.user_id,
			'name':query_get.name,
			'url':query_get.url,
			'style':query_get.style,
		}
		return _dict

if __name__ == "__main__":
	import os,django
	django.setup()
	query_user = QueryFileLibrary()
	print query_user.Filter(
		user__session = "9GEUS5/0FMeW2hnRpBOBzg=="
	)
	# print query_user.GetDict(session = "12321321")