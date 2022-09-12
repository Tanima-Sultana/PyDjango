import email
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Meetup, Participant, Profile
from .forms import RegistrationForm, UserForm,ProfileForm
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from django.core.mail import send_mail

from meetups import forms
#from myproject.settings import EMAIL_HOST_USER



meetups = Meetup.objects.all()


def all_meetups(request):
    print(meetups)
    return render(request,'meetups/all_meetups.html',{
        'meetups':meetups
    })


def index(request):
    return render(request,'meetups/index.html')


def count_words(request):
    print('in count words function')
    return render(request,'meetups/wordcount.html')

def get_count_words(request):
    text = request.POST['words']
    text_length = len(text.split())
    print(f'text in testarea : {text}')
    print(f'text in testarea : {text_length}')
    if text_length < 10 :
        return HttpResponse('heyy Please briefly describe your thoughts with more words')
    return render(request,'meetups/wordcount.html')   # same html file will be loaded here A EXPERIMENT



def signUp(request,meetup_slug):
    print('in signup')
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request,'meetups/registration-success.html',{
        'organizer_email':meetup.organizer_email
    })

def register(request):
    print('in register user')
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2 :
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
            else :
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password not matched!')
            return redirect('register')



    return render(request,'meetups/register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            print('user logged in successfully')
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect('login')
    return render(request,'meetups/login.html')


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


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'meetups/profile-update.html'

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        try:
            profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)
            
        except:
            profile_form = ProfileForm(post_data, file_data, instance=Profile(user_id=request.user.id))

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'meetups/profile.html'


