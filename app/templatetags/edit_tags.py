from django import template
from django.db import models


register = template.Library()


#возвращает ссылку на редактирование в адмминке, если передан объект модели
@register.simple_tag
def edit(obj):
	try:
	    assert issubclass(type(obj),models.Model) 
	except:
		return 'Тегу передан объект, не наследованный от класса django.db.models.Model'
	model_name = type(obj).__name__
	return '/admin/app/%s/%s/change/' % (model_name.lower(), obj.id)