from django.urls import path
from . import views

app_name = 'bootsrap'

urlpatterns = [
    path('',views.index,name='index'),
]
