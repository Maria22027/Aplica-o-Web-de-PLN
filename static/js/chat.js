const form = document.getElementById('chat-form');
const input = document.getElementById('user-input');
const chatBox = document.getElementById('chat-box');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const message = input.value.trim();
    if (!message) return;

    addMessage(message, 'user');
    input.value = '';
    addMessage('Digitando...', 'bot');

    try {
        const response = await fetch('/api/chat/', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ prompt: message })
        });
        const data = await response.json();
        removeTyping();
        addMessage(data.response, 'bot');
    } catch (error) {
        removeTyping();
        addMessage('⚠️ Erro ao se comunicar com o servidor.', 'bot');
    }
});

function addMessage(text, sender) {
    const msg = document.createElement('div');
    msg.classList.add('msg', sender);
    msg.innerText = text;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function removeTyping() {
    const typing = document.querySelector('.msg.bot:last-child');
    if (typing && typing.innerText === 'Digitando...') typing.remove();
}
