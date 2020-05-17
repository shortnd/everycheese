from django.urls import path
from . import views

app_name = "cheese"

urlpatterns = [
    path(
      route='',
      view=views.CheeseList.as_view(),
      name='list'
    )
]
