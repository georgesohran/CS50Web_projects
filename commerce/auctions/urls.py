from django.urls import path

from . import views

urlpatterns = [
    path("<str:category>", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("categories", views.categories, name="categories"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("listings/<int:listing_id>", views.listings, name="listing"),

]
