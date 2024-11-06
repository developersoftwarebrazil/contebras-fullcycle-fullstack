from atexit import register
from django.contrib import admin

from school_materials.models import MaterialCourse

# Register your models here.
class MaterialCourseAdmin(admin.ModelAdmin):
  list_display= ('title_course', 'description_course', 'archive_course_type', 'upload_date')

admin.site.register(MaterialCourse, MaterialCourseAdmin)

