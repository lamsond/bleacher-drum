from django.forms import ModelForm
from .models import Team, Player, LineupSlot, Game

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['location', 'name', 'abbr']

class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['date', 'team_away', 'team_home', 'runs_away', 'runs_home']





