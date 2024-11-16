from django.db import models


class Post(models.Model):
	content = models.TextField()
	media = models.FileField(upload_to="mainapp_media/",)
	date_published = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.date_published}"