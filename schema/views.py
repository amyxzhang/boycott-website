from django.shortcuts import render
import schema

def home(request):
    return render(request, 'home.html', {})