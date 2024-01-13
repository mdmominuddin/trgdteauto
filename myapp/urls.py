from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('section/', views.sections, name='section'),
    path('armytrg/', views.armytrg, name='armytrg'),
    path('navytrg/', views.navytrg, name='navytrg'),
    path('airtrg/', views.airtrg, name='airtrg'),
    path('jttrg/', views.jttrg, name='jttrg'),
    path('hqtrg/', views.hqtrg, name='hqtrg'),
    path('summary/', views.Summary, name='summary'),
    path('addparticipants/', views.AddParticipants, name='addparticipants'),
    path('add_go/', views.GovtOrderandParticipations, name='add_go'),
]
