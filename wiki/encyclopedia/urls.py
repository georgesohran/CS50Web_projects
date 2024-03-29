from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new_page", views.create_new_page, name="new_page"),
    path("edit_page/<str:name>", views.edit_page, name="edit_page"),
    path("<str:name>", views.entry, name="entry"),
]
