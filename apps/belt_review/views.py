from django.shortcuts import render, HttpResponse, redirect
from .models import *
# Create your views here.
def index(request):

    return render(request, 'belt_review/index.html')


def register(request):
    # ---- TEST ---- First Test
    # print(request.POST)
    results = User.objects.regValidator(request.POST)
    print('Validation Result: ', results)

    return redirect('/')


# def login(request):
#     pass
#
# def logout(request):
#     pass
#
# def dashboard(request):
#     pass
#
# def buy(request):
#     pass
#
# def sell(request):
#     pass
#
# def remove(request):
#     pass
