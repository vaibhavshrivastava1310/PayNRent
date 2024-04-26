from django.db import connection
from django.shortcuts import render
from django.http.response import JsonResponse
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from paynrentapp.serializers import VehiclesSerializers
from paynrentapp.models import Vehicles
from . import tuple_to_dict
import json
import datetime
@api_view(['GET','POST','DELETE'])
def Home(request):
    return render(request,'Index.html')
@api_view(['GET','POST','DELETE'])
def DisplayVehicleForUser(request):
    if request.method=='GET':
        try:
          if(request.GET['param']=="all"):
             q="select V.*,(select C.categoryname from paynrentapp_category C where C.id=V.categoryid) as categoryname,(select S.subcategoryname from paynrentapp_subcategory S where S.id=V.subcategoryid) as subcategoryname from paynrentapp_vehicles V" 
          else:
              q="select V.*,(select C.categoryname from paynrentapp_category C where C.id=V.categoryid) as categoryname,(select S.subcategoryname from paynrentapp_subcategory S where S.id=V.subcategoryid) as subcategoryname from paynrentapp_vehicles V where V.subcategoryid in (select id from paynrentapp_subcategory where companyname in({}) or fueltype in ({}) or transmissiontype in ({}) or noofseats in ({}))".format(request.GET['param'],request.GET['param'],request.GET['param'],request.GET['param'],request.GET['param'])
        #   print(q)
          cursor=connection.cursor()
          cursor.execute(q)
          records=tuple_to_dict.ParseDictMultipleRecord(cursor)
        #   print('XXXXXXXXXXX',records)
          return JsonResponse(records,safe=False) 
        except Exception as error:
            print('Error:',error)
            return JsonResponse(records,safe=False)
@api_view(['GET','POST','DELETE'])
def ShowVehicleList(request):
    userdata={'mobileno':'','city':request.GET['city'],'starttime':request.GET['starttime'],'endtime':request.GET['endtime'],'days':request.GET['dh']}
    request.session["USERDATA"]=userdata
    return JsonResponse(userdata,safe=False) 
@api_view(['GET','POST','DELETE'])
def PageUserVehicle(request):
    userdata=request.session["USERDATA"]  # session is used to set a function used to share the a value into a programm 
    # print("Usssssssssssss",userdata)
    return render(request,'UserVehicleList.html',{'userdata':userdata})
@api_view(['GET','POST','DELETE'])
def DisplaySelectedVehicle(request):
    vehicle=request.GET['vehicle']
    selected_vehicle=json.loads(vehicle)
    # print('xxxxxxxxxxxxxxxxxxxxxx',selected_vehicle)
    userdata=request.session["USERDATA"]
    st=datetime.datetime.strptime(userdata['starttime'],"%Y/%m/%d %H:%M")
    et=datetime.datetime.strptime(userdata['endtime'],"%Y/%m/%d %H:%M")
    userdata['starttime']=datetime.datetime.strftime(st,"%a,%d %b %Y")
    userdata['endtime']=datetime.datetime.strftime(et,"%a,%d %b %Y")
    d=userdata['days'].split(":")
    # print(d)
    userdata['days']=d[0]+"Days,"+" "+d[1]+" Hour"
    userdata['fare']=selected_vehicle['price']
    hr=int(selected_vehicle['price'])//24
    userdata['amount']=(int(d[0])*int(selected_vehicle['price']))+(hr*int(d[1]))
    userdata['netamount']=userdata['amount']+400
    return render(request,'DisplaySelectedVehicle.html',{'vehicle':selected_vehicle,'userdata':userdata})
@api_view(['GET','POST','DELETE'])
def SetMobileAndEmail(request):
    userdata=request.session["USERDATA"]
    userdata['mobileno']=request.GET['mobileno']
    userdata['emailaddress']=request.GET['emailaddress']
    userdata['amount']=request.GET['amount']
    request.session["USERDATA"]=userdata
    return JsonResponse(userdata,safe=False) 
@api_view(['GET','POST','DELETE'])
def ModifyLocationTime(request):
    userdata=request.session['USERDATA']
    userdata['city']=request.GET['city']
    userdata['starttime']=request.GET['starttime']
    userdata['endtime']=request.GET['endtime']
    userdata['days']=request.GET['dh']
    # print("xxxxxxxxxxxxxxxxxxxxx",userdata['days'])
    request.session["USERDATA"]=userdata
    return JsonResponse(userdata,safe=False)