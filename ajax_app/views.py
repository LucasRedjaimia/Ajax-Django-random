from random import randint

from django.shortcuts import render
from django.views.generic import View
from django.http import * 

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

# Create your views here.
class AjaxHandler(View):
    def get(self, request):

        return render(request, 'ajax_app/index.html')

class Number(View, ):
    def get(self, request):
        if is_ajax(request):
            action = request.GET.get('action', None)
            if action == 'random':
                i = randint(1, 999)
                context = {}
                context['i'] = i

                return render(request, 'ajax_app/ajout.html', context)
            elif action == 'accueil':
                return render(request, 'ajax_app/init.html')
            else:
                return HttpResponse('problème')     
        else:
            return render(request, 'ajax_app/index2.html')
        