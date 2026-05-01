from django.db import models

class Note(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	tag = models.TextField(blank=True)

	def __str__(self):
		return self.title

	def __repr__(self):
		return self.__str__()