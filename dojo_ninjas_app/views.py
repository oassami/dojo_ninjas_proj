from django.shortcuts import render, redirect
from .models import *

def index(request):
    context={
        'dojos': Dojo.objects.all()
    }
    return render(request, "index.html", context)

def add_dojo(request):
    if request.method=="POST":
        Dojo.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])
    return redirect('/')

def add_ninja(request):
    if request.method=="POST":
        the_dojo = Dojo.objects.get(id=request.POST['dojo'])
        new_ninja = Ninja.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], dojo=the_dojo)
    return redirect('/')

def delete_dojo(request, dojo_id):
    dojo_to_delete = Dojo.objects.get(id=dojo_id)
    dojo_to_delete.delete()
    return redirect('/')
    