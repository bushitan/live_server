#coding:utf-8
class QueryBase(object):
	def __init__(self,model = None):
		self.model = model
	def _PackList(self,_pack_fun,query_filter):
		_list = []
		for q in query_filter:
			_list.append( _pack_fun(q) )
		return _list

	def _PackDict(self,*args, **kwargs):
		pass

	def IsExists(self, *args, **kwargs):
		return self.model.objects.filter(*args, **kwargs).exists()

	def Add(self,*args,**kwargs):
		_m = self.model(*args,**kwargs)
		_m.save()
		return self._PackDict(_m)

	def Get(self,*args,**kwargs):
		_m = self.model.objects.get(*args,**kwargs)
		return self._PackDict(_m)

	def GetQuery(self,*args,**kwargs):
		return self.model.objects.get(*args,**kwargs)
		# return self._PackDict(_m)

	def Filter(self,*args,**kwargs):
		_m = self.model.objects.filter(*args,**kwargs)
		return self._PackList( self._PackDict,_m)

	def FilterQuery(self,*args,**kwargs):
		return self.model.objects.filter(*args,**kwargs)

	def Update(self,obj,*args,**kwargs):
		obj.update(*args,**kwargs)
		return self._PackList( self._PackDict,obj)

	def Delete(self,obj):
		obj.delete()
		return True