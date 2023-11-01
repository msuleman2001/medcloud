# manager/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('managers/', views.get_managers, name='managers-list'),
    path('search_manager/<int:manager_id>/',
         views.search_manager, name='manager-detail'),
    path('add_manager/', views.add_manager, name='add-manager'),
    path('update_manager/<int:manager_id>/',
         views.update_manager, name='update-manager'),
]
