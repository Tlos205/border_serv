from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contract-vacancies/', views.contract_vacancies, name='contract_vacancies'),
    path('leadership/', views.leadership, name='leadership'),
    path('structure/', views.structure, name='structure'),
    path('activity/', views.activity, name='activity'),
    path('gosuslugi/', views.gosuslugi, name='gosuslugi'),
    path('service/', views.service, name='service'),
    path('residents/', views.residents, name='residents'),
    path('presscenter/', views.presscenter, name='presscenter'),
    path('contacts/', views.contacts, name='contacts'),
    path('feedback/', views.feedback, name='feedback'),
]