from django.urls import path

from . import views

app_name='kanon'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:kanon_id>/', views.detail, name='detail')
]