from django.conf.urls import url
# from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^project$', views.project),
    url(r'^about$', views.about),
    url(r'^testimonials$', views.testimonials)

]
