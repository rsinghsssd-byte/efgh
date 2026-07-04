from django.shortcuts import render

def generator_view(request):
    return render(request, "generator/bloggenerator.html")

def process_view(request):
    return render(request, "generator/process.html")
