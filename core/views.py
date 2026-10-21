from django.shortcuts import render
from .models import Modalidade, Turma


def inicio(request):
    modalidades = Modalidade.objects.all()

    return render(
        request,
        'inicio.html',
        {'modalidades': modalidades}
    )


def turmas(request):
    lista = Turma.objects.all()

    return render(
        request,
        'turmas.html',
        {'turmas': lista}
    )