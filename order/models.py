#coding:utf-8
from django.db import models
from lib.util import *
from lib.image_save import *
from lite.models import *
from cover.models import *
import django.utils.timezone as timezone
# Create your models here.


# 会议费用
class Cost(models.Model):
    app =  models.ForeignKey( App, verbose_name=u'所属小程序',null=True,blank=True)
    name =  models.CharField(max_length=100, verbose_name=u'小程序-项目名称',default="",null=True,blank=True)
    name_admin =  models.CharField(max_length=100, verbose_name=u'后台-项目名称',default="",null=True,blank=True)
    description = models.CharField(max_length=100, verbose_name=u'费用说明',null=True,blank=True)
    unit_price = models.FloatField(u'单价',default=0)
    duration = models.IntegerField(u'会员持续时间',default=0,)
    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
    # 点击链接的文章
    class Meta:
        verbose_name_plural = verbose_name = u'费用明细'
        ordering = ['-create_time']
    def __unicode__(self):
        return '%s' % (self.name_admin)


class Member(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户',related_name='order_user',null=True,blank=True)
    cost = models.ForeignKey(Cost, verbose_name=u'会议支付项目',null=True,blank=True)
    is_alive = models.IntegerField( verbose_name=u'是否有效',default=YES,choices=IS_ALIVE.items())
    start_time = models.DateTimeField(u'开始时间', default = timezone.now)
    end_time = models.DateTimeField(u'结束时间', default = timezone.now)
    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
    # 点击链接的文章
    class Meta:
        verbose_name_plural = verbose_name = u'会员列表'
        ordering = ['-create_time']
    def __unicode__(self):
        return '%s' % (self.id)

# class Single(models.Model):
#     user = models.ForeignKey(User, verbose_name=u'用户',related_name='order_user',null=True,blank=True)

#6 会议订单
class Order(models.Model):
    member = models.ForeignKey(Member, verbose_name=u'参会报名',null=True,blank=True)
    #订单是否有效
    is_alive = models.IntegerField(u'订单状态',default=YES,choices=IS_ALIVE.items())
    #订单支付状态
    is_pay = models.IntegerField(u'支付状态',default=NO,choices=IS_PAY.items(),)
    #微信支付部分
    wx_out_trade_no = models.CharField(max_length=32, verbose_name=u'微信_商户订单号',null=True,blank=True)

    discount = models.ForeignKey('Discount', verbose_name=u'优惠券',null=True,blank=True)
    # num = models.IntegerField(u'数量',default=0)
    # total_price = models.FloatField(u'总价',default=0)
    origin_price = models.FloatField(u'原始价格',default=0)
    pay_price = models.FloatField(u'支付价格',default=0)
    remark = models.CharField(max_length=100, verbose_name=u'备注',null=True,blank=True)
    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
    # 点击链接的文章
    class Meta:
        verbose_name_plural = verbose_name = u'支付订单'
        ordering = ['-create_time']
    def __unicode__(self):
        return '%s' % (self.id)




class DiscountTemplate(models.Model):
    #会员
    name = models.CharField(max_length=100, verbose_name=u'优惠券名称',null=True,blank=True)
    price = models.FloatField( verbose_name=u'优惠价格',default=5)
    limit_fee = models.FloatField( verbose_name=u'最低使用价格',default=0)  #最低使用价格为0元
    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
    class Meta:
        verbose_name_plural = verbose_name = u'优惠券模板'
        ordering = ['-create_time']
        # app_label = 'api'
    def __unicode__(self):
        # _id = self.id
        if self.id < 10 :
            _id = "0" + str(self.id)
        else:
            _id = str(self.id)
        return 'T%s : %s' % (_id,self.name)

def three_day_hence(): #优惠券默认3天有效期
    return timezone.now() + timezone.timedelta(days=3)

#优惠券
class Discount(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户名称',null=True,blank=True)
    template = models.ForeignKey('DiscountTemplate', verbose_name=u'优惠券类型')
    #1 是否使用
    is_used = models.IntegerField(u'是否使用',default=YES,choices=IS_SHOW.items())
    # is_active = models.IntegerField(u'是否作废',default=YES,choices=IS_SHOW.items())
    is_alive = models.IntegerField( verbose_name=u'是否有效',default=YES,choices=IS_ALIVE.items())
    #2 使用时间
    start_time = models.DateTimeField(u'开始时间', default = timezone.now)
    end_time = models.DateTimeField(u'结束时间', default=three_day_hence )
    #3 使用区域

    create_time = models.DateTimeField(u'创建时间', default = timezone.now)
    class Meta:
        verbose_name_plural = verbose_name = u'优惠券'
        ordering = ['-create_time']
        # app_label = 'api'
    def __unicode__(self):
        return '%s' % (self.id)
