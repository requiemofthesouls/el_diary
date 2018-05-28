from django.contrib import admin
from college.models import *


class SpecialityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Speciality._meta.fields]


admin.site.register(Speciality, SpecialityAdmin)


class DisciplineAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Discipline._meta.fields]


admin.site.register(Discipline, DisciplineAdmin)


class ClassAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cabinets._meta.fields]


admin.site.register(Cabinets, ClassAdmin)


class GroupAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Group._meta.fields]


admin.site.register(Group, GroupAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Student._meta.fields]


admin.site.register(Student, StudentAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Teacher._meta.fields]


admin.site.register(Teacher, TeacherAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.fields]


admin.site.register(Post, PostAdmin)
