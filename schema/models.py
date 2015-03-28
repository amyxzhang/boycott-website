from django.db import models
from django.contrib.auth.models import User
import util

import datetime

# Create your models here.

class BoycottPetition(models.Model):
    name = models.CharField(max_length=250, default='')
    description = models.TextField(default='')
    what_to_boycott = models.TextField(default='')
    created_at = models.DateTimeField(default=datetime.datetime.utcnow())
    created_by = models.ForeignKey(User)
    image_url = models.URLField(max_length=300, null=True)
    video_url = models.URLField(max_length=300, null=True)
    
class UpdatePetition(models.Model):
    petition = models.ForeignKey(BoycottPetition)
    description = models.TextField(default='')

class PictureBoycott(models.Model):
    petition = models.ForeignKey(BoycottPetition)
    user = models.ForeignKey(User)
    image_url = models.URLField(max_length=300, null=False)
    created_at = models.DateTimeField(default=datetime.datetime.utcnow())

class LikePetition(models.Model):
    user = models.ForeignKey(User)
    petition = models.ForeignKey(BoycottPetition)

class Signature(models.Model):
    user = models.ForeignKey(User)
    petition = models.ForeignKey(BoycottPetition)
    reason = models.TextField(default='')
    signed_at = models.DateTimeField(default=datetime.datetime.utcnow())
    cash_amount = models.IntegerField()
    time_scale = models.CharField(max_length=10, choices=util.TIME_SCALES)

class LikeSignature(models.Model):
    user = models.ForeignKey(User)
    signature = models.ForeignKey(Signature)

class UserProfile(models.Model):
    user = models.ForeignKey(User)
