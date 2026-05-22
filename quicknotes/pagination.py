from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response

class CustomPagination(LimitOffsetPagination):
	default_limit = 5
	
	def get_paginated_response(self, data):
		return Response({
			"count": self.count,
			"next": self.get_next_link(),
			"previous": self.get_previous_link(),
			"data": data
		})