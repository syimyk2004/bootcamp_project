from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.HoumeListView.as_view(), name='home'),
    path('single/', views.SingleListView.as_view(), name='single'),
    path('movie/', views.MovieListView.as_view(),  name='movie')
]