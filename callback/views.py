from django.http import JsonResponse

import time

from .forms import *





def createCallbackForm(request):
    return_dict = {}
    if request.POST:
        req = request.POST
        if '_' in req.get('userPhone'):
            return_dict['result'] = 'phone'
        else:
            form = CallbackOrderForm(request.POST)
            if form.is_valid():

                form.save()
                return_dict['result'] = 'ok'

            else:
                return_dict['result'] = 'name'

                print(form.errors)
        return JsonResponse(return_dict)


def createQuiz(request):
    print(request.POST)
    return_dict = {}
    if request.POST:
        req=request.POST
        if not req.get('name'):
            print('error name')
            return_dict['result'] = 'name'
        elif '_' in req.get('phone'):
            print('error phone')
            return_dict['result'] = 'phone'
        else:
            Quiz.objects.create(userName=req.get('name'),
                                userPhone=req.get('phone'),
                                question1=req.get('tab1-q'),
                                question2=req.get('tab2-q'),
                                question3=req.get('tab3-q'),
                                question4=req.get('tab4-q'),
                                question5=req.get('tab5-q'),

                                )
            return_dict['result'] = 'ok'
        return JsonResponse(return_dict)
