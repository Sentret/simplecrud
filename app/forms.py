from django import forms
from .models import Group
from .models import Student

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name','monitor']
    
    #старостой может быть только член группы
    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        if self.instance.pk is not None:
            self.fields['monitor'].queryset = Student.objects.filter(group_id=self.instance.pk)


class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['firstname','lastname']