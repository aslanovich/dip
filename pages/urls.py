from django.conf.urls import url
from pages import views

urlpatterns = [
    url(r'^login$', views.user_login),
    url(r'^logout$', views.user_logout),
    url(r'^(\w+)$', views.clientView),
    url(r'^administrator/(\w+)$', views.administratorView),
    url(r'^plan/$', views.createPlan),
]
