from django.urls import path
from firstapp import views


urlpatterns = [
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),

]