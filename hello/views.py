from django.shortcuts import render
from django.http import HttpResponse
from cgi import escape
from requests import get

from .models import Greeting

# Create your views here.
def index(request):
    name = escape(request.META['HTTP_HOST']).split('.')[-3]
    title = "%s got peachd" % (name.title())
    try:
        fart = get("https://sfx-api.herokuapp.com/farts/random").json()
    except:
        fart = {}

    return render(request, 'index.html', {
        'greeting': {
            'title': title,
            'name': name,
            'fart': fart
        }
    })


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

