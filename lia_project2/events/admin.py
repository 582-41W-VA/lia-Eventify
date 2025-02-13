from django.contrib import admin
from .models import Category, Event, Comment, FavoriteEvent, Like, Flag, Attendance


admin.site.register(Category)
# admin.site.register(Event)
admin.site.register(Comment)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by", "is_flagged")
    list_filter = ("is_flagged", "category", "created_by")
    search_fields = ("title", "created_by__username", "category__name")
    actions = ["approve_events", "remove_flagged_events"]



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
    actions = ["approve_flagged_event", "remove_flagged_event"]
    def approve_flagged_event(self, request, queryset):
        """ Approve the flagged event by updating its status. """
        for flag in queryset:
            flag.event.is_approved = True
            flag.event.is_flagged = False
            flag.event.save()
        count = queryset.count()
        self.message_user(request, f"{count} flagged events have been approved.")
        queryset.delete()  # Remove the flags after approval

    approve_flagged_event.short_description = "Approve flagged events"

    def remove_flagged_event(self, request, queryset):
        """ Remove flagged events from the database. """
        count = queryset.count()
        for flag in queryset:
            flag.event.delete()  # Delete the associated event
        queryset.delete()  # Delete the flags
        self.message_user(request, f"{count} flagged events have been removed.")

    remove_flagged_event.short_description = "Remove flagged events"

admin.site.register(Attendance)