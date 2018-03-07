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

YES = 1
NO = 0
IS_SHOW = {
	YES:u"显示",
	NO:u"隐藏",
}

IMAGE_COVER = 1
IMAGE_LOGO = 2
IMAGE_STYLE = {
    IMAGE_COVER:u"封面",
    IMAGE_LOGO:u"头像",
}

ARTICLE_STYLE_NORMAL = 1
ARTICLE_STYLE_TEXT = 2
ARTICLE_STYLE_AUDIO = 3
ARTICLE_STYLE_VIDEO = 4
ARTICLE_STYLE = {
    ARTICLE_STYLE_NORMAL :"普通",
    ARTICLE_STYLE_TEXT :"纯文字",
    ARTICLE_STYLE_AUDIO :"音频",
    ARTICLE_STYLE_VIDEO :"视频",
}
IS_TOP = {
    YES:u"置顶",
    NO:u"不置顶",
}

ROOM_PREPARE = 0
ROOM_PLAYER = 1
ROOM_LIVE = 2
ROOM_STYLE = {
    ROOM_PREPARE:u"准备",
    ROOM_PLAYER:u"直播",
    ROOM_LIVE:u"纯文字",
}

MESSAGE_TEXT = 0
MESSAGE_IMAGE = 1
MESSAGE_AUDIO = 2
MESSAGE_STYLE = {
    MESSAGE_TEXT:u"文字",
    MESSAGE_IMAGE:u"图片",
    MESSAGE_AUDIO:u"语音",
}