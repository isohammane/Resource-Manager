from django.urls import path 
from .views import Home,delete,Download_func
urlpatterns = [ 
    path("",Home),
    path('delete/<str:code>',delete),
    path('download/<str:code>',Download_func)
    
]