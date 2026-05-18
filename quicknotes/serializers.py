from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from quicknotes.models import Note, Collection



class CollectionSerializer(ModelSerializer):
	# notes = NoteSerializer(many=True, read_only=True)
	class Meta:
		model = Collection
		fields = "__all__"

class NoteSerializer(ModelSerializer):
	collection_data = CollectionSerializer(source="collection", read_only=True)

	# this is API level validation, not DB or front-end
	# content = serializers.CharField(required=False, allow_blank=True, default="")
	class Meta:
		model = Note
		fields = "__all__"