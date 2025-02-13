from django.contrib import admin
from .models import Category, Event, Comment, FavoriteEvent, Like, Flag, Attendance


admin.site.register(Category)
# admin.site.register(Event)

@admin.register(Event)


class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by", "is_flagged", "is_approved")
    list_filter = ("is_flagged", "is_approved", "category", "created_by")
    search_fields = ("title", "created_by__username", "category__name")
    actions = ["approve_events", "remove_flagged_events"]
   
    def approve_events(self, request, queryset):
        """ Approve flagged events and remove flag status. """
        queryset.update(is_approved=True, is_flagged=False)
        self.message_user(request, "Selected events have been approved.")

    approve_events.short_description = "Approve selected flagged events"

    def remove_flagged_events(self, request, queryset):
        """ Remove flagged events from the database. """
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f"{count} flagged events have been removed.")

    remove_flagged_events.short_description = "Remove selected flagged events"


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


@admin.register(Flag)
class FlagAdmin(admin.ModelAdmin):
    list_display = ("user", "event", "reason", "created_at")
    search_fields = ("user__username", "event__title", "reason")
    list_filter = ("reason", "created_at")

admin.site.register(Attendance)