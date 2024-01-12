"""
URL configuration for mybestgames project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from games import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('create/', views.game_create, name='game_create'),
    path('<int:id>/', views.game_detail, name='game_detail'),
    path('<int:id>/update/', views.game_update, name='game_update'),
    path('<int:id>/delete/', views.game_delete, name='game_delete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

