from django.forms import ModelForm
from .models import Team, Player, LineupSlot

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['location', 'name', 'abbr']





