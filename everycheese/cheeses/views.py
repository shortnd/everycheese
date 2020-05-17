from django.views.generic import ListView, DetailView

from .models import Cheese


class CheeseList(ListView):
    model = Cheese


class CheeseDetailView(DetailView):
    model = Cheese
