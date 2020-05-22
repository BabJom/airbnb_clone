from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):
    """ abstract Item """

    name = models.CharField(max_length=40)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """ Room Type Object Definition"""

    pass


class Amenity(AbstractItem):
    """ Amenity Model Definition """

    pass


class Facility(AbstractItem):
    """Facility Model Definition """

    pass


class HouseRule(AbstractItem):
    """HouseRule Model Definition"""

    pass


class Room(core_models.TimeStampedModel):
    """ Room Model Defintion """

    name = models.CharField(max_length=140)
    discription = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=100)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_books = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    # host 는 유저와 연동
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    houserules = models.ManyToManyField(HouseRule, blank=True)

    def __str__(self):
        return self.name
