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
    kanon = get_object_or_404(Kanon, pk=kanon_id)
    return render(request, 'kanon/manTheKanon.html',{'kanon': kanon})

# add munition to kanon
def order(request, kanon_id):
    kanon = get_object_or_404(Kanon, pk=kanon_id)
    return render(request, 'kanon/orderMunition.html',{'kanon': kanon})

def placeOrder(request,kanon_id):
    kanon = get_object_or_404(Kanon, pk=kanon_id)
    kanon.munition=kanon.munition+int(request.POST['amount'])
    kanon.save()
    return render(request, 'kanon/detail.html', {'kanon': kanon})

def assignSoldier(request,kanon_id):
    kanon = get_object_or_404(Kanon, pk=kanon_id)
    kanon.user_set.add()
    return render(request, 'kanon/detail.html', {'kanon': kanon})


def createUser(request):
    return render(request, 'kanon/index.html')