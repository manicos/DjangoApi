from django.urls import path

from . import views

urlpatterns = [
    path('',views.vista,name='vista'),
    path('dogs',views.dogs,name='dogs'),
    path('dog/add',views.dogsAdd,name='dogsAdd'),
    path('dog/delete',views.dogsDelete,name='dogsdelete'),
    path('dog/get',views.dogsGet,name='dogsGet'),
    path('dog/get/<int:dogid>',views.dogsGetId,name='dogsGetId'),
    path('types',views.types,name='types'),
]
