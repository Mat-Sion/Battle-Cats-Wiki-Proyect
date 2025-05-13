from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Objective, Effect, Ability
from .forms import ObjectiveForm, EffectForm, AbilityForm

class HomeView(TemplateView):
    template_name = "catspedia/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objectives"] = Objective.objects.all()[:5]
        context["effects"] = Effect.objects.all()[:5]
        context["abilities"] = Ability.objects.all()[:5]
        return context

class SearchView(TemplateView):
    template_name = "catspedia/search_results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("q", "")
        if query:
            objective_results = Objective.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
            effect_results = Effect.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
            ability_results = Ability.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
            context.update({
                "query": query,
                "objective_results": objective_results,
                "effect_results": effect_results,
                "ability_results": ability_results
            })
        return context

# Objective views
class ObjectiveListView(ListView):
    model = Objective
    context_object_name = "objectives"
    template_name = "catspedia/objective_list.html"

class ObjectiveDetailView(DetailView):
    model = Objective
    context_object_name = "objective"
    template_name = "catspedia/objective_detail.html"

class ObjectiveCreateView(CreateView):
    model = Objective
    form_class = ObjectiveForm
    template_name = "catspedia/objective_form.html"

class ObjectiveUpdateView(UpdateView):
    model = Objective
    form_class = ObjectiveForm
    template_name = "catspedia/objective_form.html"

class ObjectiveDeleteView(DeleteView):
    model = Objective
    context_object_name = "objective"
    template_name = "catspedia/objective_confirm_delete.html"
    success_url = reverse_lazy("catspedia:objective-list")

# Effect views
class EffectListView(ListView):
    model = Effect
    context_object_name = "effects"
    template_name = "catspedia/effect_list.html"

class EffectDetailView(DetailView):
    model = Effect
    context_object_name = "effect"
    template_name = "catspedia/effect_detail.html"

class EffectCreateView(CreateView):
    model = Effect
    form_class = EffectForm
    template_name = "catspedia/effect_form.html"

class EffectUpdateView(UpdateView):
    model = Effect
    form_class = EffectForm
    template_name = "catspedia/effect_form.html"

class EffectDeleteView(DeleteView):
    model = Effect
    context_object_name = "effect"
    template_name = "catspedia/effect_confirm_delete.html"
    success_url = reverse_lazy("catspedia:effect-list")

# Ability views
class AbilityListView(ListView):
    model = Ability
    context_object_name = "abilities"
    template_name = "catspedia/ability_list.html"

class AbilityDetailView(DetailView):
    model = Ability
    context_object_name = "ability"
    template_name = "catspedia/ability_detail.html"

class AbilityCreateView(CreateView):
    model = Ability
    form_class = AbilityForm
    template_name = "catspedia/ability_form.html"

class AbilityUpdateView(UpdateView):
    model = Ability
    form_class = AbilityForm
    template_name = "catspedia/ability_form.html"

class AbilityDeleteView(DeleteView):
    model = Ability
    context_object_name = "ability"
    template_name = "catspedia/ability_confirm_delete.html"
    success_url = reverse_lazy("catspedia:ability-list")
