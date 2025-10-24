async function carregarHistorico() {
    const res = await fetch('/api/historico/');
    const data = await res.json();
    renderHistorico(data);
}

function renderHistorico(dados) {
    const tbody = document.getElementById('history-body');
    tbody.innerHTML = '';
    dados.forEach(item => {
        const row = `
            <tr>
                <td>${new Date(item.timestamp).toLocaleString()}</td>
                <td>${item.prompt}</td>
                <td>${item.response}</td>
                <td>${item.model}</td>
            </tr>
        `;
        tbody.innerHTML += row;
    });
}

document.getElementById('filter-btn').addEventListener('click', async () => {
    const filtro = document.getElementById('filter-input').value.trim();
    const res = await fetch(`/api/historico/?q=${encodeURIComponent(filtro)}`);
    const data = await res.json();
    renderHistorico(data);
});

document.getElementById('export-csv').addEventListener('click', () => {
    window.location.href = '/api/exportar/?formato=csv';
});

document.getElementById('export-json').addEventListener('click', () => {
    window.location.href = '/api/exportar/?formato=json';
});

carregarHistorico();
