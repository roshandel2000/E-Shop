from django.urls import path
from .views import index, fun

urlpatterns = [
    path('index', index),
    path('<string>', fun)
]