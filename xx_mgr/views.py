# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.views.generic import  ListView
# Create your views here.

import json
import logging
from action.page import *
action_page = ActionPage()

class BaseMixin(object):
	def get_context_data(self, *args, **kwargs):
		# kwargs['nav_list'] = action_page.GetNav(self)
		context = super(BaseMixin, self).get_context_data(**kwargs)
		return context

class YMBase(BaseMixin):
	def get_context_data(self, *args, **kwargs):
		kwargs['nav_list'] = action_page.GetNav(1)
		context = super(YMBase, self).get_context_data(**kwargs)
		return context

class YMIndexView(YMBase, ListView):
	template_name = 'ym_index.html'
	context_object_name = 'article_list'

	def get_context_data(self, **kwargs):
		# pass
		# 轮播
		# kwargs['carousel_page_list'] = Carousel.objects.all()
		one_tag_list,one_article_list ,two_tag,two_article_list    ,three_tag, three_article_list   ,  four_tag,four_article_list  =  action_page.GetYMIndex()
		# kwargs['news'] = tag_list[0]
		# kwargs['tag_list'] = tag_list
		# kwargs['one_tag_list'] = tag_list
		# kwargs['nav_list'] = action_page.GetYMNav()
		kwargs['nav_index'] = 0



		kwargs['one_tag_list'] = one_tag_list
		kwargs['one_article_list'] = one_article_list

		kwargs['two_tag'] = two_tag
		kwargs['two_article_list'] = two_article_list

		kwargs['three_tag'] = three_tag
		kwargs['three_article_list'] = three_article_list

		kwargs['four_tag'] = four_tag
		kwargs['four_article_list'] = four_article_list


		return super(YMIndexView, self).get_context_data(**kwargs)

	def get_queryset(self):
		tag_list = action_page.GetYMIndex()
		print tag_list
		return tag_list
		# action_page.
		# article_list = Article.objects.filter(status=0)
		# return article_list

# 移民国家子项
class YMCountryView(YMBase, ListView):
	template_name = 'ym_country.html'
	# context_object_name = 'article_list'
	def get_context_data(self, **kwargs):
		kwargs['nav_index'] = int(self.nav_index)

		print 10
		tag,article = action_page.GetYMCountryAd()
		kwargs['ad'] = article
		print 11
		kwargs['info_tag'],kwargs['info_article_list'] = action_page.GetYMCountryInfo()
		print 12
		kwargs['detail_tag_list'],kwargs['detail_article_list'] = action_page.GetYMCountryDetail()

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

class YMCoverView(YMBase, ListView):
	template_name = 'ym_cover.html'
	# context_object_name = 'article_list'
	def get_context_data(self, **kwargs):
		kwargs['nav_index'] = int(self.nav_index)

		kwargs['article_list'] = action_page.GetArticleListByTagID(self.tag_id)
		# tag,article = action_page.GetYMCountryAd()
		# kwargs['ad'] = article
		# kwargs['info_tag'],kwargs['info_article_list'] = action_page.GetYMCountryInfo()
		# kwargs['detail_tag_list'],kwargs['detail_article_list'] = action_page.GetYMCountryDetail()
		return super(YMCoverView, self).get_context_data(**kwargs)

	def get_queryset(self):
		tag_list = action_page.GetYMIndex()
		print tag_list
		return tag_list

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
		print kwargs['article']
		return super(YMArticleView, self).get_context_data(**kwargs)

	def get_queryset(self):
		tag_list = action_page.GetYMIndex()
		print tag_list
		return tag_list

	def get(self, request, *args, **kwargs):
		self.nav_index = self.kwargs.get('nav_index')
		self.article_id = self.kwargs.get('article_id')
		return super(YMArticleView, self).get(request, *args, **kwargs)


class AboutMeView(YMBase, ListView):
	template_name = 'about_me.html'
	# context_object_name = 'article_list'
	def get_context_data(self, **kwargs):
		kwargs['nav_index'] = int(self.nav_index)
		# kwargs['article'] = action_page.GetArticleByID(self.article_id)
		# print kwargs['article']
		return super(AboutMeView, self).get_context_data(**kwargs)

	def get_queryset(self):
		tag_list = action_page.GetYMIndex()
		print tag_list
		return tag_list

	def get(self, request, *args, **kwargs):
		self.nav_index = self.kwargs.get('nav_index')
		self.article_id = self.kwargs.get('article_id')
		return super(AboutMeView, self).get(request, *args, **kwargs)





############################留学#########################



class LXBase(BaseMixin):
	def get_context_data(self, *args, **kwargs):

		kwargs['nav_list'] = action_page.GetNav(0)
		print  11111, kwargs['nav_list']
		context = super(LXBase, self).get_context_data(**kwargs)
		return context

class LXIndexView(LXBase, ListView):
	template_name = 'lx_index.html'
	context_object_name = 'article_list'

	def get_context_data(self, **kwargs):
		# pass
		# 轮播
		# kwargs['carousel_page_list'] = Carousel.objects.all()
		one_tag_list,one_article_list ,two_tag,two_article_list    ,three_tag, three_article_list   ,  four_tag,four_article_list  =  action_page.GetYMIndex()
		# kwargs['news'] = tag_list[0]
		# kwargs['tag_list'] = tag_list
		# kwargs['one_tag_list'] = tag_list
		# kwargs['nav_list'] = action_page.GetYMNav()
		kwargs['nav_index'] = 0


		PID_LX_INDEX = 21
		kwargs['one_tag_list'],kwargs['one_article_list']  = action_page.queryMore(PID_LX_INDEX,1)

		# print kwargs['one_tag_list']
		# kwargs['one_article_list'] = one_article_list

		kwargs['two_tag'], kwargs['two_article_list']  =action_page.queryOnly(PID_LX_INDEX,2,8)
		# kwargs['two_tag'] = two_tag
		# kwargs['two_article_list'] = two_article_list

		kwargs['three_tag'], kwargs['three_article_list']  = action_page.queryOnly(PID_LX_INDEX,3,9)

		kwargs['four_tag'], kwargs['four_article_list']  = action_page.queryOnly(PID_LX_INDEX,4,8)


		kwargs['five_tag'], kwargs['five_article_list']  = action_page.queryOnly(PID_LX_INDEX,5,4)
		kwargs['six_tag'], kwargs['six_article_list']  = action_page.queryOnly(PID_LX_INDEX,6,4)
		# kwargs['three_tag'] = three_tag
		# kwargs['three_article_list'] = three_article_list

		# kwargs['four_tag'] = four_tag
		# kwargs['four_article_list'] = four_article_list


		return super(LXIndexView, self).get_context_data(**kwargs)

	def get_queryset(self):
		tag_list = action_page.GetYMIndex()
		# print tag_list
		return tag_list
		# action_page.
		# article_list = Article.objects.filter(status=0)
		# return article_list



class LXCountryView(LXBase, ListView):
	template_name = 'lx_country.html'
	context_object_name = 'article_list'

	def get_context_data(self, **kwargs):
		kwargs['nav_index'] = 0

		kwargs['one_tag'],kwargs['one_article']  = action_page.getOnly(self.pid,1)
		print kwargs['one_article']
		kwargs['two_tag'], kwargs['two_article']  = action_page.getOnly(self.pid,2)
		kwargs['three_tag'], kwargs['three_article']  = action_page.getOnly(self.pid,3)
		# kwargs['three_tag'], kwargs['three_article_list']  = action_page.queryOnly(self.pid,3,8)
		# kwargs['two_tag'], kwargs['two_article_list']  = action_page.getOnly(self.pid,1)



		PID_LX_INDEX = 21


		# kwargs['one_tag_list'],kwargs['one_article_list']  = action_page.queryMore(PID_LX_INDEX,1)
		#
		# kwargs['two_tag'], kwargs['two_article_list']  =action_page.queryOnly(PID_LX_INDEX,2,8)
		#
		# kwargs['three_tag'], kwargs['three_article_list']  = action_page.queryOnly(PID_LX_INDEX,3,9)
		#
		# kwargs['four_tag'], kwargs['four_article_list']  = action_page.queryOnly(PID_LX_INDEX,4,8)
		#
		# kwargs['five_tag'], kwargs['five_article_list']  = action_page.queryOnly(PID_LX_INDEX,5,4)
		# kwargs['six_tag'], kwargs['six_article_list']  = action_page.queryOnly(PID_LX_INDEX,6,4)


		return super(LXCountryView, self).get_context_data(**kwargs)

	def get_queryset(self):
		self.nav_index = self.kwargs.get('nav_index')
		self.pid = self.kwargs.get('pid')
		# print self.pid , "pid"
		pass
		# tag_list = action_page.GetYMIndex()
		# return tag_list



class LXStudyView(LXBase, ListView):
	template_name = 'lx_success.html'
	context_object_name = 'article_list'

	def get_context_data(self, **kwargs):
		kwargs['nav_index'] = 6

		# kwargs['one_tag'],kwargs['one_article']  = action_page.getOnly(self.pid,1)
		# print kwargs['one_article']
		# kwargs['two_tag'], kwargs['two_article']  = action_page.getOnly(self.pid,2)
		# kwargs['three_tag'], kwargs['three_article']  = action_page.getOnly(self.pid,3)

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
		# kwargs['one_tag'],kwargs['one_article']  = action_page.getOnly(self.pid,1)
		# print kwargs['one_article']
		# kwargs['two_tag'], kwargs['two_article']  = action_page.getOnly(self.pid,2)
		# kwargs['three_tag'], kwargs['three_article']  = action_page.getOnly(self.pid,3)

		return super(LXSuccessView, self).get_context_data(**kwargs)

	def get_queryset(self):
		self.nav_index = self.kwargs.get('nav_index')
		# self.pid = self.kwargs.get('pid')
		# print self.pid , "pid"
		pass





















