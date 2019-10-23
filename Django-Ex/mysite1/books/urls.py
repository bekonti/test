from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
	url('',	views.index, name = 'index'),
	url('hey',	views.hey, name = 'hey')

]