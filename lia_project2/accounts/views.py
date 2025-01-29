from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib.auth import login, logout, authenticate
from accounts.models import User

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        profile_picture = request.FILES.get("profile_picture")
        bio = request.POST.get("bio")

        # Check required fields
        if not username or not email or not password1 or not password2:
            return render(request, "accounts/register.html", {"error": "All fields are required."})

        # Check if username or email is already taken
        if User.objects.filter(username=username).exists():
            return render(request, "accounts/register.html", {"error": "Username already in use."})

        if User.objects.filter(email=email).exists():
            return render(request, "accounts/register.html", {"error": "Email already registered."})

        # Check if passwords match
        if password1 != password2:
            return render(request, "accounts/register.html", {"error": "Passwords do not match."})

        try:
            user = User(
                username=username,
                email=email,
                password=password1,
                profile_picture=profile_picture,
                bio=bio,
            )
            user.save()

            login(request, user)
            return redirect("home")

        except ValidationError as e:
            return render(request, "accounts/register.html", {"error": e.message})

    return render(request, "accounts/register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "accounts/login.html", {"error": "Invalid username or password."})

    return render(request, "accounts/login.html")


def user_logout(request):
    logout(request)
    return redirect("login")