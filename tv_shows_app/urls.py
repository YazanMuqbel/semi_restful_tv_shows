from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shows/create', views.create_show, name='create'),
    path('shows/<int:id>', views.show_info, name='show_info'),
    path('show_all', views.show_all_shows, name= 'list_of_all_shows'),
    path('shows/<int:id>/delete', views.delete_show, name='delete'),
    #path('shows/<int:id>/update', views.update_show, name='update'),
    
]