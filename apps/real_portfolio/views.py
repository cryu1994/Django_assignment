from django.shortcuts import render

def index(request):
    return render(request, "index/index.html")
def about(request):
    return render(request, "index/about.html")
def project(request):
    return render(request, "index/project.html")
def testimonials(request):
    return render(request, "index/testimonials.html")
# Create your views here.
