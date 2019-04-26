from django.urls import path
from .views import search_view, detail_view#, ml_view


urlpatterns = [
    path('search/', search_view),
	path('page/@<str:username>/', detail_view),
#	path('page/@{username}/ml/', ml_view),
]
