from django.urls import path
from .views import *
urlpatterns=[
    path('',book),
    path('all/',book2)
]
