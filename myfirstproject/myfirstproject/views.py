from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def formulaire(request):
    return render(request, 'formulaire.html')


def bonjour(request):
    nom = request.GET.get('nom', '')
    return render(request, 'bonjour.html', {'nom': nom})
