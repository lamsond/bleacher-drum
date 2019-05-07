from django.forms import ModelForm
from .models import Team, Player, LineupSlot, Game

from django.forms.widgets import SelectDateWidget

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['location', 'name', 'abbr']

class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['date', 'team_away', 'team_home', 'runs_away', 'runs_home']
        widgets = {
                'date': SelectDateWidget
                }

class LineupForm(ModelForm):
    class Meta:
        model = LineupSlot
        fields = ['game', 'player', 'num', 'pos', 'starter']


