from django.urls import path
from .views import attended_events
from . import views


from .views import (
    homepage, event_list, event_detail, event_create,
    toggle_like, toggle_favorite, toggle_flag, saved_events_dashboard,
    toggle_attendance, my_events_dashboard
    
)

urlpatterns = [
    path("", homepage, name="homepage"),
    path("list/", event_list, name="event_list"),
    path("<int:event_id>/", event_detail, name="event_detail"),
    path("create/", event_create, name="event_create"),
    path("events/<int:event_id>/like/", toggle_like, name="toggle_like"),
    path("events/<int:event_id>/favorite/", toggle_favorite, name="toggle_favorite"),
    path("events/<int:event_id>/flag/", toggle_flag, name="toggle_flag"),
    path("saved_events_dashboard/", saved_events_dashboard, name="saved_events_dashboard"),
    path("events/<int:event_id>/attend/", toggle_attendance, name="toggle_attendance"),
    path("my_events_dashboard/", my_events_dashboard, name="my_events_dashboard"),

    path('dashboard/favorited-events/', views.favorited_events, name='favorite-events'),

    
    path('dashboard/attended-events/', attended_events, name='attended-events'),
    path('event/<int:event_id>/', event_detail, name='event-detail'),
]
