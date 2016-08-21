from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
import os

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
	return render(request, 'polls/index.html')
	
def atelier(request):
	return render(request, 'polls/atelier.html')

def merci(request):
	return render(request, 'polls/merci.html')
	
#def en_ce_moment(request):
#	return render(request, 'polls/en-ce-moment.html')
	
def contact(request):
	return render(request, 'polls/contact.html')
	
def les_copains(request):
	return render(request, 'polls/les-copains.html')
	
def detail(request, artist, art_id):
	file_list = os.listdir("mysite/static/%s/%s/" % (artist,art_id))
	img_list = []
	for p in file_list:
		if ((p.endswith(".jpg")) and not(p.startswith('.'))):
			img_list.append(p)
	detail_text_str = open("mysite/static/%s/%s.txt" % (artist,art_id)).read()
	
	detail_text = detail_text_str.split('|')
	
	for k in range (0,len(detail_text)):
		detail_text[k] = detail_text[k]#.replace("â€™", "'").encode('iso-8859-1')
		
		
	return render(request, 'polls/detail.html', {'artist':artist, 'art_id': art_id, 'img_list':img_list, 'detail_text':detail_text})
	#return HttpResponse("You're looking at <h1> %s </h1>" % artist)	
	
def listing(request, artist="58deg"):
	file_list = os.listdir("mysite/static/%s/" %artist)
	project_list = []
	for p in file_list:
		if (not p.endswith(".jpg") and not p.endswith(".txt") and not "Thumbs" in p):
			project_list.append(p)
	project_list.reverse()
	return render(request, 'polls/listing.html', {'artist':artist, 'project_list':project_list})
	
def en_ce_moment(request):
	file_list = os.listdir("mysite/static/en-ce-moment/")
	event_list = []
	for p in file_list:
		if (p.endswith(".jpg") ):
			event_name = p.replace('.jpg','')
			
			txt_str = open("mysite/static/en-ce-moment/%s.txt" % (event_name)).read()
			event_str = txt_str.encode('iso-8859-1')
			event_list.append([event_name, event_str])
			
	event_list.reverse()
	return render(request, 'polls/en-ce-moment.html', {'event_list':event_list})

def shop_listing(request, shop_category):
	file_list = os.listdir("mysite/static/%s/" %shop_category)
	project_list = []
	for p in file_list:
		if (not p.endswith(".jpg") and not p.endswith(".txt")):
			project_list.append(p)
	return render(request, 'polls/shop_listing.html', {'shop_category':shop_category, 'project_list':project_list})
	
	
def shop_detail(request, shop_category, art_id):
	img_list = os.listdir("mysite/static/%s/%s/" % (shop_category,art_id))
	detail_text = open("mysite/static/%s/%s.txt" % (shop_category,art_id)).read().encode('iso-8859-1')
	return render(request, 'polls/shop_detail.html', {'shop_category':shop_category, 'art_id': art_id, 'img_list':img_list, 'detail_text':detail_text})
	#return HttpResponse("You're looking at <h1> %s </h1>" % artist)
