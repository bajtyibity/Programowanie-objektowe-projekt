from django.urls import include, re_path
from app import views

#wzorce url
urlpatterns = [
    re_path(r'^api/app$',views.lekarze_lista),
    re_path(r'^api/app/(?P<pk>[0-9]+)$',views.lekarze_lista),
    re_path(r'^api/app$',views.pacjent_lista),
    re_path(r'^api/app/(?P<pk>[0-9]+)$',views.pacjent_lista)
]
