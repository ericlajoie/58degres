from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^atelier', views.atelier, name='atelier'),
	url(r'^contact', views.contact, name='contact'),
	url(r'^merci', views.merci, name='merci'),
	url(r'^les-copains', views.les_copains, name='les_copains'),
	url(r'^en-ce-moment', views.en_ce_moment, name='en_ce_moment'),
        url(r'^art/(?P<artist>.*)/(?P<art_id>.*)/$', views.detail, name='detail'),
        url(r'^shop/(?P<shop_category>.*)/(?P<art_id>.*)/$', views.shop_detail, name='shop_detail'),
	# ex: /_58deg/5
	url(r'^art/(?P<artist>.*)/$', views.listing, name='listing'),
	url(r'^shop/(?P<shop_category>.*)/$', views.shop_listing, name='shop_listing'),
]
