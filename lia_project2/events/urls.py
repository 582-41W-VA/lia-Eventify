from django.urls import path
from .views import homepage, event_list, event_detail, event_create

urlpatterns = [
    path("", homepage, name="homepage"),
    path("list/", event_list, name="event_list"),
    path("<int:event_id>/", event_detail, name="event_detail"),
    path("create/", event_create, name="event_create"),
]
