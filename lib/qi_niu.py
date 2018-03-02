# -*- coding: utf-8 -*-
from django.http import HttpResponse
# import qiniu
import qiniu
# from huaxun_server.settings import (qiniu_access_key,
#                                  qiniu_secret_key,
#                                  qiniu_bucket_name)
from lib.util import *
qiniu_access_key = QINIU_ACCESS_KEY
qiniu_secret_key = QINIU_SECRET_KEY
qiniu_bucket_name = QINIU_BUCKET_NAME
assert qiniu_access_key and qiniu_secret_key and qiniu_bucket_name
import sys
import os
import logging
# logger
logger = logging.getLogger(__name__)

class QiNiu():
    # 上传头像到七牛,返回图片存储名字
    # qiniu_path 七牛的路径
    # filename  文件的名字
    # path  图片本地地址
    def put(self,qiniu_path,filename,local_path):
        try:

            print 1
            q = qiniu.Auth(qiniu_access_key, qiniu_secret_key)

            key = qiniu_path + filename
            localfile = local_path

            # mime_type = "text/plain"
            mime_type = "image/png"
            params = {'x:a': 'a'}

            print key
            print local_path
            print params
            token = q.upload_token(qiniu_bucket_name, key)
            ret, info = qiniu.put_file(token, key, localfile,
                                       mime_type=mime_type, check_crc=True)
            print info
            # 验证上传是否错误
            if ret['key'] != key or ret['hash'] != qiniu.etag(localfile):
                logger.error(
                    u'[UserControl]上传头像错误：[{}]'.format(
                        'test'
                    )
                )
                return HttpResponse(u"上传头像错误", status=500)

            return True

        except Exception as e:
            # request.user.img = "/static/tx/"+filename
            # request.user.save()
            print 'error',e
            # 验证上传是否错误
            if not os.path.exists(local_path):
                logger.error(
                    u'[UserControl]用户上传头像出错:[{}]'.format(
                        'test'
                        # request.user.username
                    )
                )
                return HttpResponse(u"上传头像错误", status=500)

            return HttpResponse(u"上传头像成功!\n(注意有10分钟缓存)")
    def getToken(self,qiniu_path,filename,path):
        q = qiniu.Auth(qiniu_access_key, qiniu_secret_key)

        key = qiniu_path + filename
        localfile = path

        policy = {
            # "callbackUrl":"http://120.27.97.33/upload/token/",
            "callbackUrl":"https://www.12xiong.top/upload/token/",
            "callbackBody":"key=$(key)&hash=$(etag)&w=$(imageInfo.width)&h=$(imageInfo.height)&duration=$(avinfo.video.duration)&fsize=$(fsize)&vw=$(avinfo.video.width)&vh=$(avinfo.video.height)",
            "callbackHost":"120.27.97.33",
            "fsizeLimit": 6815744,
            # "mimeLimit": "image/png"
        }

        token = q.upload_token(qiniu_bucket_name,key = key,policy = policy)
        # token = q.upload_token(QINIU_BUCKET_NAME,key = key)
        return token,key

    def delete(self,key):
        # try:
            #初始化Auth状态
        q = qiniu.Auth(qiniu_access_key, qiniu_secret_key)
        #初始化BucketManager
        bucket = qiniu.BucketManager(q)
        #删除bucket_name 中的文件 key  #你要测试的空间， 并且这个key在你空间中存在
        ret, info = bucket.delete(qiniu_bucket_name, key)
        print(info)
            # return True
        # except Exception as e:
        #     print 'error',e
        #     return False

# q = QiNiu()
# q.put("hx_","a.jpg",r"C:\lab\git\hua_xun\huaxun_server\static\admin\img\gis\move_vertex_off.png")
# q.put("hx_","a.jpg",r"C:\lab\git\hua_xun\huaxun_server\media\1.png")
