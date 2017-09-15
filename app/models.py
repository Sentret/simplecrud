from django.db import models
from django.contrib import admin


class Student(models.Model):
	firstname = models.CharField(max_length=20)
	secondname = models.CharField(max_length=20, blank=True)
	lastname = models.CharField(max_length=20)
	studentcardnumber = models.CharField(max_length=20, blank=True)
	group = models.ForeignKey('Group', null=True, blank=True)

	def __str__(self):
		return self.firstname + ' ' + self.lastname 


class Group(models.Model):
    name = models.CharField(max_length=20)
    monitor = models.ForeignKey(Student, related_name='+', null=True, blank=True)
    

    def get_students(self):
    	return Student.objects.filter(group__id=self.id)


    def __str__(self):
        return self.name + ' : ' + str(self.monitor)


