from django.shortcuts import render
from schema.models import *
import schema

def home(request):
	top_ten = BoycottPetition.objects.all()[:10]
	return render(request, 'schema/home.html', {'top':top_ten})
