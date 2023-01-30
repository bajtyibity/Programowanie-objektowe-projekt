from django.contrib import admin
from .models import Lekarz
from .models import Pacjent
# Register your models here.

#dodanie modelu lekarza i pacjenta do strony admina
admin.site.register(Lekarz)
admin.site.register(Pacjent)