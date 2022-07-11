from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('art_gallery/', views.art_gallery, name='index'),
    path('art/<int:art_id>/', views.art_detail, name='detail'),
    # path('collection', views.collection, name='collection'),
]