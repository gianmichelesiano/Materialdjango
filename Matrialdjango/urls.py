from django.conf.urls import include, url
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('compilaGare.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]
