from django.contrib import admin
from school_manager.models import Student, Course,Classroom, RegistrationClassroom


# Register your models here.

admin.site.site_header = 'Painel Administrativo da Escola Contebras'

class CourseAdmin(admin.ModelAdmin):
  list_display = ('name', 'description')

class StudantAdmin(admin.ModelAdmin):
  list_display = ('name', 'email')

class ClassroomAdmin(admin.ModelAdmin):
  list_display = ('name', 'course')
  filter_horizontal = ('student')
  
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Classroom)
# admin.site.register(RegistrationClassroom)