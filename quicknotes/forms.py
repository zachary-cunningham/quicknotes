from django.forms import ModelForm
from .models import Note

# inherits from modelform
class NoteForm(ModelForm):
	class Meta:
		model = Note
		fields = ['title', 'content']