from django.shortcuts import render
from features.models import Uses
from django.core.paginator import Paginator

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
        
    content = { 
        'uses':pagi_data
    }
    return render(request, 'uses.html', content)

def pictures(request):
    return render(request, 'pictures.html')