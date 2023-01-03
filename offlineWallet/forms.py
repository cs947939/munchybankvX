from django import forms
from django.forms import ModelForm
from django import forms
from accounts.models import Transaction

TRANSACTIONS_TYPES = (
  #  ('Interest-Free Loan Issued', 'Interest-Free Loan Issued'),
 #   ('MT Realtor Payment - Transaction should start with "-".','MT Realtor Payment - Transaction should start with "-".'),
  #  ('Loan Paid Off','Loan Paid Off'),
    ('Interest-Free Loan for MTRealtor','Interest-Free Loan for MTRealtor'),
    ('Pay off your Interest-Free Loan','Pay off your Interest-Free Loan'),
    ('Withdrawal - Purchase Listing on MTRealtor','Withdrawal - Purchase Listing on MTRealtor'),

    )

class TransactionForm(ModelForm):
    Your_Username = forms.TextInput()
   # Transaction_Type = forms.ChoiceField(choices = TRANSACTIONS_TYPES)
    amount = forms.TextInput()
    memo = forms.TextInput()
   # time = forms.TimeField()
    class Meta:
        model = Transaction
        fields = ['Your_Username','Transaction_Type', 'amount', 'memo']