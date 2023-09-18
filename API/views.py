from django.shortcuts import render
from django.http import JsonResponse 
from .models import studentModel
from .serializer import studentserializer
# Create your views here.
def student_info(request):
    stu= studentModel.objects.all()
    serial= studentserializer(stu, many=True)
    return JsonResponse(serial.data ,safe=False)

def student_details(request,number):
    stu= studentModel.objects.get(id=number)
    serial= studentserializer(stu)
    return JsonResponse(serial.data)