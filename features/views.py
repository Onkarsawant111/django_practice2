from django.shortcuts import render
from features.models import Uses

# Create your views here.
def uses(request):
    data = Uses.objects.all()
    if request.method == "GET":
        search = request.GET.get("search")
        if search != None:
            data = Uses.objects.filter(uses_title__icontains = search) or Uses.objects.filter(uses_des__icontains = search)
        
                
    content = {
        'uses':data
    }
    return render(request, 'uses.html', content)

def pictures(request):
    return render(request, 'pictures.html')