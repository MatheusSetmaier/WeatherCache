async function buscarClima() {

    const cidade = document.getElementById('cidade').value

    const resposta = await fetch(`/weather/${cidade}`)

    const dados = await resposta.json()

    document.getElementById('resultado').innerHTML = `
        <h2>${dados.cidade}</h2>
        <p>Temperatura: ${dados.temperatura}°</p>
        <p>Sensação térmica: ${dados.sensacao_termica}°</p>
        <p>Umidade: ${dados.umidade}%</p>
        <p>Condição: ${dados.condicao}</p>
    `
}