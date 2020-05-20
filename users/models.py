from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    """ Custom User Model """

    GENDER_MALE = "MALE"
    GENDER_FEMALE = "FEMALE"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    )

    LANGUAGE_KOREAN = "KOR"
    LANGUAGE_ENGLISH = "ENG"
    LANGUAGE_OTHER = "OTH"

    LANGUAGE_CHOICES = (
        (LANGUAGE_KOREAN, "KOR"),
        (LANGUAGE_ENGLISH, "ENG"),
        (LANGUAGE_OTHER, "OTH"),
    )

    CURRENCY_USD = "USD"
    CURRENCY_WON = "WON"

    CURRENCY_CHOICES = (
        (CURRENCY_WON, "WON"),
        (CURRENCY_USD, "USD"),
    )
    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, default=GENDER_MALE, null=True
    )
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=10, default=LANGUAGE_OTHER, null=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, default=CURRENCY_WON, null=True
    )

    superhost = models.BooleanField(default=False, blank=True)
