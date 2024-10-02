from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
         path('', views.index, name='main'),
         path('about/', views.about, name='about'),
         path('gallery/', views.galery, name='galery'),
         path('contact/', views.contact, name='contact'),
     ]