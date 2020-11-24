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

