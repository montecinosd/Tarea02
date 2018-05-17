from django.urls import path
from basket import views


urlpatterns = [
    path('', views.index, name="player"),
    path('list', views.index, name="player_list"),
    path('view/<int:player_id>', views.detail, name="player_detail"),
    path('agregar',views.TemplateAgregar,name='agregar'),
    path('listar',views.Templatelistar,name='Templatelistar')

]
