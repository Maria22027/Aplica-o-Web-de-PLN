from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json, datetime
from .services.simple_model import SimpleChatModel
from django.views.decorators.csrf import csrf_exempt
import csv
from io import StringIO

# Modelo simples
model = SimpleChatModel()

# Lista global para armazenar histórico temporário
chat_history = []

# Página principal do chat
def chat(request):
    return render(request, 'chat.html')

# API chamada pelo JavaScript para enviar a mensagem e receber a resposta
@csrf_exempt
def chat_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        prompt = data.get("prompt", "")

        # Gera resposta
        response = model.generate(prompt)

        # Monta registro
        record = {
            "session": str(request.session.session_key or "anon"),
            "prompt": prompt,
            "response": response,
            "timestamp": datetime.datetime.now().isoformat()
        }

        # Armazena na lista (substitui o MongoDB)
        chat_history.append(record)

        # Retorna resposta
        return JsonResponse({"response": response})

    return JsonResponse({"error": "Método inválido"}, status=400)

# Página do histórico
def historico(request):
    # Mostra histórico da lista em memória
    chats = sorted(chat_history, key=lambda x: x["timestamp"], reverse=True)
    return render(request, 'historico.html', {"chats": chats})

# Exporta histórico em JSON
def export_json(request):
    data = json.dumps(chat_history, ensure_ascii=False, indent=2)
    response = HttpResponse(data, content_type="application/json")
    response["Content-Disposition"] = 'attachment; filename="historico.json"'
    return response

# Exporta histórico em CSV
def export_csv(request):
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["prompt", "response", "timestamp"])
    for chat in chat_history:
        writer.writerow([chat.get("prompt"), chat.get("response"), chat.get("timestamp")])
    response = HttpResponse(output.getvalue(), content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="historico.csv"'
    return response
