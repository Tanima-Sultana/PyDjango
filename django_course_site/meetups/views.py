from http.client import HTTPResponse
from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup
from .forms import RegistrationForm

meetups = Meetup.objects.all()

def index(request):
    print(meetups)
    return render(request,'meetups/index.html',{
        'meetups':meetups
    })

def meetup_details(request,meetup_slug):
    try:
        selected_meetups = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(Request.POST)
            if registration_form.is_valid():
                participant = registration_form.save()
                selected_meetups.participants.add(participant)
                

        return render(request,'meetups/meetup-details.html',{
                'meetup_found':True,
                'meetup':selected_meetups,
                'form':registration_form
            })
            
    except Exception as exc:
        return render(request,'meetups/meetup-details.html',{
            'meetup_found':False
        })