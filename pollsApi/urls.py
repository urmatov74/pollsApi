from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.polls.urls import polls_router
from apps.auth.views import UserRegisterView, LogoutView, LoginView

router = routers.DefaultRouter()
router.registry.extend(polls_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/', include(router.urls)),
    path(r'auth/logout/', LogoutView.as_view(), name='logout'),
    path(r'auth/login/', LoginView.as_view(), name='login'),
    path(r'auth/register/', UserRegisterView.as_view(), name='register'),
    # path(r'auth/login', TokenObtainPairView.as_view(), name='login'),
    # path(r'auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
