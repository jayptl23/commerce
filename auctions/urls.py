from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_listing_view, name="create"),
    path("categories", views.categories, name="categories"),
    path("<str:category>/listings", views.listings_by_category, name="listings_by_category")
]
