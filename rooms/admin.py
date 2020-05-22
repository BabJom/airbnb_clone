from django.contrib import admin
from . import models

# from core import models as core_models


@admin.register(models.RoomType)
class ItemAdmin(admin.ModelAdmin):
    """ add item in roomType"""

    pass


@admin.register(models.Amenity)
class ItemAdmin(admin.ModelAdmin):
    """ add item in Amenity"""

    pass


@admin.register(models.Facility)
class ItemAdmin(admin.ModelAdmin):
    """ add item in Facility"""

    pass


@admin.register(models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ add item in HouseRule"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin """

    readonly_fields = ("updated", "created")
    pass
