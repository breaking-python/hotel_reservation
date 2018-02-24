from django.urls import path
from .views import *

urlpatterns = [
    path('reserve/<int:id>/', reserve)

]
