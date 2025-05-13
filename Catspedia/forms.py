from django import forms
from django.core.exceptions import ValidationError
from .models import Objective, Effect, Ability

class ObjectiveForm(forms.ModelForm):
    class Meta:
        model = Objective
        fields = [
            "name", "description", "difficulty", "energy_cost",
            "rewards", "required_level", "enemy_types"
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "difficulty": forms.Select(attrs={"class": "form-select"}),
            "energy_cost": forms.NumberInput(attrs={"class": "form-control", "min": "0"}),
            "rewards": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": '''{"xp": 100, "items": ["potion", "gold"]}'''
            }),
            "required_level": forms.NumberInput(attrs={"class": "form-control", "min": "1"}),
            "enemy_types": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": '''["red", "floating", "black"]'''
            })
        }

class EffectForm(forms.ModelForm):
    class Meta:
        model = Effect
        fields = [
            "name", "description", "effect_type", "base_power",
            "duration", "cooldown", "area_of_effect", "proc_chance"
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "effect_type": forms.Select(attrs={"class": "form-select"}),
            "base_power": forms.NumberInput(attrs={"class": "form-control", "min": "0.1", "step": "0.1"}),
            "duration": forms.NumberInput(attrs={"class": "form-control", "min": "1"}),
            "cooldown": forms.NumberInput(attrs={"class": "form-control", "min": "0"}),
            "area_of_effect": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "proc_chance": forms.NumberInput(attrs={
                "class": "form-control",
                "min": "0",
                "max": "100",
                "step": "1"
            })
        }

class AbilityForm(forms.ModelForm):
    class Meta:
        model = Ability
        fields = [
            "name", "description", "effects", "ability_type",
            "target_traits", "requirements", "energy_cost"
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "effects": forms.SelectMultiple(attrs={"class": "form-select"}),
            "ability_type": forms.Select(attrs={"class": "form-select"}),
            "target_traits": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": '''["red", "floating", "black"]'''
            }),
            "requirements": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": '''{"level": 5, "items": ["special_orb"]}'''
            }),
            "energy_cost": forms.NumberInput(attrs={"class": "form-control", "min": "0"})
        }
