from django.shortcuts import render
from django.http import HttpResponse
 
# Create your views here.


def index(request):
    context = {}
    # return HttpResponse('<h1>DM Plugin</h1>')
    return render(request, 'index.html', context)
