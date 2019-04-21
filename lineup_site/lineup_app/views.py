from django.shortcuts import render
from django.http import HttpResponse

from .models import Game, LineupSlot, Player, Team
from rest_framework import viewsets
from .serializers import GameSerializer, PlayerSerializer, TeamSerializer

class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows games to be viewed or edited
    """
    queryset = Game.objects.all().order_by('-date')
    serializer_class = GameSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows players to be viewed or edited
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed or edited
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

def new_game(request):
    return render(request, 'lineup_app/new_game.html')

def set_lineup(request, game_id):
    return HttpResponse("<h1>Coming soon...</h1>")


