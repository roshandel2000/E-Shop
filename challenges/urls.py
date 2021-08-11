from django.urls import path
from .views import index, fun, fun_by_number

urlpatterns = [
    path('index', index),
    path('<int:num>', fun_by_number),
    path('<str:string>', fun, name="fun")
]