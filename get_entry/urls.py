from django.urls import path
from . import views
urlpatterns =[
    path("",views.landingpage,name="landingpage"),path("login",views.landingpage,name="login"),path("get",views.index,name="index"),path("convert",views.con,name="convert"),path("register",views.register,name="register"),
    path("get_details",views.detail,name="detail"),path("logout",views.logout,name="logout")
]