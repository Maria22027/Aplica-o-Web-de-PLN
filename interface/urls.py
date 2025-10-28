from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
    path('historico/', views.historico, name='historico'),
    path('api/chat/', views.chat_api),          # <-- aqui estava 'api_chat'
    path('api/historico/', views.historico), # se existir
    path("export/json/", views.export_json, name="export_json"),
    path("export/csv/", views.export_csv, name="export_csv"),
]
