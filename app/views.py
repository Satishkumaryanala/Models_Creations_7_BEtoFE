from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.


def display_topic(request):
    QSTO = Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)


def display_webpage(request):
    QSWO = webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_web.html',d)

def display_Access(request):
    QSAO=AccessRecord.objects.all()
    d={'QSAO':QSAO}
    return render(request,'display_Access.html',d)