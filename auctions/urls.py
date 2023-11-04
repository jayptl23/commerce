from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_listing_view, name="create"),
    path("categories", views.categories, name="categories"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("<int:category>/listings", views.listings_by_category, name="listings_by_category"),
    path("add-to-watchlist/<int:user_id>/<int:listing_id>", views.add_to_watchlist, name="add_to_watchlist"),
    path("remove-from-watchlist/<int:user_id>/<int:listing_id>", views.remove_from_watchlist, name="remove_from_watchlist"),
    path("watchlist/<int:user_id>", views.watchlist, name="watchlist")
]
