from django.urls import path
from .views import homepage, event_list, event_detail, event_create, event_edit, event_delete

urlpatterns = [
    path("", homepage, name="homepage"),
    path("list/", event_list, name="event_list"),
    path("<int:event_id>/", event_detail, name="event_detail"),
    path("create/", event_create, name="event_create"),
    path("<int:event_id>/edit/", event_edit, name="event_edit"),
    path("<int:event_id>/delete/", event_delete, name="event_delete"),
]
