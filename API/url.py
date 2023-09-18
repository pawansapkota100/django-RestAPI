from django.urls import path, include
from API import url
from .views import *

urlpatterns = [

    path('student_info',view=student_info),
    path('student_info/<int:number>',view=student_details)
]