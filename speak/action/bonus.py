# -*- coding: utf-8 -*-
from lib.util import *
import json
import urllib2
from django.db import transaction
from lite.query.user import *
from lite.query.file_library import *
from speak.query.speak_theme import *
from speak.query.speak_user import *
from speak.query.speak_bonus import *
from speak.query.speak_set_score import *
from lib.qi_niu import *
class ActionBonus():
    def __init__(self):
        self.query_theme = QuerySpeakTheme()
        self.query_speak_user = QuerySpeakUser()
        self.query_speak_bonus = QuerySpeakBonus()
        self.query_user = QueryUser()
        self.query_file = QueryFileLibrary()
        self.query_set_score = QuerySpeakSetScore()
        self.qiniu = QiNiu()

    def _sys_score(self,action):
        return self.query_set_score.GetScore(action)

    #打卡获取积分
    # 1 查用户
    # 2 增加积分
    def addCheck(self,session,theme_id):
        _self = self.query_user.GetQuery(session=session)
        if self.query_speak_bonus.IsExists(
            user_self_id = _self.id ,
            theme_id = theme_id,
            action = SPEAK_ACTION_CHECK,
        ) is True: #避免重复分享
            return BONUS_CODE_CHECK_EXIST,'已打卡'
        else:
            _score = self._sys_score(SPEAK_ACTION_CHECK)
            self.query_speak_bonus.Add(
                user_self_id = _self.id ,
                theme_id = theme_id,
                action = SPEAK_ACTION_CHECK,
                score = _score,
            )
            return BONUS_CODE_CHECK,"打卡成功，积分+" +  str( _score )

    #分享获取积分
    # 1 查session是否存在bonus表中，
    # 2 已存在，不得积分
    # 3 未存在，加积分
    # self 是分享者  other是新用户
    def addShare(self,self_id,other_session):
        _self = self.query_user.GetQuery(id=self_id)
        _other = self.query_user.GetQuery(session=other_session)
        if _self.id == _other.id:
            return BONUS_CODE_SHARE_SELF,'分享给别人才有积分哦~'
        if self.query_speak_bonus.IsExists(
            user_self_id = _self.id ,
            user_other_id = _other.id ,
        ) is True: #避免重复分享
            return BONUS_CODE_SHARE_EXIST,'该用户已经接受了分享'
        else:
            _score = self._sys_score(SPEAK_ACTION_SHARE)
            self.query_speak_bonus.Add(
                user_self_id = _self.id ,
                user_other_id = _other.id ,
                action = SPEAK_ACTION_SHARE,
                score = _score,
            )
            return BONUS_CODE_SHARE,'接受分享成功'

    #报名获取积分
    # 1 重复报名
    # 2 报名成功
    def addSignIn(self,session,name,phone):
        with transaction.atomic():
            #用户报名数据
            _self = self.query_user.FilterQuery(session=session)
            _self_id = _self[0].id
            self.query_user.Update(_self,name = name,phone = phone)
            #增加积分
            if self.query_speak_bonus.IsExists(
                user_self_id = _self_id,
                action = SPEAK_ACTION_SIGN_IN,
            ) is True:
                 return BONUS_CODE_SIGN_IN_EXIST ,'已经报名'
            else:
                _score = self._sys_score(SPEAK_ACTION_SIGN_IN)
                self.query_speak_bonus.Add(
                    user_self_id = _self_id,
                    action = SPEAK_ACTION_SIGN_IN,
                    score = _score ,
                )
                return BONUS_CODE_SIGN_IN,'报名成功，积分+' + str(_score)

    #兑换积分
    # 1 app_id 下是，other_session是否为教师
    # 2 session剩余积分 大于0 ，扣除成功
    # 3 积分小于0 扣除失败
    # self 是学生  other是老师扣除
    def exchangeGift(self,session,other_session,cost_score):
        _self = self.query_user.GetQuery(session=session)
        _other = self.query_user.GetQuery(session=other_session)
        _sum_score = self.query_speak_bonus.Remain( _self.id)  #剩余积分
        if _sum_score > cost_score: #当剩余积分大于花费
            self.query_speak_bonus.Add(
                user_self_id = _self.id ,
                user_other_id = _other.id ,
                action = SPEAK_ACTION_COST,
                score = cost_score,
            )
            return BONUS_CODE_COST ,'礼品兑换成功，消耗积分：' + str(cost_score)
        else:
            return BONUS_CODE_COST_NOT_ENOUGH ,"积分不足"


    # 获取用户积分记录
    def getRecode(self,session):
        _self = self.query_user.GetQuery(session=session)
        return self.query_speak_bonus.Filter(user_self__session = session)

    #获取用户总分数
    def getScore(self,session):
        _self = self.query_user.GetQuery(session=session)
        return self.query_speak_bonus.Remain( _self.id)  #剩余积分


if __name__ == "__main__":

    import django
    django.setup()
    a = ActionBonus()
    # print a.GetTagList()
    # print a.addVoice('9GEUS5/0FMeW2hnRpBOBzg==','httpwoiqewo',1)
    # print a.getThemeList()
    # print login.CheckSession('2w321321' , "12321321")















