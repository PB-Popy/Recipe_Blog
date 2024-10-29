from django.db import models
from django.contrib.auth.models import AbstractUser

class customUser(AbstractUser):
    
    USER=[
        ('creator','Creator'),
        ('viewers','Viewers'),
    ]
    user_type=models.CharField(choices=USER,max_length=100,null=True)
    Profile_Pic=models.ImageField(upload_to='Media/Profile_Pic',null=True)
    
    def __str__(self):  
        
        return f"{self.username}"
    
class viewersProfileModel(models.Model):

    SPECIALITIES=[
        ('desserts','Desserts'),
        ('vegan_recipes','vegan_recipes'),
    ]
    
    
    user=models.OneToOneField(customUser,on_delete=models.CASCADE,related_name='viewersProfile')
    interest=models.CharField(choices=SPECIALITIES,max_length=100,null=True)
    favourite_food=models.CharField(max_length=100,null=True)
   
    
    def __str__(self):
        return f"{self.user.username}"
    
    
class creatorProfileModel(models.Model):

    SPECIALITIES=[
        ('desserts','Desserts'),
        ('vegan_recipes','vegan_recipes'),
    ]
   
    user = models.OneToOneField(customUser, on_delete=models.CASCADE,related_name='creatorProfile')
    
    profile_picture = models.ImageField(upload_to='Media/profile_pictures', blank=True, null=True)
    bio = models.TextField(blank=True)
    specialties=models.CharField(choices=SPECIALITIES,max_length=100,null=True)
    followers=models.PositiveIntegerField(null=True)
    website = models.URLField(blank=True)
    social_media_links = models.URLField(blank=True, null=True)
   
    def __str__(self):
        return f"{self.user.username}"
    

class RecipeModel(models.Model):
    
    TAG=[
        ('vegetarian','Vegetarian'),
        ('non_Vegetarian','Non-Vegetarian')
    ]
    CATEGORY=[
        ('breakfast','Breakfast'),
        ('lunch','Lunch'),
        ('dinner','Dinner'),
    ]
    DIFFICULTY=[
        ('easy','Easy'),
        ('medium','Medium'),
        ('hard','Hard'),
    ]
    
    user=models.ForeignKey(customUser, on_delete=models.CASCADE, related_name='recipemodel')
    
    Category=models.CharField(choices=CATEGORY,max_length=100,null=True)
    difficulty=models.CharField(choices=DIFFICULTY,max_length=100,null=True)
    tag=models.CharField(choices=TAG,max_length=100,null=True)

    title=models.CharField(max_length=100,null=True)
    ingredients=models.TextField(null=True)
    instructions=models.TextField(null=True)
    prep_time=models.PositiveIntegerField(null=True)
    cooking_time=models.PositiveIntegerField(null=True)
    total_time=models.PositiveIntegerField(null=True)
    nutrition=models.TextField(null=True)
    image=models.ImageField(upload_to='Media/image' ,null=True)
    calories=models.PositiveIntegerField(null=True)
    
    def __str__(self):
        return f"{self.user.username}- {self.title}"
    
  