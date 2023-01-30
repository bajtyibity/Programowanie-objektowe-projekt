#widok ogólnie zapytania
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from app.models import Lekarz
from app.serializers import Lekarzserializers

from app.models import Pacjent
from app.serializers import Pacjentserializers

from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET','POST'])
def lekarze_lista(request):
    #stworzenie listy objektów
    if request.method == "GET":
        lekarze = Lekarz.object.all()

        #wyszukiwanie po imieniu w liscie objektów
        name=request.GET.get('name',None)
        if name is not None:
            lekarze = lekarze.filter(name__icontains=name)
        #serializer to formatu json
        lekarzserializers = Lekarzserializers(lekarze,many=True)
        return JsonResponse(lekarzserializers.data,safe=False)
    #jesli jest post przypisuje lekarzowi jego dane i zwraca czy dane są poprawne a jak nie wyswietla errory
    elif request.method == 'POST':
        lekarze_dane = JSONParser().parse(request)
        lekarzserializers = Lekarzserializers(data=lekarze_dane)
        if lekarzserializers.is_valid():
            lekarzserializers.save()
            return JsonResponse(lekarzserializers.data,status=status.HTTP_201_CREATED)
        return JsonResponse(lekarzserializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def lekarz_detail(request,pl):
    #obsługa błędów patrzenie czy istnieje
    try:
        lekarz=Lekarz.objects.get(pl=pl)
    except Lekarz.DoesNotExist:
        return JsonResponse({'message':'ten lekarz nie istnieje'},status=status.HTTP_404_NOT_FOUND)

    #jesli metoda post zwraca jsona z danymu lakarza
    if request.method=="GET":
        lekarzserializers = Lekarzserializers(Lekarz)
        return JsonResponse(lekarzserializers.data)
    #zapisuje lekarza tworzy
    elif request.method=="PUT":
        lekarz_data = JSONParser().parse(request)
        Lekarzserializers=Lekarzserializers(Lekarz,data=lekarz_data)
        if lekarzserializers.is_valid():
            lekarzserializers.save()
            return JsonResponse(lekarzserializers.data)
        return JsonResponse(lekarzserializers.errors,status=status.HTTP_400_BAD_REQUEST)
    #usuwa lekarza
    elif request.method=="DELETE":
        lekarz.delete()
        return JsonResponse({'message':'lekarz usuniety bezproblemowo XD'},status=status.HTTP_204_NO_CONTENT)

# pacjent

@api_view(['GET','POST'])
#stworzenie listy objektów
def pacjent_lista(request):
    if request.method == "GET":
        pacjent = Pacjent.object.all()

        #wyszukiwanie po imieniu w liscie objektów
        name=request.GET.get('name',None)
        if name is not None:
            pacjent = pacjent.filter(name__icontains=name)
        #serializer to formatu json
        pacjentserializers = Pacjentserializers(pacjent,many=True)
        return JsonResponse(pacjentserializers.data,safe=False)

     #jesli jest post przypisuje lekarzowi jego dane i zwraca czy dane są poprawne a jak nie wyswietla errory
    elif request.method == 'POST':
        pacjent_dane = JSONParser().parse(request)
        pacjentserializers = Pacjentserializers(data=pacjent_dane)
        if pacjentserializers.is_valid():
            pacjentserializers.save()
            return JsonResponse(pacjentserializers.data,status=status.HTTP_201_CREATED)
        return JsonResponse(pacjentserializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def pacient_detail(request,pl):
    #obsługa błędów jesli nie znaleziono
    try:
        pacjent=Pacjent.objects.get(pl=pl)
    except Pacjent.DoesNotExist:
        return JsonResponse({'message':'ten pacjent nie istnieje'},status=status.HTTP_404_NOT_FOUND)

    #jesli metoda post zwraca jsona z danymu lakarza
    if request.method=="GET":
        pacjentserializers = Pacjentserializers(Pacjent)
        return JsonResponse(pacjentserializers.data)
    
    #tworzy lekarza
    elif request.method=="PUT":
        pacjent_data = JSONParser().parse(request)
        Pacjentserializers=Pacjentserializers(Pacjent,data=pacjent_data)
        if pacjentserializers.is_valid():
            pacjentserializers.save()
            return JsonResponse(pacjentserializers.data)
        return JsonResponse(pacjentserializers.errors,status=status.HTTP_400_BAD_REQUEST)
    #usuwa lekarza
    elif request.method=="DELETE":
        pacjent.delete()
        return JsonResponse({'message':'pacjent usuniety bezproblemowo XD'},status=status.HTTP_204_NO_CONTENT)





