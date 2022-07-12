from django.urls import path
from . import views

app_name = 'afterlogin'
urlpatterns = [
    path('index/', views.Index.as_view(), name='index'),
    path('index/<pk>/', views.CarUpdate.as_view(), name='carupdate')
]
