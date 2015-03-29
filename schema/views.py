from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from schema.models import *
import schema

def error(request):
    return render(request, '404.html', {})

def home(request):
    top_ten = BoycottPetition.objects.all()[:10]
    for top in top_ten:
        top.num_likes = LikePetition.objects.filter(petition_id=top.id).count()
        top.num_sigs = Signature.objects.filter(petition_id=top.id).count()
    return render(request, 'home.html', {'top':top_ten})

def create(request):
    return render(request, 'create.html', {})

def petition(request, petition_id):
    
    try:
        p = BoycottPetition.objects.get(id=petition_id)
    except BoycottPetition.DoesNotExist:
        return redirect('/404')
        
    return render(request, 'petition.html', {'petition': p})

