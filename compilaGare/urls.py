from . import views
from django.conf.urls import include, url


urlpatterns = [             
    url(r'^$', views.index, name='index'),   
    url(r'^soggetto/new/$', views.soggetto_new, name='soggetto_new'),
    url(r'^soggetto/(?P<pk>[0-9]+)/$', views.soggetto_detail, name='soggetto_detail'),
    url(r'^soggetto/(?P<pk>[0-9]+)/edit/$', views.soggetto_edit, name='soggetto_edit'),
    url(r'^soggetto/list/$', views.soggetto_list, name='soggetto_list'),  

    url(r'^gara/new/$', views.gara_new, name='gara_new'),
    url(r'^gara/list/$', views.gara_list, name='gara_list'),
    url(r'^gara/(?P<pk>[0-9]+)/edit/$', views.gara_edit, name='gara_edit'),     
    
    url(r'^doc_base/$', views.doc_base, name='doc_base'),
    url(r'^tabella/$', views.tabella, name='tabella'),
    
    url(r'^accounts/', include('registration.backends.simple.urls')), 
]
 