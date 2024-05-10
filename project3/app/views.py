from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
sln = 0
def home(request):
    return render(request,"main.html")
def login(request):
    if request.method == 'POST':
        un = request.POST.get("un")
        pw = request.POST.get('pw')

        try:
            TO = Notes.objects.get(un=un , pw=pw)
            if TO:
                sln = TO.sln
                allobj = Notec.objects.filter(sln=sln)
                d={"item":TO,"allobj":allobj}
                return render(request,"index.html",d)
        except:
            return HttpResponse('Invalid Credentials')
    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        name = request.POST.get("nme")
        sln = request.POST.get("un")
        pw = request.POST.get("pw")

        NO = Notes(name=name ,sln=sln ,pw =pw)
        NO.save()
        return render(request,"login.html")
    return render(request,"register.html")
def page(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        desc = request.POST.get('desc')
        global sln
        sln = request.POST.get("sln")
        
        s=Notec.objects.filter(title = title)
        if s:
            return HttpResponse("This title already exist")
        elif title == "":
            return HttpResponse("Enter a title")
        NO = Notec(sln=sln,title=title,desc=desc)
        NO.save() 
    allobj = Notec.objects.filter(sln=sln)
    if allobj:
        items=allobj[0].sln
    d ={"allobj":allobj,'items':items}
    return render(request,"index.html",d)
def update(request):
    if request.method == "GET":
        
        title1 = request.GET.get("upn")
        x = Notec.objects.get(title=title1)
        d={'x':x}
        return render(request,"update.html",d)
    elif request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        sln = request.POST.get("sln")

        nobj = Notec.objects.filter(title =title)
        nobj.update(title=title , desc= desc)
        items =nobj[0].sln

        allobj = Notec.objects.filter(sln=sln)
        d={"allobj":allobj , 'items':items}
        return render(request,"index.html",d)

def delete(request):
    items = request.POST.get("sln")
    c={'items':items}
    if request.method == "GET":
        title = request.GET.get("upn")
        sln = request.GET.get("dln")

        NO = Notec.objects.filter(title = title)
        NO.delete()

        allobj = Notec.objects.filter(sln=sln)
        if allobj:
            items=allobj[0].sln       
            if items:         
                d={'allobj':allobj ,'items':items}
                return render(request,'index.html',d)
            
        return render(request,'index.html',c)