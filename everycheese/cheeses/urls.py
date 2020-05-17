from django.urls import path
from . import views

app_name = "cheese"

urlpatterns = [
    path(route="", view=views.CheeseList.as_view(), name="list"),
    path(route="add/", view=views.CheeseCreateView.as_view(), name="add",),
    path(route="<slug:slug>/", view=views.CheeseDetailView.as_view(), name="detail",),
]
