from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")
def aboutme(request):
    return render(request,"aboutme.html")
def contactme(request):
    return render(request,"contactme.html")
def services(request):
    return render(request,"services.html")


def form(request):
    final_value = 0
    try:
        value1 = int(request.GET.get('Num1'))
        value2 = int(request.GET.get('Num2'))
        final_value = value1 + value2
    except:
        pass
    return render(request,"form.html",{'content':final_value})