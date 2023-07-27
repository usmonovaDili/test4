from django.urls import path
from .views import *

urlpatterns=[
    path('',NewsPageView.as_view(), name='homepage'),
    path('text/',TextPageview.as_view(), name='textpage')
]
