from django.shortcuts import render
from django.http import HttpResponse
from models import Url
import re


# helper
def normalize_url(url):
    url = url.strip()
    if not re.match(r'^(http://|https://)', url):
        url = 'http://'+url
    return url


# Create your views here.
def index(request):
    url = request.GET.get('url', None)
    if url:
        # shorten
        url = normalize_url(url)
        return shortened(request, url)
    else:
        # allow input
        return render(request, 'index.html')


def shortened(request, url):
    short_url = 'http://' + request.get_host() + '/' + Url.shorten(url)
    return render(request, 'shortened.html', {'short_url': short_url})


def redirect(request, str):
    url = Url.objects.get(short_string=str).url
    return render(request, 'redirect.html', {'url': url})