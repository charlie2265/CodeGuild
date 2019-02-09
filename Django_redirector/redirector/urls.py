from django.urls import path

from .views import index

app_name = 'redirector'
urlpatterns = [
    path('', index, name='index'),
    
] 