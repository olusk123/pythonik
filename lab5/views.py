from rest_framework import viewsets
from .models import Osoba, Stanowisko
from .serializers import OsobaSerializer, StanowiskoSerializer

class OsobaViewSet(viewsets.ModelViewSet):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer

class StanowiskoViewSet(viewsets.ModelViewSet):
    queryset = Stanowisko.objects.all()
    serializer_class = StanowiskoSerializer