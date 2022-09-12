from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)


    def __str__(self):
        return f'{self.name} - ({self.address})'


class Participant(models.Model):
    email = models.EmailField(unique=True)


    def __str__(self):
        return self.email



class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant ,blank=True,null=True)
    organizer_email = models.EmailField()
    date = models.DateField()


    def __str__(self):
        return f'{self.title} - {self.slug}'

    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=12,blank=True)
    birth_date = models.DateField(null=True,blank=True,)
    profile_image = models.ImageField(default='images/default.png',upload_to='users',null=True,blank = True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'