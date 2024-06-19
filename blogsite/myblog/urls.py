from django.urls import path

from .views import (
    home_view, 
    create_view,

)

urlpatterns = [
    path('',home_view , name='home'),
    path('post/' , create_view , name='post'),
    
]

