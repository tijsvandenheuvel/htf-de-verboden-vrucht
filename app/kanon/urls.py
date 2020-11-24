from django.urls import path

from . import views

app_name='kanon'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:kanon_id>/', views.detail, name='detail'),
    path('<int:kanon_id>/reservation', views.reservation, name='reservation'),
    path('<int:kanon_id>/order', views.order, name='order')
]