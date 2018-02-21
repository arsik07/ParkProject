from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.start_page, name='start'),
    url(r'^places/$', views.places, name='places'),
    url(r'^places/(?P<park_id>\d+)/$', views.place_details, name='details'),
    url(r'^get_marks/$', views.get_review_marks, name='marks'),
    url(r'^get_parks/$', views.get_parks, name='parks'),
    url(r'^get_cafes/$', views.get_cafes, name='cafes'),
    url(r'^get_aquas/$', views.get_aquas, name='aquas'),
    url(r'^get_cinemas/$', views.get_cinemas, name='cinemas'),
    url(r'^about/$', views.about, name='about'),
]