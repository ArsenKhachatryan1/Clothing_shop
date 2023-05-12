from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('register/',views.register_request, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  views.activate, name='activate'),
]