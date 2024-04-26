"""djpaynrentapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from paynrentapp import category_views
from paynrentapp import subcategory_views
from paynrentapp import vehicles_views
from paynrentapp import login_view
from paynrentapp import user_view
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/categoryinterface/$',category_views.CategoryInterface),
    re_path(r'^api/categorysubmit',category_views.CategorySubmit),
    re_path(r'^api/categorydisplay/$',category_views.DisplayCategory),
    re_path(r'^api/displaycategorybyid/$',category_views.DisplayById),
    re_path(r'^api/categoryedit',category_views.EditCategory),
    re_path(r'^api/displaycategoryicon/$',category_views.DisplayCategoryIcon),
    re_path(r'^api/displaycategoryjson/$',category_views.DisplayCategoryJson),
    re_path(r'^api/category_save_icon',category_views.Category_Save_Icon),

# ---------------------------------------------------------------------------------------------------------------------------------------

    re_path(r'^api/subcategoryinterface/$',subcategory_views.SubCategoryInterface),
    re_path(r'^api/subcategorysubmit',subcategory_views.SubCategorySubmit),
    re_path(r'^api/subcategorydisplay/$',subcategory_views.DisplaySubCategory),
    re_path(r'^api/displaysubcategorybyid/$',subcategory_views.DisplayBySubId),
    re_path(r'^api/subcategoryedit',subcategory_views.EditSubCategory),
    re_path(r'^api/displaysubcategoryicon/$',subcategory_views.DisplaySubCategoryIcon),
    re_path(r'^api/subcategory_save_icon',subcategory_views.SubCategory_Save_Icon),
    re_path(r'^api/displaysubcategoryjson/$',subcategory_views.DisplaySubCategoryJson),

# -------------------------------------------------------------------------------------------------------------------------------------------


    re_path(r'^api/vehicleinterface/$',vehicles_views.VehicleInterface),
    re_path(r'^api/vehiclesubmit',vehicles_views.VehicleSubmit),
    re_path(r'^api/vehicledisplay/$',vehicles_views.DisplayVehicle),
    re_path(r'^api/displayvehiclebyid/$',vehicles_views.DisplayById),
    re_path(r'^api/vehicleedit/$',vehicles_views.EditVehicle),
    re_path(r'^api/displayvehiclepicture/$',vehicles_views.DisplayVehiclePicture),
    re_path(r'^api/vehicle_save_picture',vehicles_views.Vehicle_Save_Picture),

# ----------------------------------------------------------------------------------------------------------------------------------------------


    re_path(r'^api/loginpage/$',login_view.LoginPage),
    re_path(r'^api/checkadminlogin/$',login_view.CheckAdminLogin),


#-----------------------------------------------------------------------------------------------------------------------------------------------


    re_path(r'^api/indexpage/$',user_view.Home),
    re_path(r'^api/displayvehicleforuser/$',user_view.DisplayVehicleForUser),
    re_path(r'^api/uservehiclelist/$',user_view.PageUserVehicle),
    re_path(r'^api/displayselectedvehicle/$',user_view.DisplaySelectedVehicle),
    re_path(r'^api/showvehiclelist/$',user_view.ShowVehicleList),
    re_path(r'^api/setemailmobile/$',user_view.SetMobileAndEmail),
    re_path(r'^api/modifylocationtime/$',user_view.ModifyLocationTime),
]

