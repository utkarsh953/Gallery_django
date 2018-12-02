from django.shortcuts import render
from django.http import HttpResponse
from .models import Photos

# Create your views here.
def photo_list(request):
	queryset = Photos.objects.all()
	context = {
	"photos" : queryset 
	}
	return render (request,"photos.html",context)