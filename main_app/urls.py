from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('my_gallery/', views.my_gallery, name='gallery'),
    path('collection', views.collection, name='collection'),
]