from django.db import models
from django.core import serializers
from django.utils.timezone import now
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
from .models import CarDealer, CarMake, CarModel, DealerReview
# from .restapis import related methods
from .restapis import get_dealers_from_cf, get_dealer_by_id_from_cf, get_dealer_reviews_from_cf, get_request
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import uuid
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
def about(request):
    context={}
    if request.method== 'GET':
        return render (request, 'djangoapp/about.html', context)


# Create a `contact` view to return a static contact page
def contact(request):
    context={}
    if request.method=='GET':
        return render(request, 'djangoapp/contact.html', context)

# Create a `login_request` view to handle sign in request
# def login_request(request):
# ...

# Create a `logout_request` view to handle sign out request
# def logout_request(request):
# ...

# Create a `registration_request` view to handle sign up request
# def registration_request(request):
# ...

# Update the `get_dealerships` view to render the index page with a list of dealerships
#def get_dealerships(request):
#    context = {}
#    if request.method == "GET":
#        return render(request, 'djangoapp/index.html', context)

def get_dealerships(request):
    if request.method == "GET":
        url = "https://us-south.functions.appdomain.cloud/api/v1/web/ec674888-06e4-4ff4-8ddb-ecc6db00b252/dealership-package/get-dealership"
        # Get dealers from the URL
        dealerships = get_dealers_from_cf(url)
        context = {}
        context["dealership_list"] = dealerships
        
        return render (request, 'djangoapp/index.html', context)
        # Concat all dealer's short name
        #dealer_names = ' '.join([dealer.short_name for dealer in dealerships])
        # Return a list of dealer short name
        #return HttpResponse(dealer_names)

# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...
def get_dealer_details(request, id):
    if request.method == "GET":
        context = {}
        dealer_url = "https://us-south.functions.appdomain.cloud/api/v1/web/ec674888-06e4-4ff4-8ddb-ecc6db00b252/dealership-package/get-dealership"
        dealer = get_dealer_by_id_from_cf(dealer_url, id=id)
        context["dealer"] = dealer
    
        review_url = "https://us-south.functions.appdomain.cloud/api/v1/web/ec674888-06e4-4ff4-8ddb-ecc6db00b252/dealership-package/get-review"
        reviews = get_dealer_reviews_from_cf(review_url, id=id)
        context["reviews"] = reviews
        
        return render(request, 'djangoapp/dealer_details.html', context)

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

