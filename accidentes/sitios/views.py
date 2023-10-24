from django.shortcuts import render
from django.http import HttpResponse

from .models import Lugar
# Create your views here.
# def index(request):
#     latest_question_list = Lugar.objects.order_by('-Av.Panamerica')[:]
#     output = ','.join([q.question_text for q in lates_question_list])  
#     return HttpResponse(output)