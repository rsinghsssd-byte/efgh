from django.shortcuts import render

def landing_page_view(request):
    return render(request, "landing/landingpage.html")

def dashboard_view(request):
    return render(request, "dashboard/dashboard.html")

def profile_view(request):
    return render(request, "dashboard/profile.html")

def settings_view(request):
    return render(request, "dashboard/settings.html")
