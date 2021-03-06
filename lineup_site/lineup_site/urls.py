"""lineup_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path

from lineup_app import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('accounts/', include('django.contrib.auth.urls')),
    path('new_game/', views.new_game),
    path('new_team/', views.new_team),
    path('new_player/', views.new_player),
    path('<int:game_id>/set_lineup/<str:ctx>/', views.set_lineup),
    path('<int:game_id>/set_pitchers/<str:ctx>/', views.set_pitchers),
    path('<int:game_id>/save_lineup/<str:ctx>/', views.save_lineup),
    path('<int:game_id>/save_lineup/pitchers/<str:ctx>', views.save_lineup),
    path('<int:team_id>/view_team/', views.view_team),
    path('<int:player_id>/view_player/', views.view_player),
    path('<int:game_id>/view_lineup/', views.view_lineup),
    path('games/', views.view_games),
    path('teams/', views.view_teams),
    path('players/', views.view_players),
    path('admin/', admin.site.urls),
]
