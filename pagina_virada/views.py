from django.shortcuts import render
from .models import Pergunta, Resposta
from django.views import View
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import redirect
from django.urls import reverse 

class MainView (View) :
    def get (self, request) :
        lista_ultimas_questoes = Pergunta.objects.oreder_by("-data_criacao")
        contexto = {'perguntas' : lista_ultimas_questoes}

        return render(request, 'projeto/index.html', contexto)
    

