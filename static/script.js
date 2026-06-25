async function buscarClima() {

    const cidade = document
        .getElementById('cidade')
        .value
        .trim()

    const resultado = document.getElementById('resultado')

    if (!cidade) {
        resultado.innerHTML = '<p>Digite uma cidade.</p>'
        return
    }

    const resposta = await fetch(`/weather/${cidade}`)
    const dados = await resposta.json()

    if (dados.erro) {
        resultado.innerHTML = `<p>${dados.erro}</p>`
        return
    }

    resultado.innerHTML = `
        <h2>${dados.cidade}</h2>
        <p>Temperatura: ${dados.temperatura}°C</p>
        <p>Sensação térmica: ${dados.sensacao_termica}°C</p>
        <p>Umidade: ${dados.umidade}%</p>
        <p>Condição: ${dados.condicao}</p>
    `
}