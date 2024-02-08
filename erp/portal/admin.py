from django.contrib import admin
from .models import Staff,Department,Students,CourseUnit,Courses

# Register your models here.
admin.site.register(Staff)
admin.site.register(Department)
admin.site.register(Students)
admin.site.register(CourseUnit)
admin.site.register(Courses)