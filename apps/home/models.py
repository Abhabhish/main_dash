# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class RecordingDetail(models.Model):
    WPGs = [
        ('WP1','WP1'),
        ('WP2','WP2'),
        ('WP3','WP3'),
        ('WP4','WP4'),
        ('WP5','WP5'),
    ]

    WPTs = [
        ('WP1-TV','WP1-TV'),
        ('WP1-K','WP1-K'),
        ('WP2a-TV','WP2a-TV'),
        ('WP2b-TV','WP2b-TV'),
        ('WP2c-TV','WP2c-TV'),
        ('WP2a-K','WP2a-K'),
        ('WP2b-K','WP2c-K'),
        ('WP3-TV','WP3-TV'),
        ('WP3-K','WP3-K'),
        ('WP4-TV','WP4-TV'),
        ('WP4-K','WP4-K'),
        ('WP5-TV','WP5-TV'),
        ('WP5-K','WP5-K')
    ]
    RecordingStatus = [
        ('Completed','Completed'),
        ('Pending','Pending')
    ]
    CarStatus = [
        ('Static','Static'),
        ('Drive','Drive')
    ]
    Ethnicity = [
        ('Caucasian','Caucasian'),
        ('African','African'),
        ('Arab (Middle-East)','Arab (Middle-East)'),
        ('Asians (South-East)','Asians (South-East)'),
        ('Chinese','Chinese'),
        ('Latin/Hispanic','Latin/Hispanic'),
        ('Indian','Indian'),
        ('Others (mixed)','Others (mixed)')
    ]
    Gender = [
        ('M','M'),
        ('F','F')
    ]
    Beard = [
        ('Full beard','Full beard'),
        ('Mustache','Mustache'),
        ('Goatbeard','Goatbeard'),
        ('Henriquatre','Henriquatre')
    ]
    Hair = [
        ('Short hair','Short hair'),
        ('Middle long hair (covering ears, but not long enough to reach the shoulders)','Middle long hair (covering ears, but not long enough to reach the shoulders)'),
        ('Long hair (until shoulder or longer)','Long hair (until shoulder or longer)'),
        ('Bald head','Bald head')
    ]
    EyeColour = [
        ('brown','brown'),
        ('gray','gray'),
        ('blue','blue'),
        ('green','green')
    ]
    ClothingAccessoires = [
        ('Masks','Masks'),
        ('Scarfs','Scarfs'),
        ('Hands-free headset','Hands-free headset'),
        ('Head/Ear phones','Head/Ear phones'),
        ('Caps, hats, headscarf and turban','Caps, hats, headscarf and turban'),
        ('Headband','Headband'),
        ('Eyepatch','Eyepatch'),
        ('Earrings','Earrings'),
        ('Nose rings','Nose rings'),
        ('Piercings','Piercings')
    ]
    Glasses = [
        ('Glasses with anti-glare lenses','Glasses with anti-glare lenses'),
        ('Glasses with mirrored lenses','Glasses with mirrored lenses'),
        ('Sunglasses with IR protection in the band of frequency 780 nm – 1.400 nm','Sunglasses with IR protection in the band of frequency 780 nm – 1.400 nm'),
        ('Glasses with complete spectacle frame','Glasses with complete spectacle frame'),
        ('Metal-rimmed glasses','Metal-rimmed glasses'),
        ('Varifocal glasses with power ranging from –10 to +11','Varifocal glasses with power ranging from –10 to +11'),
        ('Glasses with cylindrical lenses for Astigmatism with power ranging from –10 to +11','Glasses with cylindrical lenses for Astigmatism with power ranging from –10 to +11'),
        ('Spherical contact lenses for Astigmatism with power ranging from  –10 to +11','Spherical contact lenses for Astigmatism with power ranging from  –10 to +11'),
        ('Sunglasses with tinted lenses','Sunglasses with tinted lenses')
    ]
    Makeup = [
        ('Makeup eyeliner','Makeup eyeliner'),
        ('Makeup mascara','Makeup mascara'),
        ('Makeup eye shadow','Makeup eye shadow'),
        ('Makeup false eyelashes','Makeup false eyelashes'),
        ('Cover makeup','Cover makeup')
    ]
    

    name = models.CharField(max_length=100)
    ethnicity=models.CharField(max_length=100,choices=Ethnicity)
    age = models.IntegerField()
    gender = models.CharField(max_length=10,choices=Gender)
    date = models.DateField(default=timezone.now)
    height = models.IntegerField()
    beard = models.CharField(max_length=100,choices=Beard,null=True)
    hair = models.CharField(max_length=100,choices=Hair)
    eyecolour = models.CharField(max_length=100,choices=EyeColour)
    workpackage = models.CharField(max_length=100,choices=WPGs)
    workpackagetype = models.CharField(max_length=100,choices=WPTs)
    carnumber = models.CharField(max_length=100,null=True)
    carstatus = models.CharField(max_length=100,choices=CarStatus,null=True)
    action = models.CharField(max_length=255,null=True)
    clothingaccessories=models.CharField(max_length=100,choices=ClothingAccessoires,null=True)
    glasses = models.CharField(max_length=100,choices=Glasses,null=True)
    makeup = models.CharField(max_length=100,choices=Makeup,null=True)
    recordingstatus=models.CharField(max_length=100,choices=RecordingStatus,null=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=False)


