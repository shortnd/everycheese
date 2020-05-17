from django.views.generic import ListView

from .models import Cheese


class CheeseList(ListView):
    model = Cheese
