from django.http.response import HttpResponse
from django.shortcuts import render
from app_rooms.models import Room

# Create your views here.

def home(request):
    return render(request, 'app_general/home.html')

def about(request):
    return render(request, 'app_general/about.html')

def subscription(request):
    all_rooms = Room.objects.all()
    context = {'rooms': all_rooms}
    return render(request, 'app_general/subscription_form.html', context)

def subscription_thankyou(request):
    return render(request, 'app_general/subscription_thankyou.html')