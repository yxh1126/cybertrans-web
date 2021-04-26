from django.urls import path
from rango import views

app_name = 'rango_app'
urlpatterns = [
    path('', views.index, name='index'),
]
