from django.shortcuts import render


def index(request):
    return render(request, 'myfirstproject.html')


def page2(request):
    """Renvoie la page statique myfirstproject2.html située dans le dossier de templates.

    Le dossier des templates inclut déjà `BASE_DIR / 'myfirstproject'` dans `settings.TEMPLATES['DIRS']`,
    donc le fichier `myfirstproject2.html` peut être rendu directement.
    """
    return render(request, 'myfirstproject2.html')


def bonjour(request):
    nom = request.GET.get('nom', '')
    return render(request, 'bonjour.html', {'nom': nom})
