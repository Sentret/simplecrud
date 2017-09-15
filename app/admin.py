from django.contrib import admin
from .models import Group
from .models import Student


#inline для Student, теперь класс Student 
#редактируется в том же месте, что и Group
class StudentInline(admin.TabularInline):
	model = Student


# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
# 	#список имен всех полей модели Student
# 	fields = [f.name for f in Student._meta.get_fields()]
# 	#fields будут отображаться на панели модели
# 	list_display = fields
# 	#костыль, без этого не работает
# 	list_display_links = None
# 	#fields редактируются в таблице модели
# 	list_editable = fields


admin.site.register(Student)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
	inlines = (StudentInline,)
	list_display = ('name','monitor')
	list_display_links = None
	list_editable = ('name','monitor')





