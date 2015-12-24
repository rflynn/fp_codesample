from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get$', views.get, name='get'),
    #url(r'^$', views.index, name='index'),
]
