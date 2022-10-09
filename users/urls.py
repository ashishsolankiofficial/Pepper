from django.urls import path
from users.views import RegisterView, LoginView, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [

    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', RegisterView.as_view()),
    path('user-login/', LoginView.as_view())
]
