from django.shortcuts import render
from django.http import JsonResponse

# Página principal do chat
def chat(request):
    return render(request, 'chat.html')

# Página do histórico
def historico(request):
    return render(request, 'historico.html')

# Mock das rotas que o JS vai chamar
def api_chat(request):
    return JsonResponse({"response": "Exemplo de resposta simulada do modelo."})

def api_historico(request):
    return JsonResponse([
        {"timestamp": "2025-10-21T10:00:00", "prompt": "Olá", "response": "Oi! Tudo bem?", "model": "mock-model"},
        {"timestamp": "2025-10-21T10:05:00", "prompt": "Qual é o seu nome?", "response": "Sou um chatbot!", "model": "mock-model"}
    ], safe=False)
