#coding:utf-8

from qi_niu import *
# from ..models import *
import datetime
from util import *

def ImageSave(self,FileLibrary):
        #ID 为空，新增图片

    if self.id is None:
        super(FileLibrary, self).save() #先保存一遍
        try:
            url = self.local_path.url  #如果为空的图片上传，会保存出错，则不上传七牛云
            QNUploadImageMeet(self,FileLibrary)
        except:
            return
    #未保存前，获取原来的地址
    m = FileLibrary.objects.get(id = self.id)
    _old_path = m.local_path.path if m.local_path != "" else ""
    print "2:",_old_path
    super(FileLibrary, self).save()

    #保存后，获取新地址
    _new_path = self.local_path.path if self.local_path !="" else ""
    print "3:",_new_path
    #地址没变化，直接保存
    if  _old_path == _new_path:
        return
    else:
        QNUploadImageMeet(self,FileLibrary)

    #更新图片
def QNUploadImageMeet(self,FileLibrary):
        #获取本地地址
        _local_path = self.local_path.path
        _now = datetime.datetime.now()
        _name = QINIU_IMG_NAME + "_" + str(self.id) + "_" + _now.strftime("%Y_%m_%d_%H_%M_%S") # 拼接名字
        _style = _local_path.split(".")[-1] # 拼接类别
        _file_name = _name + "." + _style # 拼接图片名字
        self.url =  QINIU_HOST + _file_name #存储的链接
        self.name = _file_name
        # #上传七牛
        _qiniu = QiNiu()
        print self.local_path.url
        print self.local_path.name
        _qiniu.put( "" , _file_name , _local_path )
        super(FileLibrary, self).save()
