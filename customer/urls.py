from django.contrib import admin
from django.urls import path
from customer.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('Order/', Order.as_view(), name='Order'),
    path('OrderConfirmation/', OrderConfirmation.as_view(), name='OrderConfirmation'),
    path('OrderPayConfirmation/', OrderPayConfirmation.as_view(), name='OrderPayConfirmation'),


    

]