from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_meetups,name='all-meetup'),
    path('home', views.index,name='all-meetup'),
    path('words',views.count_words,name='words'),
    path('words-count',views.get_count_words,name='word-count'),
    path('<slug:meetup_slug>',views.meetup_details,name='meetup-detail'),
    path('<slug:meetup_slug>/success/',views.signUp,name='confirm-registration')
]