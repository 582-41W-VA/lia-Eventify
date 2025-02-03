from django.contrib import admin
from .models import Category, Event, Comment, FavoriteEvent, Like, Flag

admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Comment)
admin.site.register(FavoriteEvent)
admin.site.register(Like)
admin.site.register(Flag)
