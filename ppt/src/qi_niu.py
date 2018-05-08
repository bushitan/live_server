# -*- coding: utf-8 -*-
from django.http import HttpResponse
# import qiniu
import qiniu

# 七牛配置
QINIU_ACCESS_KEY = 'bK5xWj0a-TBIljlxHYOHuQib9HYF_9Ft-HtP8tEb'
QINIU_SECRET_KEY = '56lucORYc45sF5eDqNk63mLXsQ78n4RrubIrjtE0'
QINIU_BUCKET_NAME = 'clickz'
QINIU_HOST = 'http://image.12xiong.top/'
# QINIU_CALLBACK_URL = "https://www.12xiong.top/day365/lite/upload/callback/"
QINIU_CALLBACK_URL = "https://www.12xiong.top/ppt/self/upload/callback/"
QINIU_CALLBACK_BODY = "key=$(key)&hash=$(etag)&w=$(imageInfo.width)&h=$(imageInfo.height)&duration=$(avinfo.video.duration)&fsize=$(fsize)&vw=$(avinfo.video.width)&vh=$(avinfo.video.height)"
QINIU_CALLBACK_HOST = "120.27.97.33"
QINIU_FSIZE_LIMIT = 6815744

import sys
import os
import logging
# logger
logger = logging.getLogger(__name__)

# class QiNiu():
def QiNiuGetToken(file_name):
    q = qiniu.Auth(QINIU_ACCESS_KEY, QINIU_SECRET_KEY)
    key = file_name
    url = QINIU_HOST + file_name
    policy = {
        "callbackUrl":QINIU_CALLBACK_URL,
        "callbackBody":QINIU_CALLBACK_BODY,
        "callbackHost":QINIU_CALLBACK_HOST,
        "fsizeLimit": QINIU_FSIZE_LIMIT,
    }
    token = q.upload_token(QINIU_BUCKET_NAME,key = key,policy = policy)
    return token,key,url