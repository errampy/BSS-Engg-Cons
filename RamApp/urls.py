from django.urls import path
from RamApp import views
urlpatterns=[
    path('',views.home,name='home'),
]