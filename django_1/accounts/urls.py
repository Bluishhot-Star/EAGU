from django.urls import path
from .views import *

urlpatterns = [
    path(r'^signup/$', signup, name='signup'),
]