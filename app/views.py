from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        QLTO=Topic.objects.all()
        d={'topics':QLTO}
        return render(request,'display_topic.html',d)
    return render(request,'insert_topic.html')


def insert_webpage(request):
     QLTO=Topic.objects.all()
     d={'topics':QLTO}
     if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        TO=Topic.objects.get(topic_name=tn)
        WO=WebPage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
        WO.save()
        QLWO=WebPage.objects.all()
        d1={'webpages':QLWO}
        return render(request,'display_webpage.html',d1)
     return render(request,'insert_webpage.html',d)


def select_multiple(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}

    if request.method=='POST':
        topiclist=request.POST.getlist('tn')
        QLWO=WebPage.objects.none()
        for i in topiclist:
            QLWO=QLWO|WebPage.objects.filter(topic_name=i)
            d1={'webpages':QLWO}
            return render(request,'display_webpage.html',d1)


    return render(request,'select_multiple.html',d)
