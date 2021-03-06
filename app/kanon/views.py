from django.shortcuts import get_object_or_404, render, redirect

from django.http import HttpResponse

from .models import Kanon
from .models import User

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
    name = request.POST['name']
    user = User.objects.filter(user_name=name)
    if user:
        kanon.user_set.add(user[0])
    else:
        kanon.user_set.create(user_name=name)
    kanon.save()
    return render(request, 'kanon/detail.html', {'kanon': kanon})

def createUser(request):
    user_name = request.POST['name']
    user = User(user_name = user_name)
    user.save()
    return redirect('/api/kanon/')

def goToCreateUser(request):
    return render(request, 'user/user.html')


def createKanon(request):
    kanon_name = request.POST['name']
    kanon = Kanon(kanon_name = kanon_name)
    kanon.save()
    return redirect('/api/kanon/')

def goToCreateKanon(request):
    return render(request, 'kanon/kanon.html')

