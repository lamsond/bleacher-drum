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
from rest_framework import routers

"""
router = routers.DefaultRouter()
router.register(r'teams', views.TeamViewSet)
router.register(r'games', views.GameViewSet)
router.register(r'players', views.PlayerViewSet)
"""

urlpatterns = [
    path('play_ball/', views.play_ball),
    path('new_game/', views.new_game),
    path('new_team/', views.new_team),
    path('<int:game_id>/set_lineup/', views.set_lineup),
    path('<int:game_id>/save_lineup/', views.save_lineup),
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
