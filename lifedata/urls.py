from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.ListCreateSleep.as_view(), name='sleep_list'),
	url(r'(?P<pk>\d+)/$', views.RetrieveUpdateDestroySleep.as_view(), name="sleep_detail"),
]