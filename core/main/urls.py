from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.products, name='products'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    # path('login/', views.login_request, name='login'),
    # path('register/',views.register_request, name='register'),
    # path('logout', views.logout_request, name='logout'),
    path('product/<int:id>/', views.index_detail, name='index_detail')
]