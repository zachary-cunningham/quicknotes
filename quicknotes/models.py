from django.db import models

# inherit from a model
class Note(models.Model):
	# defined at class level
	# research why, as well as Django Model documentation
	title = models.CharField(max_length=255)
	content = models.TextField()

	def __str__(self) -> str:
		return self.title
	
	def __repr__(self) -> str:
		return self.__str__()