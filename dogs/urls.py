# This is the app-level urls.py file, as it is located under dogs\urls.py. 
# This file had to be added, as it did not come with the project automatically.

# We have to use re_path instead of urls due to an error with urls.

# Imports the classes from the views.py file.
from django.urls import re_path
from dogs import views

urlpatterns = [

    # References the DogList class from the views.py file.
    re_path(r'^dogs/$', 
        views.DogList.as_view(), 
        name=views.DogList.name),

    # References the DogDetail class from the views.py file.    
    re_path(r'^dogs/(?P<pk>[0-9]+)/$', 
        views.DogDetail.as_view(),
        name=views.DogDetail.name),

    # References the BreedList class from the views.py file.    
    re_path(r'^breeds/$', 
        views.BreedList.as_view(),
        name=views.BreedList.name),

    # References the BreedDetail class from the views.py file.    
    re_path(r'^breeds/(?P<pk>[0-9]+)/$', 
        views.BreedDetail.as_view(),
        name=views.BreedDetail.name),

    # This is the root URL.
    re_path(r'^dogs-api/$',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name),
]
