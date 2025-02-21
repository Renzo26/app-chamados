from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Definição do caminho do arquivo JSON para armazenar os chamados
DATA_FILE = "chamados.json"

def carregar_chamados():
    """Carrega os chamados do arquivo JSON."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

def salvar_chamados(chamados):
    """Salva os chamados no arquivo JSON."""
    with open(DATA_FILE, "w") as file:
        json.dump(chamados, file)

@app.route("/salvar_dados", methods=["POST"])
def salvar_dados():
    data = request.get_json()
    if not data or "contadores" not in data:
        return jsonify({"sucesso": False, "erro": "Dados inválidos"}), 400

    chamados = data["contadores"]
    salvar_chamados(chamados)
    return jsonify({"sucesso": True, "mensagem": "Dados salvos com sucesso!"})
    print("📩 Recebendo dados:", data)

@app.route("/contadores", methods=["GET"])
def get_contadores():
    """Retorna os contadores salvos."""
    chamados = carregar_chamados()
    return jsonify(chamados)

@app.route("/total_chamados", methods=["GET"])
def get_total_chamados():
    """Retorna o total de chamados."""
    chamados = carregar_chamados()
    total = sum(chamados.values())
    return jsonify({"total": total})

@app.route("/ping", methods=["GET"])
def ping():
    """Endpoint para verificar se a API está rodando."""
    return jsonify({"status": "API rodando"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002, debug=True)