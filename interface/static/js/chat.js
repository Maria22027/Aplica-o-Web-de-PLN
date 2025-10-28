// Espera o envio do formulário e intercepta o comportamento padrão
document.getElementById("chat-form").addEventListener("submit", async (e) => {
  e.preventDefault(); // previne o reload da página

  const input = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");
  const message = input.value.trim();

  if (!message) return; // não envia mensagem vazia

  // Exibe a mensagem do usuário
  chatBox.innerHTML += `<div class="msg user"><b>Você:</b> ${message}</div>`;
  input.value = "";

  try {
    // Faz a requisição ao backend Django na rota correta
    const res = await fetch("/api/chat/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt: message }),
    });

    if (!res.ok) {
      throw new Error(`Erro na requisição: ${res.status}`);
    }

    const data = await res.json();

    // Exibe a resposta do bot
    chatBox.innerHTML += `<div class="msg bot"><b>Bot:</b> ${data.response}</div>`;
  } catch (err) {
    // Caso dê algum erro, mostra mensagem de erro no chat
    chatBox.innerHTML += `<div class="msg bot"><b>Bot:</b> Erro: não foi possível obter resposta</div>`;
    console.error(err);
  }

  // Rola automaticamente para o final
  chatBox.scrollTop = chatBox.scrollHeight;
});
