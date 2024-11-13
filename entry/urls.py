from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('add-patient/', views.add_patient, name='add_patient'),
    path('entry_list', views.entry_list, name='entry_list'),        
    path('activate_patient/<int:id>/', views.activate_patient, name='activate_patient'),
]
