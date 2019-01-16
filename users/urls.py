from django.urls import path

from . import views


urlpatterns = [
    path('users/', views.index, name='index'),
    path('users/<int:pk>/', views.oneUser, name='one user'),
    path('languages/', views.languages, name='languages')
]
