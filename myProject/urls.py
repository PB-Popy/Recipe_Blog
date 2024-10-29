from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from myProject.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',signupPage,name="signupPage"),
    path("signInPage/", signInPage, name="signInPage"),
    path("homePage/", homePage, name="homePage"),
    path("logoutPage/", logoutPage, name="logoutPage"),
    path("ProfilePage/", profilePage, name="profilePage"),

    path("addRecipePage/", addRecipePage, name="addRecipePage"),
    path("createdRecipePage/", createdRecipePage, name="createdRecipePage"),
    path("editRecipe/<str:recipe_id>", editRecipe, name="editRecipe"),

    path("deleteRecioe/<str:recipe_id>", deleteRecioe, name="deleteRecioe"),
    path("viewRecipe/<str:recipe_id>", viewRecipe, name="viewRecipe"),

    path("recipeFeed/", recipeFeed, name="recipeFeed"),

    path("editProfilePage/", editProfilePage, name="editProfilePage"),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
