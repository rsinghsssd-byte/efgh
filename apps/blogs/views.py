from django.shortcuts import render

def blogs_list_view(request):
    return render(request, "dashboard/blogs.html")

def blog_detail_view(request, slug=None):
    return render(request, "generator/blogreader.html")

def favorites_view(request):
    return render(request, "emptypage/favroites_emptypage.html")

def history_view(request):
    return render(request, "dashboard/history.html")
