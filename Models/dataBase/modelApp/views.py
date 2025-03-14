from django.shortcuts import render, redirect
from .models import Members

# Create your views here.
def index(request):
    mem = Members.objects.all()
    return render(request, 'index.html', {'mem': mem})

def add(request):
    return render(request, 'form.html')


def addrec(request):
    x = request.POST['first']
    y = request.POST['last']
    z = request.POST['country']

    mem = Members(first_name=x, last_name=y, country=z)
    mem.save()
    return redirect('/')

def delete(request, id):
    mem = Members.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request, id):
    mem = Members.objects.get(id=id)
    return render(request, 'update.html', {'mem':mem})

def uprec(request, id):
    x = request.POST['first']
    y = request.POST['last']
    z = request.POST['country']

    mem = Members.objects.get(id=id)
    mem.first_name = x
    mem.last_name = y
    mem.country = z

    mem.save()
    return redirect("/")