from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import *
from django.views.decorators.csrf import csrf_exempt
from .serializers import *

# Create your views here.
@csrf_exempt
def student_view_api(request):
    if request.method == 'POST':
        json_data = request.body
        py_data = json.loads(json_data)
        deserial_data = StudentSerializer(data = py_data)

        if deserial_data.is_valid():
            deserial_data.save()
            return JsonResponse(
                {
                    'Message': "Data Inserted Successfully",
                }
            )
        return JsonResponse(
            {
                'Message': "Data Not Inserted Successfully",
            }
        )

    if request.method == 'GET':
        all_student_details = Student.objects.all()
        serial_data = StudentSerializer(all_student_details, many = True)
        return JsonResponse(serial_data.data, safe = False)


@csrf_exempt
def student_update_api(request, id):
    try:
        stu = Student.objects.get(id=id)
    except:
        return JsonResponse(
            {
                'Message' : "404 Not Found"
            }
        )
    
    if request.method == 'PUT':
        json_data = request.body
        py_data = json.loads(json_data)

        stu.name = py_data.get('name', stu.name)
        stu.age = py_data.get('age', stu.age)
        stu.address = py_data.get('address', stu.address)
        stu.email = py_data.get('email', stu.email)
        stu.phone_number = py_data.get('phone_number', stu.phone_number)
        stu.save()
        return JsonResponse(
            {
                'Message': "Data Updated Successfully",
            }
        )
    
    if request.method == 'GET':
        serial_data = StudentSerializer(stu)
        return JsonResponse(serial_data.data, content_type="application/json")
