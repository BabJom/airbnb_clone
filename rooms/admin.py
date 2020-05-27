from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition"""

    fieldsets = (
        ("Space", {"fields": ("guests", "beds", "bedrooms", "bathrooms",)},),
        ("Basic Info", {"fields": ("name", "description", "address", "price",)}),
        ("Times", {"fields": ("check_in", "check_out", "instant_books",)}),
        (
            "More About the Spaces",
            {"fields": ("amenities", "facilities", "house_rule",)},
        ),
        ("Last Details", {"classes": ("collapse",), "fields": ("host",)}),
    )
    ordering = (
        "name",
        "price",
    )
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "bathrooms",
        "check_in",
        "check_out",
        "instant_books",
        "count_amenities",
    )
    list_filter = (
        "host__superhost",
        "instant_books",
        "room_type",
        "amenities",
        "facilities",
        "house_rule",
        "city",
        "country",
    )

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rule",
    )
    search_fields = ("city", "^host__username")
    readonly_fields = ("updated", "created")

    def count_amenities(self, object):
        #    print(object.amenities.count())
        return object.amenities.count()


#    count_amenities.short_description = "Sexy"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Definition"""

    pass
