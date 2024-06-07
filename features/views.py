from django.shortcuts import render
from features.models import Uses

# Create your views here.
def uses(request):
    data = Uses.objects.all()
    content = {
        'uses':data
    }
    return render(request, 'uses.html', content)

def pictures(request):
    return render(request, 'pictures.html')