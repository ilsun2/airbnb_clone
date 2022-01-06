from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django_countries.fields import CountryField
from core import models as core_models
from users import models as users_models


class AbstractItem( core_models.TimeStampedModel):
    
    ''' Abstract Item definition'''

    name = models.CharField(max_length= 80)


    class Meta :
        abstract = True

    
    def __str__(self) :
        return self.name
    
    
class RoomType(AbstractItem):

    class Meta :
        verbose_name = "Room Type"

class Amenity(AbstractItem):

    class Meta :
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    class Meta :
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    class Meta :
        verbose_name = "Hosue Rule"


class Photo(core_models.TimeStampedModel):


    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=CASCADE)

    def __str__(self):
        return self.caption


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
    room_type = models.ManyToManyField(RoomType, blank=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    houserule = models.ManyToManyField(HouseRule, blank=True)
    def __str__(self) :
        return self.name

