# example/urls.py
from django.urls import path

from example.views import index


urlpatterns = [
    # path('', index),
    path('get', index, name='sample_get_api'),
]