from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import *
from .models import Group,Student
from .forms import GroupForm
from .forms import StudentForm
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class GroupListView(LoginRequiredMixin, ListView):
	model = Group
	context_object_name = 'groups'


class GroupCreateView(LoginRequiredMixin, CreateView):
	model = Group
	form_class = GroupForm

	def get_success_url(self):
		return reverse('group-list')


class GroupDeleteView(LoginRequiredMixin, DeleteView):
	model = Group

	def get_success_url(self):
		return reverse('group-list')


class GroupEditView(LoginRequiredMixin,UpdateView):
    model = Group
    form_class = GroupForm

    def get_success_url(self):
        return reverse('group-list')


class StudentListView(LoginRequiredMixin, View):

	def get(self, request, pk):
		query = Group.objects.get(id=pk).get_students()
		return render(request, 'app/student_list.html', {'query':query,'pk':pk})
		

class StudentDeleteView(LoginRequiredMixin, View):	
	model = Student

	def post(self, request, group_pk, pk):
	    student = Student.objects.get(id=pk)
	    student.delete()
	    query = Group.objects.get(id=group_pk).get_students()
	    return render(request, 'app/student_list.html', {'query':query, 'pk':pk})


class StudentCreateView(LoginRequiredMixin, View):
	def get(self, request, pk):
		form = StudentForm()
		return render(request, 'app/student_form.html', {'form':form})

	def post(self, request, pk):
		form = StudentForm(request.POST)
		if form.is_valid():
			student = form.save()
			student.group = Group.objects.get(id=pk)
			student.save()

		query = Group.objects.get(id=pk).get_students()
		return render(request, 'app/student_list.html', {'query':query, 'pk':pk})	


class StudentEditView(LoginRequiredMixin, View):

    def get(self, request, pk):
        student = Student.objects.get(id=pk)
        form = StudentForm(instance=student)
        return render(request, 'app/student_form.html', {'form':form})


    def post(self, request, pk):
        student = Student.objects.get(id=pk)
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
        
        group_pk = student.group.id        
        query = Group.objects.get(id=group_pk).get_students()
        return render(request, 'app/student_list.html', {'query':query, 'pk':group_pk})	


