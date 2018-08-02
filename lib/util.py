# -*- coding: utf-8 -*-
import django.utils.timezone as timezone
#小程序配置
APP_ID = "wx95ed67937837f4e5"
APP_SECRET = "a3f103b09e27d46b722aa2e74afb39be"
MACH_ID = "1488713872"
MACH_KEY = "283fc3d9d4b8ba3b58601145466d4417"

# 七牛配置
QINIU_ACCESS_KEY = 'bK5xWj0a-TBIljlxHYOHuQib9HYF_9Ft-HtP8tEb'
QINIU_SECRET_KEY = '56lucORYc45sF5eDqNk63mLXsQ78n4RrubIrjtE0'
QINIU_BUCKET_NAME = 'clickz' #空间名称
QINIU_IMG_NAME = "live"  #路径前缀
QINIU_HOST = 'http://image.12xiong.top/'
QINIU_CALLBACK_URL = "https://www.12xiong.top/day365/lite/upload/callback/"
QINIU_CALLBACK_BODY = "key=$(key)&hash=$(etag)&w=$(imageInfo.width)&h=$(imageInfo.height)&duration=$(avinfo.video.duration)&fsize=$(fsize)&vw=$(avinfo.video.width)&vh=$(avinfo.video.height)"
QINIU_CALLBACK_HOST = "120.27.97.33"
QINIU_FSIZE_LIMIT = 6815744
QINIU_KEY_HASH = {}  ##七牛上传的hash文件信息

YES = 1
NO = 0
IS_SHOW = {
	YES:u"显示",
	NO:u"隐藏",
}
IS_ALIVE = {
    YES:u"激活",
    NO:u"失效",
}
IS_TOP = {
    YES:u"置顶",
    NO:u"不置顶",
}

IS_PAY = {
    YES:u"已支付",
    NO:u"未支付",
}

IS_TEACHER = {
    YES:u"讲师",
    NO:u"听众",
}


FILE_IMAGE = 0
FILE_AUDIO = 1
FILE_VIDEO = 2
FILE_STYLE = {
    FILE_IMAGE:u"图片",
    FILE_AUDIO:u"音频",
    FILE_VIDEO:u"视频",
}

ARTICLE_STYLE_NORMAL = 1
ARTICLE_STYLE_TEXT = 2
ARTICLE_STYLE_AUDIO = 3
ARTICLE_STYLE_VIDEO = 4
ARTICLE_STYLE_LIVE = 5
ARTICLE_STYLE = {
    ARTICLE_STYLE_NORMAL :"普通",
    ARTICLE_STYLE_TEXT :"纯文字",
    ARTICLE_STYLE_AUDIO :"音频",
    ARTICLE_STYLE_VIDEO :"视频",
    ARTICLE_STYLE_LIVE :"直播回放",
}
ROOM_PREPARE = 0
ROOM_PLAYER = 1
ROOM_LIVE = 2
ROOM_STYLE = {
    ROOM_PREPARE:u"准备",
    ROOM_PLAYER:u"直播",
    ROOM_LIVE:u"纯文字",
}
ROOM_STATUS_PREPARE = 0
ROOM_STATUS_ING = 1
ROOM_STATUS_END = 2
ROOM_STATUS = {
    ROOM_STATUS_PREPARE:u"准备",
    ROOM_STATUS_ING:u"进行中",
    ROOM_STATUS_END:u"已经输",
}


MESSAGE_TEXT = 0
MESSAGE_IMAGE = 1
MESSAGE_AUDIO = 2
MESSAGE_STYLE = {
    MESSAGE_TEXT:u"文字",
    MESSAGE_IMAGE:u"图片",
    MESSAGE_AUDIO:u"语音",
}


VERTICAL = 0  #竖屏
HORIZONTAL = 1 #横屏




##speak 要素
SPEAK_ACTION_CHECK = 0
SPEAK_ACTION_SHARE = 1
SPEAK_ACTION_COST = 2
SPEAK_ACTION_SIGN_IN = 3
# SPEAK_ACTION_LOGO = 3
SPEAK_ACTION = {
    SPEAK_ACTION_CHECK:u"打卡",
    SPEAK_ACTION_SHARE:u"分享",
    SPEAK_ACTION_COST:u"消费",
    SPEAK_ACTION_SIGN_IN:u"报名",
    # SPEAK_ACTION_LOGO:u"上传头像",
}

BONUS_CODE_CHECK = 1101         #打卡
BONUS_CODE_CHECK_EXIST = 1102   #重复打卡
BONUS_CODE_SHARE = 1103         #分享
BONUS_CODE_SHARE_SELF = 1104    #分享给自己
BONUS_CODE_SHARE_EXIST = 1105   #已经接受分享
BONUS_CODE_SIGN_IN = 1106         #报名
BONUS_CODE_SIGN_IN_EXIST = 1107   #已报名
BONUS_CODE_COST = 1108      #积分兑换成功
BONUS_CODE_COST_NOT_ENOUGH = 1109      #积分不足


