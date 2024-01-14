from django.urls import path
from .views import my_view

app_name = 'myapp'

urlpatterns = [
    path('my-view/', my_view, name='my_view')
]