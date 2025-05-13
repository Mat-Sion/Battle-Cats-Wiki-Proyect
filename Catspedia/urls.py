from django.urls import path
from .views import (
    HomeView,
    SearchView,
    ObjectiveListView,
    ObjectiveDetailView,
    ObjectiveCreateView,
    ObjectiveUpdateView,
    ObjectiveDeleteView,
    EffectListView,
    EffectDetailView,
    EffectCreateView,
    EffectUpdateView,
    EffectDeleteView,
    AbilityListView,
    AbilityDetailView,
    AbilityCreateView,
    AbilityUpdateView,
    AbilityDeleteView,
)

app_name = "catspedia"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("search/", SearchView.as_view(), name="search"),
    
    # Objective URLs
    path("objectives/", ObjectiveListView.as_view(), name="objective-list"),
    path("objective/<int:pk>/", ObjectiveDetailView.as_view(), name="objective-detail"),
    path("objective/new/", ObjectiveCreateView.as_view(), name="objective-create"),
    path("objective/<int:pk>/edit/", ObjectiveUpdateView.as_view(), name="objective-update"),
    path("objective/<int:pk>/delete/", ObjectiveDeleteView.as_view(), name="objective-delete"),
    
    # Effect URLs
    path("effects/", EffectListView.as_view(), name="effect-list"),
    path("effect/<int:pk>/", EffectDetailView.as_view(), name="effect-detail"),
    path("effect/new/", EffectCreateView.as_view(), name="effect-create"),
    path("effect/<int:pk>/edit/", EffectUpdateView.as_view(), name="effect-update"),
    path("effect/<int:pk>/delete/", EffectDeleteView.as_view(), name="effect-delete"),
    
    # Ability URLs
    path("abilities/", AbilityListView.as_view(), name="ability-list"),
    path("ability/<int:pk>/", AbilityDetailView.as_view(), name="ability-detail"),
    path("ability/new/", AbilityCreateView.as_view(), name="ability-create"),
    path("ability/<int:pk>/edit/", AbilityUpdateView.as_view(), name="ability-update"),
    path("ability/<int:pk>/delete/", AbilityDeleteView.as_view(), name="ability-delete"),
]
