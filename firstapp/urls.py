from django.urls import path
from firstapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('formpage/', views.create, name="form"),
    path('success/', views.success, name="form"),

]
