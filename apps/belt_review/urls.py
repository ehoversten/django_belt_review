from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    # url(r'^login$', views.register),
    # url(r'^dashboard/(?P<user_id>\d+)$', views.dashboard),
    # url(r'^shoes$', views.shoes),
    # url(r'^logout$', views.logout),
    # url(r'^buy$', views.buy),
    # url(r'^sell$', views.sell),
    # url(r'^remove$', views.remove),
]
