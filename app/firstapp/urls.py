from django.urls import path

from . import views

urlpatterns = [
    path('',views.vista,name='vista'),
    path('dogs',views.dogs,name='dogs'),
    path('dogs/add',views.dogsAdd,name='dogsdd'),
    path('dogs/delete',views.dogsDelete,name='dogsdelete'),
    path('types',views.types,name='types'),
]
