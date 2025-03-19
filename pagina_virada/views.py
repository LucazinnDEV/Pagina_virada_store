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

        return render(request, 'pagina_virada/index.html', contexto)
    
class PerguntaView (View) :
    def get (self, request, pergunta_id) :
        try :
            pergunta = Pergunta.objects.get(pk=pergunta_id)
        except Pergunta.DoesNotExist :
            raise Http404("Pergunta não encontrada")
        contexto = {'pergunta' : pergunta}

        return render(request, 'pagina_virada/delahte.html', contexto)
    
class VotoView (View) :
    def get (self, request, resposta_id) :
        try :
            resposta = Resposta.objects.get(pk = resposta_id)
        except resposta.DoesNotExist :
            raise HttpResponse(str(resposta) + "; votos: " + str(resposta.votos))
        
    def post (self, request, resposta_id) :
        try :
            resposta = Resposta.objects.get(pk = resposta_id)
        except resposta.DoesNotExist :
            raise Http404("Pergunta não encontrada")
            resposta.votos += 1
            resposta.save()
            return redirect(reverse('projeto:detalhe', agrs = [resposta.pergunta.id]))
        
class InserirPerguntaView (View) :
    def get (self, request) :
        return render (request, 'pagina_virada/inserir_pergunta.html')
    
    def post (self, request) :
        if request.user.is_authenticadet :
            usuario = request.ucer.username
        else :
            usuario = "anonimo"
            titulo = request.POST.get('titulo')
            detalhe = request.POST.get('detalhe')
            tentativa = request.POST.get('tentativa')
            data_criacao = timezone.now()
            pergunta = Pergunta(titulo = titulo, detalhe = detalhe, tentativa = tentativa, data_criacao = data_criacao, usuario = usuario)
        
        pergunta.save()
        return redirect(reverse('projeto:detalhe', args = [pergunta.id]))
    

