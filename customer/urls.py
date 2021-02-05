from django.contrib import admin
from django.urls import path
from customer.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('Order/', Order.as_view(), name='Order'),
    # path('Order/', views.Order, name='Order'),

    path('OrderConfirmation/', OrderConfirmation.as_view(), name='OrderConfirmation'),
    path('OrderPayConfirmation/', OrderPayConfirmation.as_view(), name='OrderPayConfirmation'),
    path('Menu/', Menu.as_view(), name='Menu'),
    path('MenuSearch/', MenuSearch.as_view(), name='MenuSearch'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('accounts/register/', views.registration, name='register'),




    

]