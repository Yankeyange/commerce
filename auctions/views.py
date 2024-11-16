from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import AuctionsForm

from .models import User, Auctions, Bids, Comment


def index(request):
    auctions = Auctions.objects.all()
    context = {'auctions': auctions}
    return render(request, "auctions/index.html", context)


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


def CreateListing(request):
  
  if request.method != 'POST':
    # form va iriter de TopicForm
    form = AuctionsForm()
  
  else:
    form = AuctionsForm(data=request.POST)

    if form.is_valid():
      # si le formulaire est valid on sauvegarde
      form.save()
      # et on retourne à topics
      return redirect('index')
  context = {'form':form}

  return render(request, "CreateListing.html", context)


def Watchlist(request):
    return render(request, "Watchlist.html")

def Categories(request):
    return render(request, "Categories.html")