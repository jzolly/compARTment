from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('art_gallery/', views.art_gallery, name='index'),
    path('art/<int:art_id>/', views.art_detail, name='detail'),
    path('art/create/', views.ArtCreate.as_view(), name='art_create'),
    # path('art/<int:pk>/update/', views.ArtUpdate.as_view(), name='art_update'),
    # path('art/<int:pk>/delete/', views.ArtDelete.as_view(), name='art_delete'),
    # path('collection', views.collection, name='collection'),
    path('accounts/signup/', views.signup, name='signup'),
]