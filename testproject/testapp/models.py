from django.db import models

# Create your models here.
class Photos(models.Model):
	title = models.CharField(max_length=100)
	# height = models.IntegerField(default=0)
	# width = models.IntegerField(default=0)
	image = models.ImageField(blank=True,null=True)
	time_stamp = models.DateTimeField(auto_now=True,auto_now_add=False)

	def __str__(self):
		return self.title
	class Meta:
		ordering = ['time_stamp']	