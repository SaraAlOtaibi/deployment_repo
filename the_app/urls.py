from django.urls import path     
from . import views
from wall_app import views as wall_app_views

app_name = 'the_app'
urlpatterns = [
    path('', views.index, name='home'),
    path('register', views.register),
    path('success', views.loged_in),
    path('login_page', views.login_temp),
    path('login', views.login),
    path('logout', views.logout, name='logout')
]