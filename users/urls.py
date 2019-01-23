from django.urls import include, path

from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('users/', views.users.as_view(), name='users'),
    path('users/<int:pk>/', views.oneUser.as_view(), name='one user'),
    path('alphabets/', views.languages.as_view(), name='languages'),
    path('alphabets/<str:lang>', views.languageByName, name='one alphabet'),
    path('alllessons/', views.allLessons.as_view(), name='all lessons'),
    path('lessons/<str:lang>', views.lessons, name='lessons'),
    path('lesson/<int:lesson_id>', views.lesson, name='lesson'),
    path('questions/', views.questions.as_view(), name='questions'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
