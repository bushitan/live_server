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

		kwargs['nav_list'] = action_page.GetYMNav()
		context = super(BaseMixin, self).get_context_data(**kwargs)

		return context
class YMIndexView(BaseMixin, ListView):
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


class YMCountryView(BaseMixin, ListView):
	template_name = 'ym_country.html'
	# context_object_name = 'article_list'
	def get_context_data(self, **kwargs):
		kwargs['nav_index'] = int(self.nav_index)

		tag,article = action_page.GetYMCountryAd()
		kwargs['ad'] = article

		kwargs['info_tag'],kwargs['info_article_list'] = action_page.GetYMCountryInfo()

		kwargs['detail_tag_list'],kwargs['detail_article_list'] = action_page.GetYMCountryDetail()



		return super(YMCountryView, self).get_context_data(**kwargs)

	def get_queryset(self):
		tag_list = action_page.GetYMIndex()
		print tag_list
		return tag_list

	def get(self, request, *args, **kwargs):

		self.nav_index = self.kwargs.get('nav_index')
		self.pid = self.kwargs.get('pid')

		# kwargs['nav_index'] = country_id
		# print country_id
		return super(YMCountryView, self).get(request, *args, **kwargs)





























