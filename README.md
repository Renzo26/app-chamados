📝 Introdução

O Registro de Chamados é um software de gerenciamento de chamados para unidades de saúde. Ele permite registrar, visualizar e zerar contadores de chamados, salvando os dados em planilhas Excel. O projeto é desenvolvido utilizando Electron (frontend) e Flask (backend), garantindo uma interface moderna e uma API robusta.

🚀 Tecnologias Utilizadas

Frontend: Electron, HTML, CSS, JavaScript.

Backend: Flask, Python, Pandas.

Banco de Dados: JSON (possível melhoria futura para SQLite ou PostgreSQL).

Empacotamento: Electron Builder. 

📂 Estrutura do Projeto

📦 Registro de Chamados
┣ 📜 api.py            # Backend Flask (API)
┣ 📜 backend.py        # Backend Flask (Processamento e Planilhas)
┣ 📜 main.js           # Configuração do Electron
┣ 📜 preload.js        # Integração com Electron
┣ 📜 script.js         # Lógica de interface e chamadas à API
┣ 📜 style.css         # Estilização da interface
┣ 📜 index.html        # Interface principal
┣ 📜 data.js           # Manipulação de arquivos JSON
┣ 📜 package.json      # Configuração do projeto Electron
┣ 📜 electron-builder.yaml  # Configuração do empacotamento
┣ 📜 LICENSE.txt       # Licença do software
┗ 📜 README.md         # Documentação do projeto

💻 Frontend - Electron

O frontend do projeto é desenvolvido com Electron e interage com o backend através de requisições HTTP.

📌 Principais Arquivos:

main.js: Configuração do Electron e execução do backend.

script.js: Manipulação dos contadores e integração com a API.

index.html: Interface gráfica do usuário.

style.css: Estilização do frontend.

⚙️ Fluxo de Funcionamento

O Electron inicia o backend Flask automaticamente.

A interface carrega os contadores das unidades de saúde.

O usuário pode incrementar contadores, zerar chamados e salvar os dados.

Os dados são enviados ao backend, que os armazena no JSON e gera uma planilha Excel.

🏆 Autores

📌 Desenvolvido por Arthur Renzo 🎯
📌 Testes e QA por Nicoly Ferreira de Paula 🎯

📝 Licença: MIT
