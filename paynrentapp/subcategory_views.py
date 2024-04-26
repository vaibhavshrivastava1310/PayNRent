from django.db import connection
from django.shortcuts import render
from django.http.response import JsonResponse
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from paynrentapp.serializers import SubCategorySerializers
from paynrentapp.models import SubCategory
from . import tuple_to_dict
from django.views.decorators.clickjacking import xframe_options_exempt
import os
# Create your views here.
@api_view(['GET','POST','DELETE'])
@xframe_options_exempt
def SubCategoryInterface(request):
    return render(request,'SubCategoryInterface.html')
@api_view(['GET','POST','DELETE'])
@xframe_options_exempt
def SubCategorySubmit(request):
    if (request.method=='POST'):
        try:
            subcategory_serializer = SubCategorySerializers(data=request.data)
            if subcategory_serializer.is_valid():
                subcategory_serializer.save()
                return render(request,'SubCategoryInterface.html',{"message":"Record Submitted"})
        except Exception as error:
            print(error)
            return render(request,'SubCategoryInterface.html',{"message":error})
@api_view(['GET','POST','DELETE'])
@xframe_options_exempt
def DisplaySubCategory(request):
    if request.method=='GET':
        try:
            q="select S.*,(select C.categoryname from paynrentapp_category C where C.id=S.categoryid) as categoryname from paynrentapp_subcategory S"
            # print(q)
            cursor=connection.cursor()
            cursor.execute(q)
            records=tuple_to_dict.ParseDictMultipleRecord(cursor)
            # print('XXXXXXXXXXXXXX',records)
            return render(request,"SubCategoryDisplay.html",{'data':records})
        except Exception as error:
            print('Error:',error)
            return render(request,"SubCategoryDisplay.html",{'message':error})
@api_view(['GET','POST','DELETE'])
@xframe_options_exempt
def DisplaySubCategoryJson(request):
    if request.method=='GET':
        try:
            q="select * from paynrentapp_subcategory where categoryid={0}".format(request.GET['cid'])
            cursor=connection.cursor()
            cursor.execute(q)
            cursor.fetchall
            record=tuple_to_dict.ParseDictMultipleRecord(cursor)
            # print("xxxxxxxxx",record)
            return JsonResponse(record,safe=False)
        except Exception as error:
            print('Error:',error)
            return JsonResponse([],safe=False)
@api_view(['GET','POST','DELETE'])
@xframe_options_exempt
def DisplayBySubId(request):
    if request.method=='GET':
        try:
            q="select S.*,(select C.categoryname from paynrentapp_category C where C.id=S.categoryid) as categoryname from paynrentapp_subcategory S where id={0}".format(request.GET['id'])
            cursor=connection.cursor()
            cursor.execute(q)
            cursor.fetchone
            record=tuple_to_dict.ParseDictSingleRecord(cursor)
            print("xxxxxxxxx",record)
            return render(request,"DisplayBySubId.html",{'data':record})
        except Exception as error:
            print('Error:',error)
            return render(request,"DisplayBySubId.html",{'message':error})
@api_view(['GET','POST','DELETE'])
@xframe_options_exempt
def EditSubCategory(request):
    try:
        if request.method=='GET':
            if(request.GET['btn']=="EDIT"):
                subcategory=SubCategory.objects.get(pk=request.GET['id'])
                subcategory.categoryid=request.GET['categoryid']
                subcategory.companyname=request.GET['companyname']
                subcategory.subcategoryname=request.GET['subcategoryname']
                subcategory.description=request.GET['description']
                subcategory.save()
            else:
                category=SubCategory.objects.get(pk=request.GET['id'])
                category.delete()
        return redirect('/api/subcategorydisplay')
    except Exception as error:
        print('Error',error)
        return render(request,'DisplayBySubId.html',{'message',error})
@api_view(['GET','POST','DELETE'])
@xframe_options_exempt
def DisplaySubCategoryIcon(request):
    try:
        if request.method=='GET':
            return render(request,'DisplayBySubIcon.html',{'data':dict(request.GET)})
    except Exception as error:
        print(error)
        return render(request,'DisplayBySubId.html',{'message':error})
@api_view(['GET','POST','DELETE'])
@xframe_options_exempt
def SubCategory_Save_Icon(request):
    try:
        if request.method=='POST':
            subcategory=SubCategory.objects.get(pk=request.POST['id'])
            subcategory.icon=request.FILES['icon']
            subcategory.save()
            os.remove('D:/djpaynrentapp'+request.POST['oldpic'])
            return redirect('/api/subcategorydisplay')
    except Exception as error:
        print(error)
        return redirect('/api/subcategorydisplay')
