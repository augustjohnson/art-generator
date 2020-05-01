from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('art/', views.index, name='art'),
    path('robot/', views.index, name='robot'),
]