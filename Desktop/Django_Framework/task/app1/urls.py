from django.urls import path
from .views import *
urlpatterns=[
path('welcome1/',welcome1, name="welcome1"),  # CORRECT
]
