from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('home_1',views.home_1, name='home-1'),
    path('function_1',views.function_1, name='function-1'),
    
]
