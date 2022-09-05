from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='all-meetup'),
    path('<slug:meetup_slug>',views.meetup_details,name='meetup-detail'),
    path('<slug:meetup_slug>/success/',views.signUp,name='confirm-registration')
]