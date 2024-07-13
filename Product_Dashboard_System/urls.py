from django.urls import path
from Product_Dashboard_System import views


app_name = 'product_dashboard'

urlpatterns = [
    path('', views.home_view.home, name='test'),
]
