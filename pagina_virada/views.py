from django.shortcuts import render
from .models import Pergunta, Resposta
from django.views import View
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import redirect
from django.urls import reverse 


