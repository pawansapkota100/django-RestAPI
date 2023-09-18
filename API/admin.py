from django.contrib import admin
from .models import studentModel
class studentadmin(admin.ModelAdmin):
    list_display=['id','name','Class','city','age']
admin.site.register(studentModel, studentadmin)