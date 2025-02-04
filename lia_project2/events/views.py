from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Event, Category

def homepage(request):
    query = request.GET.get("q", "").strip()
    events = Event.objects.all().order_by("-start_datetime")

    if query:
        events = events.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, "events/homepage.html", {
        "all_events": events,
        "query": query
    })

def event_list(request):
    events = Event.objects.all().order_by("-start_datetime")
    return render(request, "events/event_list.html", {"events": events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, "events/event_detail.html", {"event": event})

@login_required
def event_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        start_datetime = request.POST.get("start_datetime")
        end_datetime = request.POST.get("end_datetime")
        max_attendees = request.POST.get("max_attendees")
        location = request.POST.get("location")
        latitude = request.POST.get("latitude") or None
        longitude = request.POST.get("longitude") or None
        category_name = request.POST.get("category")
        image = request.FILES.get("image")

        category = Category.objects.filter(name=category_name).first()
        if not category:
            return render(request, "events/event_create.html", {"error": "Invalid category."})

        event = Event.objects.create(
            title=title,
            description=description,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            max_attendees=max_attendees,
            location=location,
            latitude=latitude,
            longitude=longitude,
            category=category,
            image=image,
            created_by=request.user,
        )
        return redirect("event_list")

    categories = Category.objects.all()
    return render(request, "events/event_create.html", {"categories": categories})
