from django.contrib import admin
from .models import Category, Event, Comment, FavoriteEvent, Like, Flag


admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Comment)
@admin.register(FavoriteEvent) #edit
class FavoriteEventAdmin(admin.ModelAdmin):
    list_display = ("user", "event")
    search_fields = ("user__username", "event__title")
    list_filter = ("event", "user")
@admin.register(Like) #edit
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "event")
    search_fields = ("user__username", "event__title")
    list_filter = ("event", "user")


admin.site.register(Flag)