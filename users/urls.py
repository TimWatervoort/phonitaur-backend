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
    path('language/<int:pk>', views.oneLanguage.as_view(), name='one language'),
    path('alphabets/<str:lang>', views.languageByName, name='one alphabet'),
    path('lessons/', views.allLessons.as_view(), name='all lessons'),
    path('lessons/<str:lang>', views.lessons, name='lessons'),
    path('lesson/<int:pk>', views.oneLesson.as_view(), name='lesson'),
    path('questions/', views.questions.as_view(), name='questions'),
    path('questions/<int:pk>', views.oneQuestion.as_view(), name='one question'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
