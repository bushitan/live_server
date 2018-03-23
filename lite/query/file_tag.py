# -*- coding: utf-8 -*-
from lib.query_base import *
from lite.models import *
class QueryFileTag(QueryBase):
	def __init__(self):
		super(QueryFileTag,self).__init__(FileTag)

	def _PackDict(self,query_get):
		_dict = {
			'file_tag_id':query_get.id,
			# 'user_id':query_get.user_id,
			'name':query_get.name,
		}
		return _dict

if __name__ == "__main__":
	import os,django
	django.setup()
	query_user = QueryFileTag()

	# print query_user.GetDict(session = "12321321")