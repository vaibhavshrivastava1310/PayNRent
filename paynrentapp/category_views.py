from django.db import connection
from django.shortcuts import render
from django.http.response import JsonResponse
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from paynrentapp.serializers import CategorySerializers
from paynrentapp.models import Category
from . import tuple_to_dict
from django.views.decorators.clickjacking import xframe_options_exempt
import os
# Create your views here.
@api_view(['GET','POST','DELETE'])
@xframe_options_exempt
def CategoryInterface(request):
    return render(request,'CategoryInterface.html')
@api_view(['GET','POST','DELETE'])
def CategorySubmit(request):
    if (request.method=='POST'):
        try:
            category_serializer = CategorySerializers(data=request.data)
            if category_serializer.is_valid():
                category_serializer.save()
                return render(request,"CategoryInterface.html",{"message":"Record Submitted"})
        except Exception as error:
            print(error)
            return render(request,"CategoryInterface.html",{"message":error})
@api_view(['GET','POST','DELETE'])
@xframe_options_exempt
def DisplayCategory(request):
    if request.method=='GET':
        try:
            list_category=Category.objects.all()
            list_category_serializer=CategorySerializers(list_category,many=True)
            records=tuple_to_dict.ParseDict(list_category_serializer.data)
            # print(records)
            return render(request,"CategoryDisplay.html",{'data':records})
        except Exception as error:
            print('Error:',error)
            return render(request,"CategoryDisplay.html",{'message':error})
@api_view(['GET','POST','DELETE'])
@xframe_options_exempt
def DisplayById(request):
    if request.method=='GET':
        try:
            q="select * from paynrentapp_category where id={0}".format(request.GET['id'])
            cursor=connection.cursor()
            cursor.execute(q)
            cursor.fetchone
            record=tuple_to_dict.ParseDictSingleRecord(cursor)
            # print("xxxxxxxxx",record)
            return render(request,"DisplayById.html",{'data':record})
        except Exception as error:
            print('Error:',error)
            return render(request,"DisplayById.html",{'messagze':error})
@api_view(['GET','POST','DELETE'])
@xframe_options_exempt
def EditCategory(request):
    try:
        if request.method=='GET':
            if(request.GET['btn']=="EDIT"):
                category=Category.objects.get(pk=request.GET['id'])
                category.categoryname=request.GET['categoryname']
                category.description=request.GET['description']
                category.save()
            else:
                category=Category.objects.get(pk=request.GET['id'])
                category.delete()
        return redirect('/api/categorydisplay')
    except Exception as error:
        print('Error',error)
        return render(request,'DisplayById.html',{'message',error})
@api_view(['GET','POST','DELETE'])
@xframe_options_exempt
def DisplayCategoryIcon(request):
    try:
        if request.method=='GET':
            return render(request,'DisplayByIcon.html',{'data':dict(request.GET)})
    except Exception as error:
        print(error)
        return render(request,'DisplayById.html',{'message':error})
@api_view(['GET','POST','DELETE'])
@xframe_options_exempt
def Category_Save_Icon(request):
    try:
        if request.method=='POST':
            category=Category.objects.get(pk=request.POST['id'])
            category.icon=request.FILES['icon']
            category.save()
            os.remove('D:/djpaynrentapp'+request.POST['oldpic'])
            return redirect('/api/categorydisplay')
    except Exception as error:
        print(error)
        return redirect('/api/categorydisplay')
@api_view(['GET','POST','DELETE'])
@xframe_options_exempt
def DisplayCategoryJson(request):
    if request.method=='GET':
        try:
            list_category=Category.objects.all()
            list_category_serializer=CategorySerializers(list_category,many=True)
            records=tuple_to_dict.ParseDict(list_category_serializer.data)
            # print(records)
            return JsonResponse(data=records,safe=False)
        except Exception as error:
            print('Error:',error)
            return render(request,"CategoryInterface.html",{'message':error})
    