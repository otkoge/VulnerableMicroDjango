from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='sb_admin_start'),
    path(r'containers', views.RunningContainerView.as_view(), name='containers'),
    path(r'images', views.ImagesView.as_view(), name='images'),
    path(r'ifconfig', views.IfconfigView.as_view(), name='ifconfig'),
    path(r'ping', views.PingView.as_view(), name='ping'),
    path(r'route', views.RouteView.as_view(), name='route'),
    path(r'login', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path(r'logout', auth_views.LogoutView.as_view(), name='logout'),
]