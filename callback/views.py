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



