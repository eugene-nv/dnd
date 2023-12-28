from django.views.generic import ListView, DetailView

from bestiary.models import Bestiary


class CreaturesViews(ListView):
    template_name = 'bestiary/bestiary.html'
    model = Bestiary
    context_object_name = 'bestiary'


class ShowCreature(DetailView):
    model = Bestiary
    template_name = 'bestiary/creature_card.html'
    context_object_name = 'creature'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
