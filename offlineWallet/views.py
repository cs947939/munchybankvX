from datetime import time
#import re
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from accounts.models import balance, Transaction
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm
#from .models import transaction
#from .models import Purchase


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            instance = balance(user = request.user, balance = 0)
            instance.save()
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
@login_required
def profile(request):
    msg=""
    if request.method == "POST":
        try:
            username = request.POST["username"]
            amount = request.POST["amount"]
            memo = request.POST["memo"]
           # paper = request.POST["paper"]
           # pencil = request.POST["pencil"]
            time = request.POST["time"]
            senderUser = User.objects.get(username=request.user.username)
            sending_user=str(senderUser)
            receiverrUser =  User.objects.get(username=username)
            sender = balance.objects.get(user = senderUser)
            receiverr = balance.objects.get(user = receiverrUser)
            sender.balance = sender.balance - int(amount)
            receiverr.balance = receiverr.balance + int(amount)
            sender.memo = memo
            receiverr.memo = memo
          #  sender.paper = paper
          #  receiverr.pencil = pencil
            #sender.balance.memo = sender.memo()
            #receiverr.balance.memo = receiverr.memo()
            #sender.balance.memo.save()
            #receiverr.balance.memo.save()
            sender.time = time
            receiverr.time = time
            sender.save()
            receiverr.save()

            
            msg = "Transaction Success! " + amount + " MCI " + "has been transferred from " + sending_user + " to " + username + "."
        except Exception as e:
            print(e)
            msg = "Transaction Failure, Please check and try again."
    user = balance.objects.get(user=request.user)
    all_users= get_user_model().objects.all()
    displaynames= User.objects.all()
    balances= balance.objects.all()
    return render(request,'profile.html',{"balance":user.balance,"msg":msg, "all_users":all_users,"displayusername":displaynames,"balances":balances})#, "memo":user.memo})

def login1(request):
    return render(request,'registration/login.html')

def success(request):
    return render(request, 'success.html')

def requests(request):
    msg=""
    form = TransactionForm(request.POST)
    if request.method == 'POST':
      #  msg=""s
        form = TransactionForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form = TransactionForm(request.POST)
           # user = request.POST.get('user')
           # memo = request.POST.get('memo')
           # amount = request.POST.get('amount')
            form.save()
           # msg = "Your Transaction Request has been successfully submitted. Please wait until your account balance has been updated."
        return redirect(profile)
        
    return render(request,'request.html',{'form':form})#, 'user':user, 'memo':memo, 'amount':amount})
