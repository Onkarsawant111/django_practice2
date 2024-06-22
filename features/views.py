from django.shortcuts import render
from features.models import Uses
from django.core.paginator import Paginator
from features.models import Formdata
# brevo sending mail :
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def uses(request):
    data = Uses.objects.all()
    if request.method == "GET":
        search = request.GET.get("search")
        if search != None:
            data = Uses.objects.filter(uses_title__icontains = search) or Uses.objects.filter(uses_des__icontains = search)
    
    pagi = Paginator(data, 2)
    page_num = request.GET.get('page')
    pagi_data = pagi.get_page(page_num)
    totalpages = pagi_data.paginator.num_pages      
        
    content = { 
        'uses':pagi_data,
        'page_number':[i+1 for i in range(totalpages)]
    }
    return render(request, 'uses.html', content)


def formdata(request):
    submit = {}
    if request.method == "POST":
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        data = Formdata(name=name,email=email,password=password)
        data.save()
        mssge = "data submitted"
        submit = {'mssge':mssge}
    
        send_mail(
            "tsting mai onkar sawant",
            "Here is the message.",
            settings.EMAIL_HOST_USER,
            ["onkarsawant111@gmail.com","os2962000@gmail.com"],
            fail_silently=False,
        )
    return render(request, 'formdata.html', submit)


