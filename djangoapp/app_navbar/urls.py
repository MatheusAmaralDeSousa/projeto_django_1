from django.urls import path
from app_navbar import views

urlpatterns = [
    path('',views.home,name = "home"),
]
