from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^index.html', views.index, name="index"),
    url(r'^about.html', views.about_view, name="about"),
    url(r'^contact.html', views.contact_view, name="contact"),
    url(r'^articles/(?P<slug>[\w-]+)/$', views.post_detail, name = 'post_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)