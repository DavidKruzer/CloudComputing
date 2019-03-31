from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.detail, name='translation'),
    path('get_translation/', views.translation, name='get_translation'),
]
