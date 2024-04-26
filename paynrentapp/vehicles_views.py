from django.db import connection
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from paynrentapp.serializers import VehiclesSerializers
from paynrentapp.models import Vehicles
from . import tuple_to_dict
from django.views.decorators.clickjacking import xframe_options_exempt
import os
@api_view(['GET','POST','DELETE'])
@xframe_options_exempt
def VehicleInterface(request):
    return render(request,'VehicleInterface.html')
@api_view(['GET','POST','DELETE'])
@xframe_options_exempt
def VehicleSubmit(request):
    if (request.method=='POST'):
        try:
            vehicle_serializer = VehiclesSerializers(data=request.data)
            if vehicle_serializer.is_valid():
                vehicle_serializer.save()
                return render(request,'VehicleInterface.html',{"message":"Record Submitted"})
        except Exception as error:
            print(error)
            return render(request,'VehicleInterface.html',{"message":error})
@api_view(['GET','POST','DELETE'])
@xframe_options_exempt
def DisplayVehicle(request):
    if request.method=='GET':
        try:
          q="select V.*,(select C.categoryname from paynrentapp_category C where C.id=V.categoryid) as categoryname,(select S.subcategoryname from paynrentapp_subcategory S where S.id=V.subcategoryid) as subcategoryname from paynrentapp_vehicles V" 
        #   print(q)
          cursor=connection.cursor()
          cursor.execute(q)
          records=tuple_to_dict.ParseDictMultipleRecord(cursor)
          print('XXXXXXXXXXX',records)
          return render(request,"VehicleDisplay.html",{'data':records}) 
        except Exception as error:
            print('Error:',error)
            return render(request,"VehicleDisplay.html",{'message':error})
@api_view(['GET','POST','DELETE'])
@xframe_options_exempt
def DisplayById(request):
    if request.method=='GET':
        try:
            q="select V.*,(select C.categoryname from paynrentapp_category C where C.id=V.categoryid) as categoryname,(select S.subcategoryname from paynrentapp_subcategory S where S.id=V.subcategoryid) as subcategoryname from paynrentapp_vehicles V where id={0}".format(request.GET['id'])
            cursor=connection.cursor()
            cursor.execute(q)
            cursor.fetchone
            record=tuple_to_dict.ParseDictSingleRecord(cursor)
            # print("xxxxxxxxx",record)
            if(record):
                status=False
                if(record['insured']=='Yes'):
                    status=True
                else:
                    status=False
                if(record['transmissiontype']=='Automatic'):
                    status=True
                else:
                    status=False
                if(record['fueltype']=='Petrol'):
                    status=True
                elif(record['fueltype']=='Diesel'):
                    status=True
                else:
                    status=False
                return render(request,"DisplayByVehicleId.html",{'data':record})
            return render(request,"DisplayByVehicleId.html",{'data':[]})
        except Exception as error:
            print('Error:',error)
            return render(request,"DisplayByVehicleId.html",{'message':error})
@api_view(['GET','POST','DELETE'])
@xframe_options_exempt
def EditVehicle(request):
    try:
        request.session.flush()
        if request.method=='GET':
            if(request.GET['btn']=="EDIT"):
                vehicles=Vehicles.objects.get(pk=request.GET['id'])
                vehicles.categoryid=request.GET['categoryid']
                vehicles.companyname=request.GET['companyname']
                vehicles.subcategoryid=request.GET['subcategoryid']
                vehicles.variant=request.GET['varient']
                vehicles.modelyear=request.GET['modelyear']
                vehicles.price=request.GET['price']
                vehicles.insured=request.GET['insured']
                vehicles.registrationno=request.GET['registrationno']
                vehicles.ownername=request.GET['ownername']
                vehicles.mobileno=request.GET['mobileno']
                vehicles.fueltype=request.GET['fueltype']
                vehicles.noofseats=request.GET['noofseats']
                vehicles.transmissiontype=request.GET['transmissiontype']
                vehicles.save()
            else:
                vehicles=Vehicles.objects.get(pk=request.GET['id'])
                vehicles.delete()
        return redirect('/api/vehicledisplay')
    except Exception as error:
        print('Error',error)
        return render(request,'DisplayByVehicleId.html',{'message',error})
@api_view(['GET','POST','DELETE'])
@xframe_options_exempt
def DisplayVehiclePicture(request):
    try:
        if request.method=='GET':
            return render(request,'DisplayByVehiclePicture.html',{'data':dict(request.GET)})
    except Exception as error:
        print(error)
        return render(request,'DisplayByVehicleId.html',{'message':error})
@api_view(['GET','POST','DELETE'])
@xframe_options_exempt
def Vehicle_Save_Picture(request):
    try:
        if request.method=='POST':
            vehicles=Vehicles.objects.get(pk=request.POST['id'])
            vehicles.picture=request.FILES['picture']
            vehicles.save()
            os.remove('D:/djpaynrentapp'+request.POST['oldpic'])
            return redirect('/api/vehicledisplay')
    except Exception as error:
        print(error)
        return redirect('/api/vehicledisplay')