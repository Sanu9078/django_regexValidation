from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.
def register(request):
    ECFO=CredForm()
    d={'ECFO':ECFO}
    if request.method == 'POST' and request.FILES:
        CFDO=CredForm(request.POST,request.FILES)
        if CFDO.is_valid():
            CFDO.save()
            return HttpResponse("Done")
        return HttpResponse("Invalid Data")
    return render(request ,'register.html',d)

def login(request):
    if request.method == 'POST':
        username=request.POST.get('un')
        password=request.POST.get('pw')
        CO=Credential.objects.filter(username=username,password=password)[0]
        if CO:
            d={'CO':CO}
            return render(request,'home.html',d)
        return HttpResponse("Invalid Data")
    return render(request,'login.html')