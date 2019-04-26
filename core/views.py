from django.shortcuts import render
from django.http import JsonResponse
from .models import Page
from .serializers import page_serializer

# Create your views here.


def search_view(request):
	query = request.GET.get('q', None)
#	page = request.GET.get('page', 1)
#	size = request.GET.get('size', 10)
	pages = Page.objects.filter(username__contains=query)	
#	_from = (int(page) - 1) * page_size
#	_to = int(page) * page_size
#	pages = pages[_from:_to]
		
	return JsonResponse(
		[page_serializer(page) for page in pages],
		safe=False
	)


def detail_view(request, username):
	try:
		page = Page.objects.get(username=username)
		return JsonResponse(page_serializer(page), status=200)
	except Page.DoesNotExist:
		return JsonResponse({
			'error': 'page not found'
		}, status=404)
"""
def ml_view(request):
	pass
"""
