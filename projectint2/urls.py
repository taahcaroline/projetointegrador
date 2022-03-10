from django.urls import path
from projectint2 import views
 
urlpatterns = [
    path('', views.home, name='meuapp-home'),
    path('sobre/', views.sobre, name='sobre'),
    path('meuscronogramas/', views.meuscronogramas, name='meuscronogramas'),
    path('meuscronogramas/<int:id>/', views.cronogramaview, name="cronograma-view"),
    path('novocronograma/', views.novocronograma, name='novocronograma'),
    path('concluircronograma/<int:id>/', views.donecron, name="concluircronograma"),
    path('editarcronograma/<int:id>/', views.editcron, name="editarcronograma"),
    path('deletarcronograma/<int:id>/', views.deletecron, name="deletarcronograma"),
    

 ]