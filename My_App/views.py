from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "dash.html")


def upload(request):
    return render(request, "upload.html")


def search(request):
    return render(request, "search.html")

def venue(request):
    return render(request, "venue.html")

def venuedetail(request):
    return render(request, "venuedetail.html")
