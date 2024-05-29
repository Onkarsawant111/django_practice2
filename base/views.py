from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def aboutme(request):
    return render(request,'aboutme.html')
def contactme(request):
    return render(request,'contactme.html')
def services(request):
    return render(request,'services.html')