from django.shortcuts import render, get_object_or_404
from .models import Personagem

def index (request):
    personagens = Personagem.objects.all()
    return render(request, 'home/index.html', {
        'personagens': personagens
    })
"""
def info_personagem (request, personagem_Nome):
    # info = Personagem.objects.get(Nome=personagem_Nome)
    info = get_object_or_404(Personagem, Nome=personagem_Nome)
    return render(request, 'home/info_personagem.html', {
        'info': info
    })
"""