from django.urls import path
from . import views


urlpatterns = [
    path('',views.Hello, name="home-page"),
    path('add', views.add, name="add")
]