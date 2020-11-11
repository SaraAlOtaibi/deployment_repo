from django.urls import path     
from . import views
app_name = 'wall_app'
urlpatterns = [
    path('', views.wall, name='wall'),
    path('/post_msg', views.post_msg, name='post_msg'),
    path('/post_comment', views.post_comment, name='post_comment'),
    path('/delete_msg', views.delete_msg, name='delete_msg'),
]