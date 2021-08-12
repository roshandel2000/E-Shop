from django.urls import path
from .views import index, fun, fun_by_number, days, days_of_week

urlpatterns = [
    path('', days_of_week),
    path('index', index),
    path('<day>', days, name="days_of_the_week"),
    path('<int:num>', fun_by_number),
    path('<str:string>', fun, name="fun")
]