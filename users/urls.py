from django.urls import include, path

from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('users/', views.index.as_view(), name='index'),
    path('users/<int:pk>/', views.oneUser.as_view(), name='one user'),
    path('alphabets/', views.languages, name='languages'),
    path('alphabets/<str:lang>', views.oneAlphabet, name='one alphabet'),
    path('lessons/<str:lang>', views.lessons, name='lessons'),
    path('lesson/<int:lesson_id>', views.lesson, name='lesson'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
