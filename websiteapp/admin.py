from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register([menus, Admission, StudentGrade, StudentClass, Gender, subjectsix, subjectseven, subjecteight, subjectnine, subjectten, stunotes, stuhomeworks, teacherregister, teachereducation])