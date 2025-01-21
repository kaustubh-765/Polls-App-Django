from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^create/$', views.create_poll, name='create_poll'),
    re_path(r'^(?P<poll_id>\d+)/add_choices/$', views.add_choices, name='add_choices'),
    re_path(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    re_path(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
]
