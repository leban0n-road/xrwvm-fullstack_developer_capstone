# Uncomment the required imports before adding the code

# from django.shortcuts import render
# from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404, render, redirect
# from django.contrib.auth import logout
# from django.contrib import messages
# from datetime import datetime
from .restapis import get_request, analyze_review_sentiments, post_review
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .models import CarMake, CarModel
from .populate import initiate  # If you use auto-population
# from .populate import initiate


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("userName")
        password = data.get("password")
        print(f"Attempting login for {username} with password {password}")  # Debug line
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"userName": username, "status": True})
        else:
            print("Authentication failed")  # Debug line
            return JsonResponse({"status": False})

# Create a `logout_request` view to handle sign out request
def logout_user(request):
    logout(request)
    return JsonResponse({"userName": "", "status": True})



# Create a `registration` view to handle sign up request
# @csrf_exempt
def register_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get("userName")
        password = data.get("password")
        first_name = data.get("firstName")
        last_name = data.get("lastName")
        email = data.get("email")

        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Already Registered"})

        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
        login(request, user)
        return JsonResponse({"userName": username, "status": True})

def get_cars(request):
    if CarMake.objects.count() == 0:
        initiate()
    car_models = CarModel.objects.select_related('car_make')
    cars = [{"CarModel": model.name, "CarMake": model.car_make.name} for model in car_models]
    return JsonResponse({"CarModels": cars})

def home(request):
    return HttpResponse("✅ Django is running successfully.")


# # Update the `get_dealerships` view to render the index page with
# a list of dealerships
def get_dealerships(request, state="All"):
    if state == "All":
        endpoint = "/fetchDealers"
    else:
        endpoint = f"/fetchDealers/{state}"
    dealerships = get_request(endpoint)
    return JsonResponse({"status": 200, "dealers": dealerships})


# Create a `get_dealer_reviews` view to render the reviews of a dealer
def get_dealer_reviews(request, dealer_id):
    if dealer_id:
        endpoint = f"/fetchReviews/dealer/{dealer_id}"
        reviews = get_request(endpoint)
        for review_detail in reviews:
            response = analyze_review_sentiments(review_detail.get("review", ""))
            review_detail["sentiment"] = response.get("sentiment", "neutral")
        return JsonResponse({"status": 200, "reviews": reviews})
    else:
        return JsonResponse({"status": 400, "message": "Bad Request"})


# Create a `get_dealer_details` view to render the dealer details
def get_dealer_details(request, dealer_id):
    if dealer_id:
        endpoint = f"/fetchDealer/{dealer_id}"
        dealership = get_request(endpoint)
        return JsonResponse({"status": 200, "dealer": dealership})
    else:
        return JsonResponse({"status": 400, "message": "Bad Request"})


# Create a `add_review` view to submit a review
def add_review(request):
    if request.user.is_authenticated:
        data = json.loads(request.body)
        try:
            response = post_review(data)
            return JsonResponse({"status": 200})
        except:
            return JsonResponse({"status": 401, "message": "Error in posting review"})
    else:
        return JsonResponse({"status": 403, "message": "Unauthorized"})

