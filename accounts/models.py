from __future__ import unicode_literals
#from typing_extensions import *
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import FloatField
from django.forms.fields import FloatField as FloatFormField
#model_field = FloatField()
#form_field = model_field.formfield(localize=True)
statuses = (
  #  ('Interest-Free Loan Issued', 'Interest-Free Loan Issued'),
 #   ('MT Realtor Payment - Transaction should start with "-".','MT Realtor Payment - Transaction should start with "-".'),
  #  ('Loan Paid Off','Loan Paid Off'),
    ('Approved','Approved'),
    ('Declined','Declined'),
    )

ppl = (
  #  ('Interest-Free Loan Issued', 'Interest-Free Loan Issued'),
 #   ('MT Realtor Payment - Transaction should start with "-".','MT Realtor Payment - Transaction should start with "-".'),
  #  ('Loan Paid Off','Loan Paid Off'),
    ('CH','CH'),
    ('SA','SA'),
    ('SL','SL'),

    )


t_type = (
  #  ('Interest-Free Loan Issued', 'Interest-Free Loan Issued'),
 #   ('MT Realtor Payment - Transaction should start with "-".','MT Realtor Payment - Transaction should start with "-".'),
  #  ('Loan Paid Off','Loan Paid Off'),
    ('Interest-Free Loan for MTRealtor','Interest-Free Loan for MTRealtor'),
    ('Pay off your Interest-Free Loan','Pay off your Interest-Free Loan'),
    ('MTRealtor Withdrawal - Purchase Listing on MTRealtor','MTRealtor Withdrawal - Purchase Listing on MTRealtor'),

    )

'''
from accounts.models import Transaction, t_type
class TransactionForm(ModelForm):
    Your_Username = forms.TextInput()
    Transaction_Type = forms.TextInput(choices=t_type)
    amount = forms.TextInput()
    memo = forms.TextInput()
   # time = forms.TimeField()
    class Meta:
        model = Transaction
        fields = ['Your_Username','Transaction_Type', 'amount', 'memo']
    Your_Username = models.CharField(max_length=100, blank=True)  

'''

# Create your models here.
class balance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField()
    username = models.CharField(blank=True, max_length=100, help_text='This is for the HTML form. Do not manually type anything here if you are a superuser or things will mess up.')
    memo = models.CharField(blank=True, max_length=100, help_text='This is for the HTML form. Do not manually type anything here if you are a superuser or things will mess up.')#), choices=memos)
    paper = models.CharField(blank=True, max_length=100, help_text='This is for the HTML form. Do not manually type anything here if you are a superuser or things will mess up.')
    pencil = models.CharField(blank=True, max_length=100, help_text='This is for the HTML form. Do not manually type anything here if you are a superuser or things will mess up.')
    time = models.CharField(blank=True, max_length=100, help_text='This is for the HTML form. Do not manually type anything here if you are a superuser or things will mess up.')

class Transaction(models.Model):
    Your_Username = models.CharField(max_length=100, blank=True)
    Transaction_Type = models.CharField(max_length=100, blank=True, choices=t_type)  
 #  user = models.CharField(max_length=100, blank=True)  
    amount = models.CharField(max_length=100, blank=True)
    memo = models.CharField(max_length=100, blank=True)
   # status_time = models.DateTimeField(blank=True, required=False, help_text='Please specify when you Approved or Declined this request.')
    status = models.CharField(max_length=100, choices=statuses, blank=True,  help_text='Please select Approved or Declined.')
    reason_of_decline_if_any = models.CharField(max_length=100, blank=True, help_text='If you want to decline ths request, please explain why.')
    Approved_or_Declined_By = models.CharField(max_length=100, choices=ppl, blank=True, help_text='The user that is approving or declining this transaction request.')
    





    '''
    add = models.IntegerField(default=0, max_length=30)
    balance1 = str(balance)
    add1 = str(add)
    balance2 = float(balance1)
    add2 = float(add1)
    total = float(add2) + float(balance2)
    total1 = float(total)
    print(total1)
  
    def new_func():
    current_bala.IntegerField()

new_func()
  '''

