from django.shortcuts import render
from django.http import HttpResponseRedirect
from schema.models import *
import schema

from django import forms

class PetitionForm(forms.Form):
    name = forms.CharField(label='WeCott Name', max_length=250)
    description = forms.CharField(label='Description', widget=forms.Textarea) # TODO make rich text?
    what_to_boycott = forms.CharField(label='What to Boycott', max_length=250)
    image_url = forms.CharField(label='Link to image (optional)', max_length=300, required=False)
    video_url = forms.CharField(label='Link to video (optional)', max_length=300, required=False)

def home(request):
	top_ten = BoycottPetition.objects.all()[:10]
	return render(request, 'home.html', {'top':top_ten})

def petition(request, petition_name):
    id = None
    return render(request, 'home.html', {})

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