from django.shortcuts import render
from django.http import HttpResponseBadRequest, JsonResponse
from django.contrib.auth.decorators import login_required

from config.template_name import GENERATOR_TEMPLATE

@login_required
def generator_page(request):
    return render(request, GENERATOR_TEMPLATE)


def generator_handler(request):
    if request.method == 'GET':
       _type = int(request.GET.get('generator_type', 1))
       input_box_text = request.GET.get('input_box_text', '')

       if _type == 1:
           system = "You are a sales man assistant"
           print(system, input_box_text)
           return JsonResponse({_type:input_box_text})
       
       if _type == 2:
           system = "Something"
           print(system, input_box_text)
           return JsonResponse({_type:input_box_text})
       
       if _type == 3:
           system = "Something"
           print(system, input_box_text)
           return JsonResponse({_type:input_box_text})
       
       if _type == 4:
           system = "Something"
           print(system, input_box_text)
           return JsonResponse({_type:input_box_text})
       
       if _type == 5:
           system = "Something"
           print(system, input_box_text)
           return JsonResponse({_type:input_box_text})
       
       if _type == 6:
           system = "Something"
           print(system, input_box_text)
           return JsonResponse({_type:input_box_text})       
       
       if _type == 7:
           system = "Something"
           print(system, input_box_text)
           return JsonResponse({_type:input_box_text})       
       if _type == 8:
           system = "Something"
           print(system, input_box_text)
           return JsonResponse({_type:input_box_text})
       
    return HttpResponseBadRequest('Invalid or missing _type parameter')