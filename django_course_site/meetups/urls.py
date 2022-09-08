from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_meetups,name='all-meetup'),
    path('register', views.register,name='register'),
    path('home', views.index,name='home'),
    path('logout',views.logout, name='logout'),
    path('words',views.count_words,name='words'),
    path('words-count',views.get_count_words,name='word-count'),
    path('<slug:meetup_slug>/success/',views.signUp,name='confirm-registration'),
    path('login',views.login,name='login'),
    path('meetup/<slug:meetup_slug>',views.meetup_details,name='meetup-detail'),

]