from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^atelier', views.atelier, name='atelier'),
    url(r'^(?P<artist>.*)/(?P<art_id>.*)/$', views.detail, name='detail'),
	# ex: /_58deg/5
	url(r'^(?P<artist>.*)/$', views.listing, name='listing'),
]
