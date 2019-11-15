from django.urls import path
from firstapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('formpage/', views.form_view, name="form"),

]
