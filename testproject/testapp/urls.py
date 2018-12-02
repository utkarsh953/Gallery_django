from django.urls import include, path

from .views import photo_list


urlpatterns = [
    path('home/', photo_list, name='main-view'),
    
]