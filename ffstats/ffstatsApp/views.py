from django.http import HttpResponse
from django.shortcuts import render

def search(request):
	error = False
	if 'player' in request.GET:
		player = request.GET['player']
		if not player:
			error = True
		else:
			return render(request, 'index.html')
	else:
		return render(request, 'index.html')