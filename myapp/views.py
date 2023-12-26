from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Contact
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')
        contact = Contact(name= name, email= email, phone= phone, comment= comment, date= datetime.today())
        contact.save()
    return render(request, 'contact.html')
def makeup(request):
    return HttpResponse("this is Makup page")
def body_massage(request):
    return HttpResponse("this is Massage Page")
def nail(request):
    return HttpResponse("this is Nails Page")
def skin_care(request):
    return HttpResponse("this is Skin Care page")
def hair_care(request):
    return HttpResponse("this is Hair Care Page")
def hair_style(request):
    return HttpResponse("this is Hair Style Page")