from django.shortcuts import render
from django.http import HttpResponse
from models import Url

# Create your views here.
def index(request):
    url = request.GET.get('url', '')
    if url == '':
        return render(request, 'index.html')
    else:
        return shortened(request, url)

def shortened(request, url):
    short_url = request.get_host() + '/' + Url.shorten(url)
    return render(request, 'shortened.html', {'short_url':short_url})