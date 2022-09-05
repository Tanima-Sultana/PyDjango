from xml.etree.ElementInclude import include
from django.shortcuts import render, redirect
from .models import Meetup, Participant
from .forms import RegistrationForm

meetups = Meetup.objects.all()

def index(request):
    print(meetups)
    return render(request,'meetups/index.html',{
        'meetups':meetups
    })

def signUp(request,meetup_slug):
    print('in signup')
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request,'meetups/registration-success.html',{
        'organizer_email':meetup.organizer_email
    })

def meetup_details(request,meetup_slug):
    try:
        print(f'meetup slug : {meetup_slug}')
        selected_meetups = Meetup.objects.get(slug=meetup_slug)
        print(f'meetup selected : {selected_meetups}')
        print(f'request method : {request.method}')
        if request.method == 'GET':
            registration_form = RegistrationForm()
            return render(request,'meetups/meetup-details.html',{
                'meetup_found':True,
                'meetup':selected_meetups,
                'form':registration_form
            })
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                print(f'registration_form : {registration_form}')
                user_email = registration_form.cleaned_data['email']
                participant,_ = Participant.objects.get_or_create(email=user_email)
                print(f'participant: {participant}')
                selected_meetups.participants.add(participant)
                print(f'saved selected_meetups : {selected_meetups}')
                return redirect('confirm-registration',meetup_slug=meetup_slug)
            else:
                return render(request,'meetups/meetup-details.html',{
                'meetup_found':True,
                'meetup':selected_meetups,
                'form':registration_form
            })
                

        
            
    except Exception as exc:
        print(exc)
        return render(request,'meetups/meetup-details.html',{
            'meetup_found':False
        })