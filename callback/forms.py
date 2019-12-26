from django.forms import ModelForm

from .models import *



class CallbackOrderForm(ModelForm):
    class Meta:
        model = CallbackOrder
        fields = (
            'userName',
            'userPhone',
        )
