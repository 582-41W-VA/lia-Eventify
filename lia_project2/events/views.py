from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from .models import Event, Category, FavoriteEvent, Like, Flag, Attendance, Comment
from django.conf import settings
from django.utils.timezone import now, timedelta

PROVINCES = {
    "ON": ["Toronto", "Ottawa", "Mississauga", "Hamilton"],
    "QC": ["Montreal", "Quebec City", "Laval", "Gatineau"]
}


def get_filtered_events(request):
    query = request.GET.get("q", "").strip()
    selected_category = request.GET.get("category", "").strip()
    province = request.GET.get("province", "").strip()
    city = request.GET.get("city", "").strip()
    date_filter = request.GET.get("date", "any").strip()

    events = Event.objects.filter(end_datetime__gte=now()).order_by("start_datetime") 

    if query:
        events = events.filter(Q(title__icontains=query) | Q(description__icontains=query))
    if selected_category:
        events = events.filter(category__name=selected_category)
    if selected_category:
        events = events.filter(category__name=selected_category)

    today = now().date()
    if date_filter == "this_week":
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        events = events.filter(start_datetime__date__gte=start_of_week, start_datetime__date__lte=end_of_week)

    elif date_filter == "next_week":
        start_of_next_week = today + timedelta(days=7 - today.weekday())
        end_of_next_week = start_of_next_week + timedelta(days=6)
        events = events.filter(start_datetime__date__gte=start_of_next_week, start_datetime__date__lte=end_of_next_week)

    if province:
        events = events.filter(province=province)
    if city and city in PROVINCES.get(province, []):
        events = events.filter(city=city)

    return events

def get_featured_events():
    return Event.objects.annotate(like_count=Count("likes")).order_by("-like_count")[:6]

def homepage(request):
    all_events = get_filtered_events(request).order_by("start_datetime")
    featured_events = all_events.annotate(like_count=Count('likes')).order_by('-like_count')[:6]
    all_events = all_events[:6]
    categories = Category.objects.all()


    user_liked_events = (
        Like.objects.filter(user=request.user).values_list("event_id", flat=True)
        if request.user.is_authenticated else []
    )

    return render(request, "events/homepage.html", {
        "featured_events": featured_events,
        "all_events": all_events,
        "query": request.GET.get("q", "").strip(),
        "selected_province": request.GET.get("province", ""),
        "selected_city": request.GET.get("city", ""),
        "categories": categories,
        "provinces": PROVINCES,
        "cities": PROVINCES.get(request.GET.get("province", ""), []),
        "user_liked_events": list(user_liked_events),
    })


@login_required
def saved_events_dashboard(request):
    favorite_events = FavoriteEvent.objects.filter(user=request.user).select_related("event")


    if request.method == "POST":
        action = request.POST.get("action")
        selected_events = request.POST.getlist("selected_events")


        if action == "remove" and selected_events:
            FavoriteEvent.objects.filter(user=request.user, event__id__in=selected_events).delete()
            return redirect("saved_events_dashboard")


    return render(request, "events/saved_events_dashboard.html", {"favorite_events": favorite_events})


@login_required
def toggle_like(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    user = request.user


    like, created = Like.objects.get_or_create(user=user, event=event)


    if created:
        event.likes.add(user)
    else:
        like.delete()
        event.likes.remove(user)


    return redirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def toggle_favorite(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    user = request.user


    favorite_event, created = FavoriteEvent.objects.get_or_create(user=user, event=event)


    if not created:
        favorite_event.delete()


    return redirect(request.META.get("HTTP_REFERER", request.path))

@login_required
def toggle_flag(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    user = request.user

    existing_flag = Flag.objects.filter(user=user, event=event)

    if existing_flag.exists():
        existing_flag.delete()
    else:
        if request.method == "POST":
            reason = request.POST.get("reason", "other")
            Flag.objects.create(user=user, event=event, reason=reason)

    return redirect(request.META.get("HTTP_REFERER", "/"))

def event_list(request):
    all_events = get_filtered_events(request)
    categories = Category.objects.all()

    user_liked_events = (
        Like.objects.filter(user=request.user).values_list("event_id", flat=True)
        if request.user.is_authenticated else []
    )

    paginator = Paginator(all_events, 36) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "events/event_list.html", {
        "all_events": all_events,
        "selected_province": request.GET.get("province", ""),
        "selected_city": request.GET.get("city", ""),
        "categories": categories,
        "selected_category": request.GET.get("category", "").strip(),
        "selected_date": request.GET.get("date", "any").strip(),
        "provinces": PROVINCES,
        "cities": PROVINCES.get(request.GET.get("province", ""), []),
        "user_liked_events": list(user_liked_events),
    })


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    is_flagged = False
    if request.user.is_authenticated:
        is_flagged = Flag.objects.filter(user=request.user, event=event).exists()

    favorite_events = (
        FavoriteEvent.objects.filter(user=request.user).values_list("event_id", flat=True)
        if request.user.is_authenticated else []
    )

    comments = Comment.objects.filter(event=event).order_by('-created_at')

    if request.method == "POST":
        if request.user.is_authenticated:
            text = request.POST.get("text").strip()
            if text:
                Comment.objects.create(user=request.user, event=event, text=text)
                return redirect("event_detail", event_id=event.id)
        else:
            return redirect("accounts:login")

    return render(request, "events/event_detail.html", {
        "event": event,
        "is_flagged": is_flagged,
        "favorite_events": favorite_events,
        "max_attendees": event.max_attendees,
        "comments": comments,
        "GOOGLE_MAPS_API_KEY": settings.GOOGLE_MAPS_API_KEY
    })

@login_required
def event_creation(request):
    categories = Category.objects.all()

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
            return render(request, "events/event_creation.html", {
                "error": "Invalid category.", "categories": categories
            })

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

    return render(request, "events/event_creation.html", {
        "categories": categories,
    })

@login_required
def toggle_attendance(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    user = request.user

    existing_attendance = Attendance.objects.filter(user=user, event=event)
    if existing_attendance.exists():
        existing_attendance.delete()
        return redirect(request.META.get("HTTP_REFERER", "/"))

    if event.attendee_count() < event.max_attendees:
        Attendance.objects.create(user=user, event=event)
    else:
        return render(request, "events/event_detail.html", {
            "event": event,
            "error_message": "This event is fully booked.",
        })

    return redirect(request.META.get("HTTP_REFERER", "/"))

@login_required
def my_events_dashboard(request):
    attending_events = request.user.attending_events.all()

    if request.method == "POST":
        action = request.POST.get("action")
        selected_events = request.POST.getlist("selected_events")

        if action == "cancel" and selected_events:
            Attendance.objects.filter(user=request.user, event__id__in=selected_events).delete()
            return redirect("my_events_dashboard")

    return render(request, "events/my_events_dashboard.html", {
        "attending_events": attending_events,
    })


@login_required
def created_events(request):
    events = Event.objects.filter(created_by=request.user)
    return render(request, 'events/my_events.html', {'events': events})


@login_required
def favorited_events(request):
    favorited_events = Event.objects.filter(favoriteevent__user=request.user)  
    return render(request, 'events/favorited_events.html', {'favorited_events': favorited_events})


@login_required
def attended_events(request):
    attended_events = Attendance.objects.filter(user=request.user)
    return render(request, 'events/attended_events.html', {
        'attended_events': attended_events
    })