from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
# import json, requests, datetime, time
from django.http import JsonResponse
from datetime import date, datetime
# from requests.adapters import HTTPAdapter
# from requests.packages.urllib3.util.retry import Retry
# from django.utils import timezone
from django.core import serializers
import json , datetime, time
# from . import models
from .models import userTable 

@csrf_exempt
def add_user(request):
    try:
        if request is not dict:
            user_obj_dict = json.loads(request.body)
        else:
            user_dict = request
        if all (key in user_obj_dict and user_obj_dict[key] for key in ['user_name', 'email_id']):
            user_dict = userTable()
            user_dict.user_id = "UI" + str(int(time.time_ns()*10))
            user_dict.user_name = user_obj_dict['user_name']
            user_dict.user_email = user_obj_dict['email_id']
            user_dict.save()
            return_object = {
                "status": '0',
                "message": 'User added Suceessfully'
            }
        else:
            return_object = {
                "status": '1',
                "message": 'Fail'
            }
    except (Exception) as error:
        print(error)
        return_object = {
            "status": '1',
            "message": 'Fail'
        }
    return JsonResponse(return_object, safe=False)


@csrf_exempt
def update_user(request):
    try:
        if request is not dict:
            user_obj_dict = json.loads(request.body)
        else:
            user_dict = request
        if all (key in user_obj_dict and user_obj_dict[key] for key in ['user_name', 'email_id']):
            user_dict = userTable.objects.get(user_id = user_obj_dict['user_id'])
            user_dict.user_name = user_obj_dict['user_name']
            user_dict.user_email = user_obj_dict['email_id']
            user_dict.save()
            return_object = {
                "status": '0',
                "message": 'User updated Suceessfully'
            }
        else:
            return_object = {
                "status": '1',
                "message": 'Fail'
            }
    except (Exception) as error:
        print(error)
        return_object = {
            "status": '1',
            "message": 'Fail'
        }
    return JsonResponse(return_object, safe=False)

@csrf_exempt
def delete_user(request):
    try:
        user_data = json.loads(request.body)
        status = userTable.objects.filter(user_id = user_data['user_id']).update(is_deleted = True)
        if status:
            return_object = {
                "status" : '0',
                "message" : 'User deleted Successfully'
            }
        else:
            return_object = {
                "status" : '0',
                "message" : 'User Data not found',
            }
    except (Exception) as error:
        print("error in update cost details ",error)
        return_object = {
            "status": '1',
            "message": 'Fail to delete user'
        }
    return JsonResponse(return_object,safe = False)


@csrf_exempt
def get_user_details(request):
    try:
        records = userTable.objects.filter(is_deleted = False) 
        data = serializers.serialize("json", records)
        result = json.loads(data)
        for data in range(len(result)):
            user_info = result[data]['fields']
            result.append(user_info) 
        returnObject = {
            "status" : '0',
            "message" :'User Data retrived suceessfully',
            "result" :result
        }
    except:
        returnObject = {
            "status" : '1',
            "message" : 'Fail to retrive user data',
        }
    return JsonResponse(returnObject,safe=False)  
