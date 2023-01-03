from django import forms
from django.forms import ModelForm
from django import forms
from .models import Transaction
class TransactionForm(ModelForm):
    Your_Username = forms.TextInput()
    #user = forms.TextInput()
    amount = forms.TextInput()
    memo = forms.TextInput()
   # time = forms.TimeField()
    class Meta:
        model = Transaction
        fields = ['Your_Username', 'amount', 'memo']