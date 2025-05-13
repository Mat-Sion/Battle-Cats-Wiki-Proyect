from django.contrib import admin
from .models import Objective, Effect, Ability

@admin.register(Objective)
class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty', 'energy_cost', 'required_level')
    list_filter = ('difficulty', 'required_level')
    search_fields = ('name', 'description')

@admin.register(Effect)
class EffectAdmin(admin.ModelAdmin):
    list_display = ('name', 'effect_type', 'base_power', 'duration', 'proc_chance')
    list_filter = ('effect_type', 'area_of_effect')
    search_fields = ('name', 'description')

@admin.register(Ability)
class AbilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'ability_type', 'energy_cost')
    list_filter = ('ability_type',)
    search_fields = ('name', 'description')
    filter_horizontal = ('effects',)
