"""pollsApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.polls.urls import polls_router
from apps.auth.views import UserRegisterView, LogoutView, LoginView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

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
