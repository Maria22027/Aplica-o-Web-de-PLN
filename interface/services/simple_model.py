import random

# Classe simples que simula um "modelo de linguagem"
# (sem usar IA, só responde de forma aleatória)
class SimpleChatModel:
    def __init__(self):
        # Respostas possíveis do modelo
        self.responses = [
            "Interessante! Me conta mais sobre isso.",
            "Entendi... e como tu te sente com isso?",
            "Parece algo importante pra ti.",
            "Hmm... nunca tinha pensado por esse lado!",
            "Pode explicar melhor?",
            "Legal! O que mais tu gostaria de saber?"
        ]

    def generate(self, prompt):
        # Se o usuário não digitar nada
        if not prompt.strip():
            return "Desculpa, não entendi. Pode repetir?"
        # Escolhe uma resposta aleatória da lista
        return random.choice(self.responses)
