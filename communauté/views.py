from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Membre, Reunion, Cotisation, Projet, Financement, Versement

def index(request):
    return HttpResponse("Bienvenue à la gestion de la communauté BATOUFAM")

def liste_membres(request):
    membres = Membre.objects.all()
    return render(request, 'communauté/liste_membres.html', {'membres': membres})

def detail_membre(request, membre_id):
    membre = get_object_or_404(Membre, pk=membre_id)
    return render(request, 'communauté/detail_membre.html', {'membre': membre})

# Ajoutez des vues supplémentaires pour les autres modèles selon les besoins.
