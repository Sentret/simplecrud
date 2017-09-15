from django.conf import settings

#делает доступным settings во всех шаблонах
def settings_to_template(request):
	return {'settings':settings}
