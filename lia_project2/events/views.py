from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from .models import Event, Category

def homepage(request):
    query = request.GET.get("q", "").strip()
    province = request.GET.get("province", "")
    city = request.GET.get("city", "")

    provinces = {
        "ON": ["Toronto", "Ottawa", "Mississauga", "Hamilton"],
        "QC": ["Montreal", "Quebec City", "Laval", "Gatineau"]
    }
    
    cities = provinces.get(province, []) if province else []

    all_events = Event.objects.all().order_by("-start_datetime")

    if query:
        all_events = all_events.filter(Q(title__icontains=query) | Q(description__icontains=query))

    if province:
        all_events = all_events.filter(province=province)

    if city and city in cities:
        all_events = all_events.filter(city=city)

    featured_events = all_events.annotate(like_count=Count('likes')).order_by('-like_count')[:5]

    return render(request, "events/homepage.html", {
        "featured_events": featured_events,
        "all_events": all_events,
        "query": query,
        "province": province,
        "city": city,
        "provinces": provinces,
        "cities": cities
    })


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from .models import Event, Category

def homepage(request):
    query = request.GET.get("q", "").strip()
    province = request.GET.get("province", "")
    city = request.GET.get("city", "")

    all_events = Event.objects.all().order_by("-start_datetime")

    if query:
        all_events = all_events.filter(Q(title__icontains=query) | Q(description__icontains=query))
    if province:
        all_events = all_events.filter(province=province)
    if city:
        all_events = all_events.filter(city=city)

    featured_events = all_events.annotate(like_count=Count('likes')).order_by('-like_count')[:5]

    categories = Category.objects.all()

    return render(request, "events/homepage.html", {
        "featured_events": featured_events,
        "all_events": all_events,
        "query": query,
        "selected_province": province,
        "selected_city": city,
        "categories": categories,
    })


def event_list(request):
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
    if city:
        events = events.filter(city=city)

    featured_events = events.annotate(like_count=Count('likes')).order_by('-like_count')[:5]

    categories = Category.objects.all()

    provinces = {
        "Ontario (ON)": ["Toronto", "Ottawa", "Mississauga", "Hamilton"],
        "Quebec (QC)": ["Montreal", "Quebec City", "Laval", "Gatineau"],
    }

    return render(request, "events/event_list.html", {
        "events": events,
        "featured_events": featured_events,
        "categories": categories,
        "query": query,
        "selected_category": selected_category,
        "province": province,
        "city": city,
        "provinces": provinces,
    })

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
        province = request.POST.get("province")
        city = request.POST.get("city")
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
    return render(request, "events/event_create.html", {"categories": categories})
