from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request,"home.html")
def aboutme(request):
    return render(request,"aboutme.html")
def contactme(request):
    return render(request,"contactme.html")
def services(request):
    return render(request,"services.html")
def thankyou(request):
    value = {}
    try:
        if request.method == "GET":
            data = request.GET.get("output")
    except:
        pass
    value = {'d':data}
    return render(request,"thankyou.html", value)

def form(request):
    final_value = 0
    data = {}
    try:
        if request.method == "POST":
            value1 = int(request.POST.get('Num1'))
            value2 = int(request.POST.get('Num2'))
        final_value = value1 + value2
        data = {'v1':value1,'v2':value2, 'content':final_value}

        url = f"/thankyou/?output={final_value}"
        return HttpResponseRedirect(url)
    
    except:
        pass
    return render(request,"form.html",data)
