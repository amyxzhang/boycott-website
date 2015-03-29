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
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PetitionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            created_at = models.DateTimeField(default=datetime.datetime.utcnow())
            created_by = models.ForeignKey(User)
            # redirect to a new URL:
            return HttpResponseRedirect('/') # TODO

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PetitionForm()

    return render(request, 'create.html', {'form': form})

def petition(request, petition_id):
    
    try:
        p = BoycottPetition.objects.get(id=petition_id)
    except BoycottPetition.DoesNotExist:
        return redirect('/404')
        
    return render(request, 'petition.html', {'petition': p})

