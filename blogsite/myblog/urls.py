from django.urls import path

from .views import (
    home_view, 
    create_view,
    detail_view,
    add_comment,
    search_view,
    update_view,
)

urlpatterns = [
    path('', home_view, name='home'),
    path('post/', create_view, name='post'),
    path('post/<int:id>',update_view,name='update'),
    path('search/', search_view, name='search'),
    path('post/<int:id>/', detail_view, name='detail'),
    path('comment/<int:post_id>/', add_comment, name='add_comment'),
]

