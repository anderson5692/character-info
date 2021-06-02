from django.shortcuts import render, get_object_or_404
from .models import Personagem


def index(request):
    personagens = Personagem.objects.all()
    return render(request, 'home/index.html', {
        'personagens': personagens
    })


def Finn(request):
    personagens = get_object_or_404(Personagem, id=1)
    return render(request, 'home/Finn.html', {
        'personagens': personagens
    })


def Jake(request):
    personagens = get_object_or_404(Personagem, id=2)
    return render(request, 'home/Jake.html', {
        'personagens': personagens
    })


def Marceline(request):
    personagens = get_object_or_404(Personagem, id=3)
    return render(request, 'home/Marceline.html', {
        'personagens': personagens
    })


def Princesacaroco(request):
    personagens = get_object_or_404(Personagem, id=10)
    return render(request, 'home/Princesacaroco.html', {
        'personagens': personagens
    })


def Princesajujuba(request):
    personagens = get_object_or_404(Personagem, id=4)
    return render(request, 'home/Princesajujuba.html', {
        'personagens': personagens
    })


def Princesadefogo(request):
    personagens = get_object_or_404(Personagem, id=5)
    return render(request, 'home/Princesadefogo.html', {
        'personagens': personagens
    })


def BMO(request):
    personagens = get_object_or_404(Personagem, id=9)
    return render(request, 'home/BMO.html', {
        'personagens': personagens
    })


def Ladyiris(request):
    personagens = get_object_or_404(Personagem, id=8)
    return render(request, 'home/Ladyiris.html', {
        'personagens': personagens
    })


def Reigelado(request):
    personagens = get_object_or_404(Personagem, id=7)
    return render(request, 'home/Reigelado.html', {
        'personagens': personagens
    })


def Lich(request):
    personagens = get_object_or_404(Personagem, id=6)
    return render(request, 'home/Lich.html', {
        'personagens': personagens
    })


# personagens = Personagem.objects.get(id=6) - substituido pelo "get_object_or_404"
"""
def info_personagem (request, personagem_Nome):
    # info = Personagem.objects.get(Nome=personagem_Nome)
    info = get_object_or_404(Personagem, Nome=personagem_Nome)
    return render(request, 'home/info_personagem.html', {
        'info': info
    })
"""
