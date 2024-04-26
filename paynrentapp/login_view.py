from django.db import connection
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from paynrentapp.serializers import AdministratorSerializers
from paynrentapp.models import Administrator
from . import tuple_to_dict
@api_view(['GET','POST','DELETE'])
def LoginPage(request):
    return render(request,'LoginPage.html')
@api_view(['GET','POST','DELETE'])
def CheckAdminLogin(request):
    try:
        if request.method=='GET':
            q="select * from paynrentapp_administrator where (mobileno='{0}' or emailid='{0}') and password='{1}'".format(request.GET['mobileno'],request.GET['password'])
            # print(q)
            cursor=connection.cursor()
            cursor.execute(q)
            record=tuple_to_dict.ParseDictMultipleRecord(cursor)
            # print('records:::::',record)
            if(len(record)==0):
                return render(request,"LoginPage.html",{'message':"Invalid Admin ID/Password"})
            else:
                return render(request,"DashBoard.html",{'data':record[0]})
    except Exception as error:
        print("Error",error)
        return render(request,"LoginPage.html",{'data':[]})