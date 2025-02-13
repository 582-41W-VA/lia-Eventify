# events/views_admin.py
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.db.models import Count
from .models import Event
from django.contrib.auth import get_user_model


@staff_member_required
def admin_statistics(request):
  
    return render(request, 'events/admin/statistics.html', context)
