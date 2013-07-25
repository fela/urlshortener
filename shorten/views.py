from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return shortened(request, 'http://test.com')
    #return render(request, 'index.html')

def shortened(request, url):
    return render(request, 'shortened.html', {'short_url':url})