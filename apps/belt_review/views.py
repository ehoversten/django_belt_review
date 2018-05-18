from django.shortcuts import render, HttpResponse, redirect
from .models import *
# Create your views here.
def index(request):

    return render(request, 'belt_review/index.html')


def register(request):
    # ---- TEST ---- First Test
    # print(request.POST)
    results = User.objects.regValidator(request.POST)
    print('Validation Result: ', result)
    if results[0]:
        # save id in session (which is in results[1])
        # (True, user_object)
        return redirect('/show')
    else:
        # transfer errors to flash messages (also in results[1])
        # (False, errors)

        for error in results[1]:
            messages.add_message(request, messages.ERROR, error)
    return redirect('/')


def login(request):
    pass

def logout(request):
    pass

def dashboard(request):
    pass

def buy(request):
    pass

def sell(request):
    pass

def remove(request):
    pass
