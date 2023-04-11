from django.shortcuts import render
from app.models import *
#from django.db.models.function import length
# Create your views here.

def display_topic(request):
    LOT=Topic.objects.all()
    d={'topic':LOT}
    return render(request,'topics.html',d)

def display_webpage(request):
    LOW=Webpage.objects.all()
    #ascending order
    #LOW=Webpage.objects.order_by('name')
    #ascending length order
    #LOW=Webpage.objects.orrder_by(length('name'))
    #descending order
    #LOW=Webpage.objects.order_by('-name')
    #exclude method 
    #LOW=Webpage.objects.exclude(topic_name='cricket')
    
    d={'webpages':LOW}
    return render(request,'webpages.html',d)
def display_access(request):
    LOA=AccessRecord.objects.all()
    d={'access':LOA}
    return render(request,'acces.html',d)
