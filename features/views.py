from django.shortcuts import render

# Create your views here.
def uses(request):
    return render(request, 'uses.html')