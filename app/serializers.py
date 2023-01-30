from rest_framework import serializers
from app.models import Lekarz
from app.models import Pacjent

#serializer dla lekarza
class Lekarzserializers(serializers.ModelSerializer):
    class Meta:
        model = Lekarz
        fields = ('lekarz_id','imie','nazwisko')

#serializer dla pacjenta
class Pacjentserializers(serializers.ModelSerializer):
    class Meta:
        model = Pacjent
        fields = ('pacjent_id','imie','nazwisko')

