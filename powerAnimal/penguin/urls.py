from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("search/", views.search, name="search"),
    path("view/<int:pid>", views.view, name="view"),
    path("checkout/<int:pid>", views.checkout, name="checkout"),
    path("viewall/<str:cat>", views.ViewAll.as_view(), name="viewall"),
]
