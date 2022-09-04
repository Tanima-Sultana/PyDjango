from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# from .models import Meetup

meetups = [{'title':"aa",'slug':"ss",'location':"gg"}]
#Meetup.objects.all()

def index(request):
    return render(request,'meetups/index.html',{
        'meetups':meetups
    })

def meetup_details(request,meetup_slug):
    try:
        selected_meetups = {'title':"aaa",'description':"des"}
        # Meetup.objects.get(slug=meetup_slug)
        return render(request,'meetups/meetup-details.html',{
            'meetup_found':True,
            'meetup_title': selected_meetups.title,
            'meetup_description':selected_meetups.description
        })
    except Exception as exc:
        return render(request,'meetups/meetup-details.html',{
            'meetup_found':False
        })