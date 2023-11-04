from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from auctions.forms import ListingForm

from .models import User, Listing, Category


def index(request):
    listings = Listing.objects.all()
    return render(request, "auctions/index.html", {"listings": listings})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create_listing_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/create-listing.html", {"form": form})
    else:
        return render(request, "auctions/create-listing.html", {"form": ListingForm()})

def categories(request):
    categories = Category.objects.all()
    return render(request, "auctions/categories.html", {"categories": categories })

def listings_by_category(request, category):
    listings = Listing.objects.filter(category=category)
    return render(request, "auctions/listings-by-category.html", { "listings": listings })

def listing(request, id):
    listing = Listing.objects.filter(pk=id).first()

    if not request.user.is_authenticated:
        return render(request, "auctions/listing-details.html", { "listing": listing })
    
    user = User.objects.get(username=request.user.username)
    has_listing_in_watchlist = user.watchlist.filter(pk=id).exists()
    print("has listing in watchlist?", has_listing_in_watchlist)

    return render(request, "auctions/listing-details.html", { "listing": listing, "has_listing_in_watchlist": has_listing_in_watchlist })

def add_to_watchlist(request, user_id, listing_id):
    if request.user.is_authenticated:
        user = User.objects.get(pk=int(user_id))
        listing = Listing.objects.get(pk=int(listing_id))
        user.watchlist.add(listing)
        return HttpResponseRedirect(reverse("listing", kwargs={ "id": listing.id }))
    return redirect("index")

def remove_from_watchlist(request, user_id, listing_id):
    if request.user.is_authenticated:
        user = User.objects.get(pk=int(user_id))
        listing = Listing.objects.get(pk=int(listing_id))
        user.watchlist.remove(listing)
        return HttpResponseRedirect(reverse("listing", kwargs={ "id": listing.id }))
    return redirect("index")

def watchlist(request, user_id):
    if request.user.is_authenticated:
        user = User.objects.get(pk=int(user_id))
        listings = user.watchlist.all()
        
    return render(request, "auctions/watchlist.html", { "listings": listings })