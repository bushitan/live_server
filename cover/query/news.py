# -*- coding: utf-8 -*-
from lib.query_base import *
from cover.models import *
class QueryNews(QueryBase):
	def __init__(self):
		super(QueryNews,self).__init__(News)

	#用于封面展示的数据
	def _PackDict(self,obj):
		return {
			"news_id":obj.id,
			"article_id":obj.article_id,
			"tag_id":obj.tag_id,
			"cover_url":obj.cover_image.url if obj.tag is not None else "",
			"title":obj.title,
			"summary":obj.summary,
			"des":obj.des,
			"footer":obj.footer, # 七牛云自动缩略图
			"issue_time":obj.issue_time.strftime("%Y-%m-%d"),
			"create_time":obj.create_time.strftime("%Y-%m-%d"),
		}
if __name__ == "__main__":
	q = QueryNews()
	print q.Filter(tag_id=1
		# session = "12321321"
	)
	# print query_user.GetDict(session = "12321321")