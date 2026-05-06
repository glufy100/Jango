from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'myfirstapp/index.html')

def formulaire(request):
    """Afficher le formulaire simple (méthode GET dans le template actuel)."""
    return render(request, 'myfirstapp/formulaire.html')


def bonjour(request):
    """Récupère le paramètre 'nom' en GET et affiche la page de salutations."""
    nom = request.GET.get('nom', '')
    # Empêcher des valeurs vides d'afficher une chaîne vide
    if not nom:
        nom = 'inconnu'
    return render(request, 'myfirstapp/bonjour.html', {'nom': nom})

