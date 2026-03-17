from django.http import HttpResponse, JsonResponse
from .models import Note

def home(request):
	return HttpResponse("Welcome Home!")

def api_notes(request):
	# claude edit; makes it serialisable
	data = list(Note.objects.all().values('id', 'title', 'content'))
	return JsonResponse({'notes': data})