from .models import Team, Player, LineupSlot, Game
from rest_framework import serializers

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('location', 'name', 'abbr')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('name', 'num', 'team')

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('team_home', 'team_away', 'runs_home', 'runs_away', 'date')


