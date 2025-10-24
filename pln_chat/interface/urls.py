from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
    path('historico/', views.historico, name='historico'),
    path('api/chat/', views.api_chat),
    path('api/historico/', views.api_historico),
]
