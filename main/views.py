from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')
def about(request):
    return render(request, 'main/about.html')
def service(request):
    return render(request, 'main/service.html')
def guard(request):
    return render(request, 'main/guard.html')
def blog(request):
    return render(request, 'main/blog.html')
def single(request):
    return render(request, 'main/single.html')
def contact(request):
    return render(request, "main/contact.html")
