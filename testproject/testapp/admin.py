from django.contrib import admin
from .models import Photos
# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
	list_display=['title','time_stamp']
	class Meta:
		model=Photos
admin.site.register(Photos,PhotoAdmin)		