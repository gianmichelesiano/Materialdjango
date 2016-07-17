from django.conf.urls import include, url, patterns
from django.conf.urls import url
from django.contrib import admin

"""
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('compilaGare.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]
"""


urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'', include('compilaGare.urls')),
    (r'^ckeditor/', include('ckeditor_uploader.urls')),
)