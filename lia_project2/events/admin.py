from django.contrib import admin
from .models import Event, Comment, FavoriteEvent, FlaggedEvent

admin.site.register(Event)
admin.site.register(Comment)
admin.site.register(FavoriteEvent)
admin.site.register(FlaggedEvent)