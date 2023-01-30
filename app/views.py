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
    if request.method == "GET":
        lekarze = Lekarz.objects.all()

        name=request.GET.get('imie',None)
        if name is not None:
            lekarze = lekarze.filter(name__icontains=name)

        lekarzserializers = Lekarzserializers(lekarze,many=True)
        return JsonResponse(lekarzserializers.data,safe=False)

    elif request.method == 'POST':
        lekarze_dane = JSONParser().parse(request)
        lekarzserializers = Lekarzserializers(data=lekarze_dane)
        if lekarzserializers.is_valid():
            lekarzserializers.save()
            return JsonResponse(lekarzserializers.data,status=status.HTTP_201_CREATED)
        return JsonResponse(lekarzserializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def lekarz_detail(request,pl):
    try:
        lekarz=Lekarz.objects.get(lekarz_id=pl)
    except Lekarz.DoesNotExist:
        return JsonResponse({'message':'ten lekarz nie istnieje'},status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        lekarz_serializers = Lekarzserializers(lekarz)
        return JsonResponse(lekarz_serializers.data)
    
    elif request.method=="PUT":
        lekarz_data = JSONParser().parse(request)
        Lekarz_serializers=Lekarzserializers(lekarz,data=lekarz_data)
        if Lekarz_serializers.is_valid():
           Lekarz_serializers.save()
           return JsonResponse(Lekarz_serializers.data)
        return JsonResponse(Lekarz_serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=="DELETE":
        lekarz.delete()
        return JsonResponse({'message':'lekarz usuniety bezproblemowo XD'},status=status.HTTP_204_NO_CONTENT)

# pacjent
#widok ogólnie zapytania
@api_view(['GET','POST'])
def pacjent_lista(request):
    if request.method == "GET":
        pacjenci = Pacjent.objects.all()

        name=request.GET.get('imie',None)
        if name is not None:
            pacjenci = pacjenci.filter(name__icontains=name)

        pacjentserializers = Pacjentserializers(pacjenci,many=True)
        return JsonResponse(pacjentserializers.data,safe=False)

    elif request.method == 'POST':
        Pacjent_dane = JSONParser().parse(request)
        pacjentserializers = Pacjentserializers(data=Pacjent_dane)
        if pacjentserializers.is_valid():
            pacjentserializers.save()
            return JsonResponse(pacjentserializers.data,status=status.HTTP_201_CREATED)
        return JsonResponse(pacjentserializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def pacjent_detail(request,pl):
    try:
        pacjent=Pacjent.objects.get(pacjent_id=pl)
    except Pacjent.DoesNotExist:
        return JsonResponse({'message':'ten pacjent nie istnieje'},status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        pacjent_serializers = Pacjentserializers(pacjent)
        return JsonResponse(pacjent_serializers.data)
    
    elif request.method=="PUT":
        pacjent_data = JSONParser().parse(request)
        pacjent_serializers=Pacjentserializers(pacjent,data=pacjent_data)
        if pacjent_serializers.is_valid():
           pacjent_serializers.save()
           return JsonResponse(pacjent_serializers.data)
        return JsonResponse(pacjent_serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=="DELETE":
        pacjent.delete()
        return JsonResponse({'message':'pacjent usuniety bezproblemowo XD'},status=status.HTTP_204_NO_CONTENT)
