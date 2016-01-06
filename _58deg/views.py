from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
import os

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
	return render(request, 'polls/index.html')
	
def atelier(request):
	return render(request, 'polls/atelier.html')
	
def en_ce_moment(request):
	return render(request, 'polls/en-ce-moment.html')
	
def detail(request, artist, art_id):
	
	#img_list = os.listdir("static/_58deg/")
	img_list = os.listdir("mysite/static/%s/%s/" % (artist,art_id))
	return render(request, 'polls/detail.html', {'artist':artist, 'art_id': art_id, 'img_list':img_list})
	#return HttpResponse("You're looking at <h1> %s </h1>" % artist)

def listing(request, artist):
	file_list = os.listdir("mysite/static/%s/" %artist)
	project_list = []
	for p in file_list:
		if (not p.endswith(".jpg")):
			project_list.append(p)
	return render(request, 'polls/listing.html', {'artist':artist, 'project_list':project_list})
	