from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    GANDER_MALE = "Male"
    GANDER_FEMAEL = "Female"
    GANDER_OTHER = "Other"

    GANDER_CHOICE = (
         (GANDER_MALE , "Male"),
    (GANDER_FEMAEL , "Female"),
    (GANDER_OTHER , "Other")
    )

    bio = models.TextField(default="",null=True,blank=True)
    avatar = models.ImageField(null = True,blank = True)
    birthday = models.DateField(null = True,blank = True)
    gander = models.CharField(choices=GANDER_CHOICE,max_length=10,null = True,blank = True)
    