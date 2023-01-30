from django.urls import include, re_path
from app import views

#wzorce url
urlpatterns = [
   re_path(r'^api/lekarze$',views.lekarze_lista),
    re_path(r'^api/lekarze/(?P<pl>[0-9]+)$',views.lekarz_detail),
    re_path(r'^api/pacjenci$',views.pacjent_lista),
    re_path(r'^api/pacjenci/(?P<pl>[0-9]+)$',views.pacjent_detail)

]
