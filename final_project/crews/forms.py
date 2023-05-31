from django import forms
from django.forms import ModelForm
from crews.models import Crew, Island, Has

class CrewForm(ModelForm):
    class Meta:
        model = Crew
        fields = ['crew_name', 'crew_pic']

class IslandForm(ModelForm):
    class Meta:
        model = Island
        fields = ['island_name', 'island_region', 'island_pic']

class HasForm(ModelForm):
    class Meta:
        model = Has
        fields = ['island']