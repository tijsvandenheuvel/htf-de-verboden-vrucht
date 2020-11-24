from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

from .models import Kanon


def index(request):
    kanon_list = Kanon.objects.order_by('kanon_name')[:5]
    context = {'kanon_list': kanon_list}
    return render(request, 'kanon/index.html', context)

def detail(request, kanon_id):
    kanon = get_object_or_404(Kanon, pk=kanon_id)
    return render(request, 'kanon/detail.html', {'kanon': kanon})

# add users to kanon
def reservation(request, kanon_id):
    return render(request, 'kanon/manTheKanon.html')

# add munition to kanon
def order(request, kanon_id):
    return render(request, 'kanon/orderMunition.html')

def placeOrder(request,kanon_id,amount):
    kanon = get_object_or_404(Kanon, pk=kanon_id)
    kanon.munition=kanon.munition.amount+amount
    return render(request, 'kanon/detail.html', {'kanon': kanon})

def assignSoldier(request,kanon_id,name):
    kanon = get_object_or_404(Kanon, pk=kanon_id)
    
    return render(request, 'kanon/detail.html', {'kanon': kanon})


def createUser(request):
    return render(request, 'kanon/index.html')