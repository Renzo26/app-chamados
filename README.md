# 📋 Registro de Chamados

Sistema desktop para gerenciamento de chamados técnicos em unidades de saúde, com visual moderno, exportação de relatórios e controle simplificado por unidade.

---

## 🧾 Sobre o Projeto

O **Registro de Chamados** é um sistema desenvolvido para facilitar o acompanhamento e registro de atendimentos técnicos em unidades de saúde. Através de uma interface simples e funcional, é possível registrar, visualizar e zerar os chamados de forma eficiente. Os dados são armazenados localmente em JSON e exportados em planilhas Excel para análise e controle.

> 📌 Projeto desenvolvido por Arthur Renzo, com contribuição de Nicoly Ferreira de Paula na área de **Testes e Garantia da Qualidade (QA)**.

---

## 🚀 Tecnologias Utilizadas

### 💻 Frontend:
- Electron
- HTML5
- CSS3
- JavaScript

### 🛠 Backend:
- Python 3 (Flask)
- Pandas

### 📦 Outras ferramentas:
- JSON (armazenamento local)
- Electron Builder (empacotamento e distribuição)

---

## 🗂 Estrutura de Pastas

📦 Registro de Chamados
┣ 📜 api.py # API Flask (endpoints HTTP)
┣ 📜 backend.py # Processamento e geração de planilhas
┣ 📜 main.js # Lógica principal do Electron
┣ 📜 preload.js # Comunicação segura com Electron
┣ 📜 script.js # Integração entre frontend e API
┣ 📜 data.js # Gerenciamento dos dados locais
┣ 📜 index.html # Página principal da interface
┣ 📜 style.css # Estilo visual
┣ 📜 package.json # Configurações do projeto Electron
┣ 📜 electron-builder.yaml # Definições para empacotamento
┣ 📜 LICENSE.txt # Licença MIT
┗ 📜 README.md # Documentação do projeto
---
