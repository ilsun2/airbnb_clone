from django.db import models
from django.db.models.deletion import CASCADE
from django_countries.fields import CountryField
from core import models as core_models
from users import models as users_models
class Room(core_models.TimeStampedModel):
    #Rooms model definition

    name = models.CharField(max_length=140)
    description = models.TextField
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    beds = models.IntegerField()
    guests = models.IntegerField()
    bath = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host =  models.ForeignKey(users_models.User, on_delete=CASCADE)

