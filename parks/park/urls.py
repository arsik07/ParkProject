from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.start_page, name='start'),
    url(r'^places/$', views.places, name='places'),
    url(r'^places/(?P<park_id>\d+)/$', views.place_details, name='details'),
    url(r'^get_marks/$', views.get_review_marks, name='marks')
]