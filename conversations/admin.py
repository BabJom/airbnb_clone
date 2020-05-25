from django.contrib import admin
from . import models


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    """MessageAmdin Model Definition"""

    pass


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """ConversationAdmin Model Definition"""

    pass
