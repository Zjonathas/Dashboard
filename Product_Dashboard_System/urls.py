from django.urls import path
from Product_Dashboard_System.views import first_view


app_name = 'product_dashboard'

urlpatterns = [
    path('', first_view, name='test')
]
