from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from .models import Event, Category
from django.conf import settings

PROVINCES = {
    "ON": ["Toronto", "Ottawa", "Mississauga", "Hamilton"],
    "QC": ["Montreal", "Quebec City", "Laval", "Gatineau"]
}

def get_filtered_events(request):
    query = request.GET.get("q", "").strip()
    selected_category = request.GET.get("category", "").strip()
    province = request.GET.get("province", "").strip()
    city = request.GET.get("city", "").strip()

    events = Event.objects.all().order_by("-start_datetime")

    if query:
        events = events.filter(Q(title__icontains=query) | Q(description__icontains=query))
    if selected_category:
        events = events.filter(category__name=selected_category)
    if province:
        events = events.filter(province=province)
    if city and city in PROVINCES.get(province, []):
        events = events.filter(city=city)

    return events

def homepage(request):
    all_events = get_filtered_events(request).order_by("-start_datetime")[:6]
    featured_events = all_events.annotate(like_count=Count('likes')).order_by('-like_count')[:6]
    categories = Category.objects.all()
    
    return render(request, "events/homepage.html", {
        "featured_events": featured_events,
        "all_events": all_events,
        "query": request.GET.get("q", "").strip(),
        "selected_province": request.GET.get("province", ""),
        "selected_city": request.GET.get("city", ""),
        "categories": categories,
        "provinces": PROVINCES,
        "cities": PROVINCES.get(request.GET.get("province", ""), [])
    })

def toggle_like(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    user = request.user
    if user in event.likes.all(): 
        event.likes.remove(user) 
    else:
        event.likes.add(user) 
    return redirect(request.META.get("HTTP_REFERER", "/"))


def event_list(request):
    events = get_filtered_events(request)
    featured_events = events.annotate(like_count=Count('likes')).order_by('-like_count')[:6]
    categories = Category.objects.all()

    return render(request, "events/event_list.html", {
        "events": events,
        "featured_events": featured_events,
        "categories": categories,
        "query": request.GET.get("q", "").strip(),
        "selected_category": request.GET.get("category", ""),
        "selected_province": request.GET.get("province", ""),
        "selected_city": request.GET.get("city", ""),
        "provinces": PROVINCES,
        "cities": PROVINCES.get(request.GET.get("province", ""), [])
    })

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, "events/event_detail.html", {
        "event": event,
        "GOOGLE_MAPS_API_KEY": settings.GOOGLE_MAPS_API_KEY
    })

@login_required
def event_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        start_datetime = request.POST.get("start_datetime")
        end_datetime = request.POST.get("end_datetime")
        max_attendees = request.POST.get("max_attendees")
        location = request.POST.get("location")
        province = request.POST.get("province")
        city = request.POST.get("city")
        latitude = request.POST.get("latitude") or None
        longitude = request.POST.get("longitude") or None
        category_name = request.POST.get("category")
        image = request.FILES.get("image")

        category = Category.objects.filter(name=category_name).first()
        if not category:
            return render(request, "events/event_create.html", {"error": "Invalid category."})

        Event.objects.create(
            title=title,
            description=description,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            max_attendees=max_attendees,
            location=location,
            province=province,
            city=city,
            latitude=latitude,
            longitude=longitude,
            category=category,
            image=image,
            created_by=request.user,
        )
        return redirect("event_list")

    categories = Category.objects.all()
    return render(request, "events/event_create.html", {
        "categories": categories,
        "provinces": PROVINCES,
    })
