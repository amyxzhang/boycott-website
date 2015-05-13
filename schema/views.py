from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from schema.models import *
import schema
from django.utils import timezone

def error(request):
    return render(request, '404.html', {})

def my_wecotts(request):
    if request.user.is_authenticated():
        signed = Signature.objects.filter(user=request.user)
        mine = BoycottPetition.objects.filter(created_by=request.user)
        return render(request, 'mycott.html', {'mine': mine, 'signed':signed})
    else:
        return redirect('/accounts/login/')

def home(request):
    top_ten = BoycottPetition.objects.all().order_by('-created_at')[:10]
    for top in top_ten:
        top.num_likes = LikePetition.objects.filter(petition_id=top.id).count()
        top.num_sigs = Signature.objects.filter(petition_id=top.id).count()
        top.description = top.description[0:450]
        
    	top.amount_saved = top.num_sigs * 300.52
        top.amount_bought = top.num_sigs * 157.32
    
    return render(request, 'home.html', {'top':top_ten})

def create(request):
    return render(request, 'create.html', {})

def petition(request, petition_id):
    
    try:
        p = BoycottPetition.objects.get(id=petition_id)
        sigs = Signature.objects.filter(petition_id=p.id)
        for sig in sigs:
            sig.user_image = sig.user.userprofile_set.all()[0].image_url
        imgs = PictureBoycott.objects.filter(petition_id=p.id)
        alts = Alternatives.objects.filter(petition_id=p.id)
        udates = UpdatePetition.objects.filter(petition_id=p.id)
        
        updates = []
        for update in udates:
            updates.append({'created_at': update.created_at,
                            'description': update.description})
        
        updates.append({'created_at': p.created_at,
                        'description': 'This WeCott campaign was created!'})
        
        updates = sorted(updates, key=lambda x: x['created_at'], reverse=True)
        
    	p.amount_saved = len(sigs) * 300.52
        p.amount_bought = len(sigs) * 157.32
    	p.count_sig = len(sigs)
    	p.count_imgs = len(imgs)
        user = p.created_by.userprofile_set.all()[0]
        time_e = timezone.now() - p.created_at
        p.days = time_e.days
    except BoycottPetition.DoesNotExist:
        return redirect('/404')
        
    return render(request, 'petition.html', {'petition': p, 'sigs': sigs, 'imgs': imgs, 'alts': alts, 'user': user, 'updates': updates})

