from django.shortcuts import render,redirect

from myApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def signupPage(request):
    
    if request.method=='POST':
        
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        Confirm_password=request.POST.get("Confirm_password")
        Profile_Pic=request.FILES.get("Profile_Pic")
        user_type=request.POST.get("user_type")
    
        
        if password==Confirm_password:
            
            
            user=customUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                Profile_Pic=Profile_Pic,
                user_type=user_type,
            )
            if user_type=='seeker':
                viewersProfileModel.objects.create(user=user)
                
            elif user_type=='recruiter':
                creatorProfileModel.objects.create(user=user)
            
            return redirect("signInPage")
            
    return render(request,"signupPage.html")


def signInPage(request):
    if request.method == 'POST':
        
        user_name=request.POST.get("username")
        pass_word=request.POST.get("password")

        try:
            user = authenticate(request, username=user_name, password=pass_word)

            if user is not None:
                login(request, user)
                return redirect('homePage') 
            else:
                return redirect('signInPage')

        except customUser.DoesNotExist:
            return redirect('signInPage')

    return render(request, 'signInPage.html')

@login_required
def homePage(request):
    
    
    return render(request,"homePage.html")


def logoutPage(request):
    
    logout(request)
    
    return redirect('signInPage')

@login_required
def profilePage(request):
    
    return render(request,"profilePage.html")


@login_required
def addRecipePage(request):

    current_user=request.user
    if current_user.user_type == "creator":
        if request.method=="POST":
            recipe=RecipeModel()
            recipe.user=current_user
            recipe.Category=request.POST.get("Category")
            recipe.difficulty=request.POST.get("difficulty")
            recipe.tag=request.POST.get("tag")
            recipe.title=request.POST.get("title")
            recipe.ingredients=request.POST.get("ingredients")
            recipe.instructions=request.POST.get("instructions")
            recipe.prep_time=request.POST.get("prep_time")
            recipe.cooking_time=request.POST.get("cooking_time")
            recipe.total_time=request.POST.get("total_time")
            recipe.nutrition=request.POST.get("nutrition")
            recipe.image=request.FILES.get("image")
            recipe.calories=request.POST.get("calories")

            
            recipe.save()
           
            return redirect("recipeFeed")
    
    return render(request,"addRecipePage.html")

@login_required
def createdRecipePage(request):

    current_user=request.user
    recipe=RecipeModel.objects.filter()

    context= {
        'recipe': recipe
    }
    
    return render(request,"createdRecipePage.html",context)

@login_required
def recipeFeed(request):

    current_user=request.user
    recipe=RecipeModel.objects.all()

    context= {
        'recipe': recipe
    }
    
    return render(request,"recipeFeed.html",context)

@login_required
def deleteRecioe(request,recipe_id):

    recipe=RecipeModel.objects.filter(id=recipe_id)
    recipe.delete()

    
    return redirect("createdRecipePage")


@login_required
def viewRecipe(request,recipe_id):

    recipe=RecipeModel.objects.filter(id=recipe_id)

    context= {
        'recipe': recipe
    }
    
    return render(request,"viewRecipe.html",context)


@login_required
def editRecipe(request,recipe_id):

    recipe=RecipeModel.objects.get(id=recipe_id)

    context= {
        'recipe': recipe
    }

    current_user=request.user

    if current_user.user_type == "creator":

        if request.method=="POST":

            if request.FILES.get("image"):
                recipe_img = request.FILES.get("image")
            else:
                recipe_img = recipe.image

            recipes = RecipeModel (

                user=current_user,
                id=request.POST.get("recipe_id"),
                Category=request.POST.get("Category"),
                difficulty=request.POST.get("difficulty"),
                tag=request.POST.get("tag"),
                title=request.POST.get("title"),
                ingredients=request.POST.get("ingredients"),
                instructions=request.POST.get("instructions"),
                prep_time=request.POST.get("prep_time"),
                cooking_time=request.POST.get("cooking_time"),
                total_time=request.POST.get("total_time"),
                nutrition=request.POST.get("nutrition"),
                image=recipe_img,
                calories=request.POST.get("calories")
            )
            

            
            recipes.save()
           
            return redirect("createdRecipePage")
    
    return render(request,"editRecipe.html",context)


@login_required
def editProfilePage(request):
    
    
    
    current_user=request.user
    
    if request.method=='POST':
        current_user.username=request.POST.get("username")
        current_user.email=request.POST.get("email")
        current_user.recipe_id=request.POST.get("recipe_id")
        current_user.Profile_Pic=request.FILES.get("profile_pic")
        
    
            
        try:
            viewersProfile=viewersProfileModel.objects.get(user=current_user)
            viewersProfile.interest=current_user.viewersProfile.interest
            viewersProfile.favourite_food=current_user.viewersProfile.favourite_food
            viewersProfile.save()
            current_user.save()
            
            return redirect("profilePage")
            
        except viewersProfileModel.DoesNotExist:
            viewersProfile=None
            
        try:
            creatorProfile=creatorProfileModel.objects.get(user=current_user)
            
            creatorProfile.bio=request.POST.get("bio")
            creatorProfile.specialties=request.POST.get("specialties")
            creatorProfile.followers=request.POST.get("followers")
            creatorProfile.website=request.POST.get("website")
            creatorProfile.social_media_links=request.POST.get("social_media_links")
            creatorProfile.save()
            current_user.save()
            
            return redirect("profilePage")
            
        except creatorProfileModel.DoesNotExist:
            creatorProfile=None
    
    return render(request, "editProfilePage.html")