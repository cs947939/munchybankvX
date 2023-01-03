from django.contrib import admin
from .models import balance, Transaction

class balanceAdmin(admin.ModelAdmin):
    list_display = ('user','balance','memo')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('Your_Username', 'Transaction_Type','memo','status')


admin.site.register(balance, balanceAdmin)
admin.site.register(Transaction,TransactionAdmin)

# Register your models here.
