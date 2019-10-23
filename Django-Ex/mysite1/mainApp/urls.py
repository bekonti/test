from django.conf.urls import url, include
from . import views

urlpatterns = [
	url('',	views.index, name = 'index'),
	# url('hey',	views.hey, name = 'hey')

]