# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.views.generic import  ListView
# Create your views here.

from lib.message import *
import json
import logging
from action.page import *
action_page = ActionPage()




# 移民国家子项
class Main(ListView):
	template_name = 'main.html'
	# context_object_name = 'article_list'
	def get_context_data(self, **kwargs):
		return super(Main, self).get_context_data(**kwargs)

	def get_queryset(self):
		pass









class BaseMixin(object):
	def get_context_data(self, *args, **kwargs):
		# kwargs['nav_list'] = action_page.GetNav(self)
		context = super(BaseMixin, self).get_context_data(**kwargs)
		return context

class YMBase(BaseMixin):
	def get_context_data(self, *args, **kwargs):
		kwargs['nav_list'] = action_page.GetNav(1)
		kwargs['cover_base_url'] = "/live/xx_mgr/ym/cover"
		kwargs['article_base_url'] = "/live/xx_mgr/ym/article"
		context = super(YMBase, self).get_context_data(**kwargs)
		return context



class YMIndexView(YMBase, ListView):
	template_name = 'ym_index.html'
	context_object_name = 'article_list'

	def get_context_data(self, **kwargs):
		kwargs['nav_index'] = 0

		PID_YM_INDEX = 11
		kwargs['one_tag_list'],kwargs['one_article_list'] = action_page.queryMore(PID_YM_INDEX,1)
		kwargs['two_tag'],kwargs['two_article_list'] = action_page.queryOnly(PID_YM_INDEX,2,8)
		kwargs['three_tag'],kwargs['three_article_list'] = action_page.queryOnly(PID_YM_INDEX,3,9)
		kwargs['four_tag'],kwargs['four_article_list'] = action_page.queryOnly(PID_YM_INDEX,4,8)
		kwargs['five_tag'],kwargs['five_article_list'] = action_page.queryOnly(PID_YM_INDEX,5,4)

		# one_tag_list,one_article_list ,two_tag,two_article_list    ,three_tag, three_article_list   ,  four_tag,four_article_list  =  action_page.GetYMIndex()
		#
		#
		# kwargs['one_tag_list'] = one_tag_list
		# kwargs['one_article_list'] = one_article_list
		#
		# kwargs['two_tag'] = two_tag
		# kwargs['two_article_list'] = two_article_list
		#
		# kwargs['three_tag'] = three_tag
		# kwargs['three_article_list'] = three_article_list
		#
		# kwargs['four_tag'] = four_tag
		# kwargs['four_article_list'] = four_article_list


		return super(YMIndexView, self).get_context_data(**kwargs)

	def get_queryset(self):
		pass
		# tag_list = action_page.GetYMIndex()
		# print tag_list
		# return tag_list
		# action_page.
		# article_list = Article.objects.filter(status=0)
		# return article_list

# 移民国家子项
class YMCountryView(YMBase, ListView):
	template_name = 'ym_country.html'
	# context_object_name = 'article_list'
	def get_context_data(self, **kwargs):
		kwargs['nav_index'] = int(self.nav_index)

		# print 10
		# tag,article = action_page.GetYMCountryAd()
		# kwargs['ad'] = article
		kwargs['one_tag'],kwargs['one_article']  = action_page.getOnly(self.pid,1)
		kwargs['two_tag'],kwargs['two_article']  = action_page.getOnly(self.pid,2)
		# print self.pid
		kwargs['three_tag'],kwargs['three_article_list'] = action_page.queryOnly(self.pid,3,8)

		kwargs['four_tag_list'],kwargs['four_article_list'] = action_page.queryMore(self.pid,4)

		print 13
		return super(YMCountryView, self).get_context_data(**kwargs)

	def get_queryset(self):
		pass
		# tag_list = action_page.GetYMIndex()
		# print tag_list
		# return tag_list

	def get(self, request, *args, **kwargs):

		self.nav_index = self.kwargs.get('nav_index')
		self.pid = self.kwargs.get('pid')

		# kwargs['nav_index'] = country_id
		# print country_id
		return super(YMCountryView, self).get(request, *args, **kwargs)


class YMAboutMeView(YMBase, ListView):
	template_name = 'ym_about_me.html'
	# context_object_name = 'article_list'
	def get_context_data(self, **kwargs):
		kwargs['nav_index'] = int(self.nav_index)
		# kwargs['article'] = action_page.GetArticleByID(self.article_id)
		# print kwargs['article']
		return super(YMAboutMeView, self).get_context_data(**kwargs)

	def get_queryset(self):
		pass
		# tag_list = action_page.GetYMIndex()
		# print tag_list
		# return tag_list

	def get(self, request, *args, **kwargs):
		self.nav_index = self.kwargs.get('nav_index')
		self.article_id = self.kwargs.get('article_id')
		return super(YMAboutMeView, self).get(request, *args, **kwargs)



############################文章#########################


class YMCoverView(YMBase, ListView):
	template_name = 'ym_cover.html'
	def get_context_data(self, **kwargs):
		kwargs['nav_index'] = int(self.nav_index)
		kwargs['tag'] ,kwargs['article_list'] = action_page.GetArticleListByTagID(self.tag_id)
		return super(YMCoverView, self).get_context_data(**kwargs)
	def get_queryset(self):
		pass
	def get(self, request, *args, **kwargs):
		self.nav_index = self.kwargs.get('nav_index')
		self.tag_id = self.kwargs.get('tag_id')
		return super(YMCoverView, self).get(request, *args, **kwargs)



class YMArticleView(YMBase, ListView):
	template_name = 'ym_article.html'
	# context_object_name = 'article_list'
	def get_context_data(self, **kwargs):
		kwargs['nav_index'] = int(self.nav_index)
		kwargs['article'] = action_page.GetArticleByID(self.article_id)
		return super(YMArticleView, self).get_context_data(**kwargs)
	def get_queryset(self):
		pass
	def get(self, request, *args, **kwargs):
		self.nav_index = self.kwargs.get('nav_index')
		self.article_id = self.kwargs.get('article_id')
		return super(YMArticleView, self).get(request, *args, **kwargs)





############################留学#########################



class LXBase(BaseMixin):
	def get_context_data(self, *args, **kwargs):

		kwargs['nav_list'] = action_page.GetNav(0)

		kwargs['cover_base_url'] = "/live/xx_mgr/lx/cover"
		kwargs['article_base_url'] = "/live/xx_mgr/lx/article"
		# print  11111, kwargs['nav_list']
		context = super(LXBase, self).get_context_data(**kwargs)
		return context

class LXIndexView(LXBase, ListView):
	template_name = 'lx_index.html'
	context_object_name = 'article_list'

	def get_context_data(self, **kwargs):
		kwargs['nav_index'] = 0
		PID_LX_INDEX = 21
		kwargs['one_tag_list'],kwargs['one_article_list']  = action_page.queryMore(PID_LX_INDEX,1)
		kwargs['two_tag'], kwargs['two_article_list']  =action_page.queryOnly(PID_LX_INDEX,2,8)
		kwargs['three_tag'], kwargs['three_article_list']  = action_page.queryOnly(PID_LX_INDEX,3,9)
		kwargs['four_tag'], kwargs['four_article_list']  = action_page.queryOnly(PID_LX_INDEX,4,8)
		kwargs['five_tag'], kwargs['five_article_list']  = action_page.queryOnly(PID_LX_INDEX,5,4)  #轮播图
		kwargs['six_tag'], kwargs['six_article_list']  = action_page.queryOnly(PID_LX_INDEX,6,4)

		return super(LXIndexView, self).get_context_data(**kwargs)

	def get_queryset(self):
		pass



class LXCountryView(LXBase, ListView):
	template_name = 'lx_country.html'
	context_object_name = 'article_list'

	def get_context_data(self, **kwargs):
		kwargs['nav_index'] =  int(self.nav_index)
		# print kwargs['nav_index']
		kwargs['one_tag'],kwargs['one_article']  = action_page.getOnly(self.pid,1)
		# print kwargs['one_article']
		kwargs['two_tag'], kwargs['two_article']  = action_page.getOnly(self.pid,2)
		kwargs['three_tag'], kwargs['three_article']  = action_page.getOnly(self.pid,3)

		kwargs['four_tag_list'], kwargs['four_article_list']  = action_page.queryMore(self.pid,4)
		kwargs['five_tag_list'], kwargs['five_article_list']  = action_page.queryMore(self.pid,5)
		kwargs['six_tag_list'], kwargs['six_article_list']  = action_page.queryMore(self.pid,6)

		return super(LXCountryView, self).get_context_data(**kwargs)

	def get_queryset(self):
		pass
	def get(self, request, *args, **kwargs):
		self.nav_index = self.kwargs.get('nav_index')
		self.pid = self.kwargs.get('pid')
		return super(LXCountryView, self).get(request, *args, **kwargs)



class LXStudyView(LXBase, ListView):
	template_name = 'lx_success.html'
	context_object_name = 'article_list'

	def get_context_data(self, **kwargs):
		kwargs['nav_index'] = 6

		kwargs['tag'],kwargs['article_list']  = action_page.queryOnly(None,27,50)

		return super(LXStudyView, self).get_context_data(**kwargs)

	def get_queryset(self):
		self.nav_index = self.kwargs.get('nav_index')
		# self.pid = self.kwargs.get('pid')
		# print self.pid , "pid"
		pass




class LXSuccessView(LXBase, ListView):
	template_name = 'lx_success.html'
	context_object_name = 'article_list'

	def get_context_data(self, **kwargs):
		kwargs['nav_index'] = 7

		kwargs['tag'],kwargs['article_list']  = action_page.queryOnly(None,28,50)

		return super(LXSuccessView, self).get_context_data(**kwargs)

	def get_queryset(self):
		self.nav_index = self.kwargs.get('nav_index')
		# self.pid = self.kwargs.get('pid')
		# print self.pid , "pid"
		pass



class LXAboutMeView(YMBase, ListView):
	template_name = 'lx_about_me.html'
	# context_object_name = 'article_list'
	def get_context_data(self, **kwargs):
		kwargs['nav_index'] = int(self.nav_index)
		# kwargs['article'] = action_page.GetArticleByID(self.article_id)
		# print kwargs['article']
		return super(LXAboutMeView, self).get_context_data(**kwargs)

	def get_queryset(self):
		pass
		# tag_list = action_page.GetYMIndex()
		# print tag_list
		# return tag_list

	def get(self, request, *args, **kwargs):
		self.nav_index = self.kwargs.get('nav_index')
		self.article_id = self.kwargs.get('article_id')
		return super(LXAboutMeView, self).get(request, *args, **kwargs)



class LXCoverView(LXBase, ListView):
	template_name = 'lx_cover.html'
	def get_context_data(self, **kwargs):
		kwargs['nav_index'] = int(self.nav_index)
		kwargs['tag'] ,kwargs['article_list'] = action_page.GetArticleListByTagID(self.tag_id)
		return super(LXCoverView, self).get_context_data(**kwargs)
	def get_queryset(self):
		pass
	def get(self, request, *args, **kwargs):
		self.nav_index = self.kwargs.get('nav_index')
		self.tag_id = self.kwargs.get('tag_id')
		return super(LXCoverView, self).get(request, *args, **kwargs)


class LXArticleView(LXBase, ListView):
	template_name = 'lx_article.html'
	# context_object_name = 'article_list'
	def get_context_data(self, **kwargs):
		kwargs['nav_index'] = int(self.nav_index)
		kwargs['article'] = action_page.GetArticleByID(self.article_id)
		return super(LXArticleView, self).get_context_data(**kwargs)
	def get_queryset(self):
		pass
	def get(self, request, *args, **kwargs):
		self.nav_index = self.kwargs.get('nav_index')
		self.article_id = self.kwargs.get('article_id')
		return super(LXArticleView, self).get(request, *args, **kwargs)







from models import MGRImage
from django.core.exceptions import PermissionDenied
import base64

class UploadImage(YMBase, ListView):

	def post(self, request, *args, **kwargs):
		print 347283574937894
		if not request.user.is_authenticated():
			logger.error(u'[UserControl]用户未登陆')
			raise PermissionDenied

		# data = request.POST['img']
		data = request.FILES.get('img')
		adminIMG = MGRImage()
		adminIMG.name = data.name
		adminIMG.local_path = data
		adminIMG.save()
		return HttpResponse(
			 "<script>top.$('.mce-btn.mce-open').parent().find('.mce-textbox').val('%s').closest('.mce-window').find('.mce-primary').click();</script>" % adminIMG.url)
		

class LiteFatherTag(LXBase, ListView):
	def get(self, request, *args, **kwargs):

		# _website = 0
		_website = request.GET.get('website',"")
		_father = action_page.GetFatherTag( _website)
		_dict = {
			"father_tag_list":_father
		}
		return MESSAGE_RESPONSE_SUCCESS(_dict)

class LiteCoverArticle(LXBase, ListView):
	def get(self, request, *args, **kwargs):

		# _website = 0
		_father_id = request.GET.get('father_id',"")
		_cover_article = action_page.GetCoverArticleByFather( _father_id)
		_dict = {
			"cover_article_list":_cover_article
		}
		return MESSAGE_RESPONSE_SUCCESS(_dict)

###获取封面
class LiteCover(LXBase, ListView):
	def get(self, request, *args, **kwargs):

		# _website = 0
		_tag_id = request.GET.get('tag_id',"")
		_cover_list = action_page.GetCoverByTag( _tag_id)
		# _dict = {
		# 	"cover_list":_cover_list
		# }
		return MESSAGE_RESPONSE_SUCCESS(_cover_list)


###获取文章
class LiteArticle(LXBase, ListView):
	def get(self, request, *args, **kwargs):
		# _website = 0
		_article_id = request.GET.get('article_id',"")
		_article_dict = action_page.GetArticle( _article_id)
		_dict = {
			"article_dict":_article_dict
		}
		return MESSAGE_RESPONSE_SUCCESS(_dict)

###获取轮播图
class LiteSwiper(LXBase, ListView):
	def get(self, request, *args, **kwargs):
		# _website = 0
		_swiper_tag_id = request.GET.get('swiper_tag_id',"")
		_article_list = action_page.GetSwiper( _swiper_tag_id)
		_dict = {
			"swiper_list":_article_list
		}
		return MESSAGE_RESPONSE_SUCCESS(_dict)



######################### 手机网页 ##########################

class MobileBase(BaseMixin):
	def get_context_data(self, *args, **kwargs):

		kwargs['nav_list'] = action_page.MobileGetNav(self.web_site)

		kwargs['base_url'] = "/live/xx_mgr/mobile/index"
		kwargs['tab_base_url'] = "/live/xx_mgr/mobile/tab"
		kwargs['cover_base_url'] = "/live/xx_mgr/mobile/cover"
		kwargs['article_base_url'] = "/live/xx_mgr/mobile/article"
		# print  11111, kwargs['nav_list']
		context = super(MobileBase, self).get_context_data(**kwargs)
		return context

###手机版首页
class MobileIndex(MobileBase, ListView):
	template_name = 'mobile/index.html'
	# context_object_name = 'article_list'

	def get_context_data(self, **kwargs):
		kwargs['web_site'] = int(self.web_site)

		if kwargs['web_site'] == 0:
			PID_LX_INDEX = 21  #留学
			kwargs['five_tag'], kwargs['five_article_list']  = action_page.queryOnly(PID_LX_INDEX,5,4)  #轮播图
			kwargs['six_tag'], kwargs['six_article_list']  = action_page.queryOnly(PID_LX_INDEX,6,4)
		else:
			PID_LX_INDEX = 11  #移民
		kwargs['one_tag_list'],kwargs['one_article_list']  = action_page.queryMore(PID_LX_INDEX,1)
		kwargs['two_tag'], kwargs['two_article_list']  =action_page.queryOnly(PID_LX_INDEX,2,8)
		print kwargs['two_tag'], kwargs['two_article_list']
		kwargs['three_tag'], kwargs['three_article_list']  = action_page.queryOnly(PID_LX_INDEX,3,9)
		kwargs['four_tag'], kwargs['four_article_list']  = action_page.queryOnly(PID_LX_INDEX,4,8)
		kwargs['five_tag'], kwargs['five_article_list']  = action_page.queryOnly(PID_LX_INDEX,5,4)  #轮播图
			# kwargs['six_tag'], kwargs['six_article_list']  = action_page.queryOnly(PID_LX_INDEX,6,4)
		# print self.web_site,PID_LX_INDEX


		return super(MobileIndex, self).get_context_data(**kwargs)
	def get_queryset(self):
		pass
	def get(self, request, *args, **kwargs):
		self.web_site = self.kwargs.get('web_site')
		return super(MobileIndex, self).get(request, *args, **kwargs)

####子栏目列表###
class MobileTabView(MobileBase, ListView):
	template_name = 'mobile/tab.html'
	def get_context_data(self, **kwargs):
		kwargs['web_site'] = int(self.web_site)
		# kwargs['tag'] ,kwargs['article_list'] = action_page.GetSonTagByFather(self.tag_id)
		kwargs['tag_list']  = action_page.GetSonTagByFather(self.father_id)
		print kwargs['tag_list']
		return super(MobileTabView, self).get_context_data(**kwargs)
	def get_queryset(self):
		pass
	def get(self, request, *args, **kwargs):
		self.web_site = self.kwargs.get('web_site')
		self.father_id = self.kwargs.get('father_id')
		# self.tag_id = 2
		return super(MobileTabView, self).get(request, *args, **kwargs)


####手机封面列表###
class MobileCoverView(MobileBase, ListView):
	template_name = 'mobile/cover.html'
	def get_context_data(self, **kwargs):
		kwargs['web_site'] = int(self.web_site)
		kwargs['tag'] ,kwargs['article_list'] = action_page.GetArticleListByTagID(self.tag_id)
		# print kwargs['tag']["tag_id"]
		return super(MobileCoverView, self).get_context_data(**kwargs)
	def get_queryset(self):
		pass
	def get(self, request, *args, **kwargs):
		self.web_site = self.kwargs.get('web_site')
		self.tag_id = self.kwargs.get('tag_id')
		# self.tag_id = 40
		return super(MobileCoverView, self).get(request, *args, **kwargs)

######## 文章列表
class MobileArticleView(MobileBase, ListView):
	template_name = 'mobile/article.html'
	# context_object_name = 'article_list'
	def get_context_data(self, **kwargs):
		kwargs['web_site'] = int(self.web_site)
		kwargs['article'] = action_page.GetArticleByID(self.article_id)
		return super(MobileArticleView, self).get_context_data(**kwargs)
	def get_queryset(self):
		pass
	def get(self, request, *args, **kwargs):
		self.web_site = self.kwargs.get('web_site')
		self.article_id = self.kwargs.get('article_id')
		return super(MobileArticleView, self).get(request, *args, **kwargs)












