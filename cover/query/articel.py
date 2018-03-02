# -*- coding: utf-8 -*-
from lib.query_base import *
from cover.models import *
class QueryArticle(QueryBase):
	def __init__(self):
		super(QueryArticle,self).__init__(Article)

	#用于封面展示的数据
	# def _PackCover(self,query_get):
	# 	_dict = {
	# 		"article_id":query_get.id,
	# 		"role_value":query_get.role.value,
	# 		"cover":query_get.cover_image.url if query_get.tag is not None else "",
	# 		#"cover":query_get.cover,
	# 		"title":query_get.title, # 七牛云自动缩略图
	# 		"issue_time":query_get.issue_time.strftime("%Y-%m-%d"),
	# 		"click_rate":query_get.click_rate,
	# 		"is_banner":query_get.is_banner, #是广告
	# 	}
	# 	return _dict

	#获取文章详细内容
	def _PackDict(self,obj):
		_article_content = {
			"article_id":obj.id,
			"style":obj.style,
			"is_show":obj.is_show,
			#综合
			"click_rate":obj.click_rate,
			"is_top":obj.is_top,

			#封面标题
			#"cover":obj.cover,
			"title":obj.title, # 七牛云自动缩略图
			"subtitle":obj.subtitle,

			#摘要 发布时间
			"summary":obj.summary,
			"source":obj.source,

			#正文
			"content_width":obj.content_width,
			"content":obj.content,

			"issue_time":obj.issue_time.strftime("%Y-%m-%d"),
			"create_time":obj.create_time.strftime("%Y-%m-%d"),

			#音频
			'audio_poster': obj.audio_poster,
			'audio_name': obj.audio_name,
			'audio_author': obj.audio_author,
			'audio_src': obj.audio_src,

			#视频
			'video_src': obj.video_src,

			#小程序跳转
			"address":obj.address,
			"work_date":obj.work_date,
			"phone":obj.phone,
			"introduction":obj.introduction,
		}
		return _article_content


if __name__ == "__main__":
	q = QueryArticle()
	print q.Filter(
		# session = "12321321"
	)
	# print query_user.GetDict(session = "12321321")