from django.urls import path

from . import views

app_name='api'

urlpatterns = [
    path('kanon/', views.index, name='index'),
    path('kanon/<int:kanon_id>/', views.detail, name='detail'),
    path('kanon/<int:kanon_id>/reservation', views.reservation, name='reservation'),
    path('kanon/<int:kanon_id>/order', views.order, name='order'),
    path('kanon/<int:kanon_id>/assignSoldier', views.assignSoldier, name='assignSoldier'),
    path('kanon/<int:kanon_id>/placeOrder', views.placeOrder, name='placeOrder'),
    path('user/createUser', views.createUser, name='createUser'),
    path('user/goToCreateUser', views.goToCreateUser, name= 'goToCreateUser'),
    path('kanon/createKanon', views.createKanon, name='createKanon'),
    path('kanon/goToCreateKanon', views.goToCreateKanon, name='goToCreateKanon')
]