import tkinter as tk
import tkinter.messagebox as messagebox
import pandas as pd
import os
from datetime import datetime, timedelta
from pathlib import Path

# --- Configurações ---
UNIDADES = [
    "Almoxarifado Central", "CAPS III AD Alves Dias", "CAPS III Álc Drog Alvarenga",
    "CAPS III Álc. e Drog Cent", "CAPS III Álc. e Drog Inf. Juv", "CAPS III Alvarenga",
    "CAPS III Alves Dias", "CAPS III Centro", "CAPS III Farina", "CAPS III Rudge Ramos",
    "CAPS III Selecta", "CAPS Inf. Juvenil", "Centro Cirúrgico e Castra Móvel",
    "Centro de referência - TEA", "CEO Alvarenga", "CEO Nova Petrópolis",
    "CEO Silvina", "CER", "Chamado errado / Sem localização", "Comunicação",
    "Consultório na Rua", "Departamento de Administração da Saúde",
    "Departamento de Apoio a Gestão do SUS", "Departamento de Atenção a Saúde e Vigilância",
    "Departamento de Atenção Básica e Gestão do Cuidado", "Departamento de Atenção Especializada",
    "Departamento de Atenção Hospitalar, Urgências  Emergências", "Divisão Ambulatorial",
    "Divisão Assistência Farmacêutica", "Divisão de Adm. De Bens, Serv. E Pessoal - SS",
    "Divisão de Adm. Do Fundo Municipal de Saúde", "Divisão de Compras",
    "Divisão de Contratos", "Divisão de Educação Permanente e Gestão Participativa",
    "Divisão de Patrimônio", "Divisão de Planejamento em Saúde", "Divisão de Saúde Bucal",
    "Divisão de Saúde do Trabalhador e do Meio Ambiente", "Divisão de Saúde Mental",
    "Divisão de Unidade Básica de Saúde", "Divisão de Veterinária e Controle de Zoonoses",
    "Divisão de Vigilância Epidemiológica", "Divisão de Vigilância Sanitária",
    "Divisão Infraestrutura (Corporativo)", "Divisão Regulação", "Divisão Técnico Assistencial",
    "Dunacor", "Escola de Saúde", "Farmácia de Medicamentos Especializados - FME",
    "FMABC", "FUNCRAF", "Gabinete da Secretaria de Saúde", "GSS | Gabinete Secretaria da Saúde",
    "HA - Hospital Anchieta", "HC - Hospital das Clinicas", "HMU - Hospital da Mulher",
    "Hospital da Reabilitação - ABC", "Hospital de Olhos", "Hospital Municipal de Olhos.",
    "HU - Hospital Urgência", "IML Demarchi - Corpo de Delito", "Juridico", "NEU - Núcleo Educação de Urgência",
    "Nutrarte", "Outras Secretarias", "PA Psiquiátrico", "PA Taboão", "Parque Estoril (SS)",
    "POLIALVARENGA", "POLICENTRO", "POLIMAGEM", "Recursos Humanos",
    "Residências Terapêuticas", "SAAJ - Serv. Atendimento Ação Judicial", "Sala de Choque",
    "SAME", "SAMU - Avançado", "SAMU - Basica", "SAMU - Serv. Administrativos",
    "Seção da Central de Regulação em Saúde", "Seção de Auditoria em Saúde",
    "Seção de Controle e Avaliação", "Seção de Educação em Saúde", "Seção de Gestão Participativa",
    "Seção de Informação para gestão", "Seção de Lab. Municipal de Saúde Pública",
    "Seção de Orçamento e Planej. Em Saúde", "Seção de Padronização e Programação",
    "Seção de Programação", "Seção de Unidade, Org. e Acesso em Assistência Farmacêutica",
    "Seção de Verificação de Óbitos", "Secretária da Administração", "Secretária de Finanças",
    "Serviço de Expediente", "Serviço e Transporte Sanitário e Administrativo",
    "SETIH - Transporte InterHospitalar - Avançado", "SETIH - Transporte InterHospitalar - Basico",
    "SIGMA", "UA - Unidade de Acolhimento Transitório", "UBS Alvarenga", "UBS Alves Dias",
    "UBS Areião", "UBS Baeta", "UBS Batistini", "UBS Calux", "UBS Caminho do Mar",
    "UBS Demarchi", "UBS Farina", "UBS Ferrazópolis", "UBS Finco", "UBS Ipê",
     "UBS Jordanópolis", "UBS Leblon", "UBS Montanhão", "UBS Nazareth",
    "UBS Orquídeas", "UBS Parque São Bernardo", "UBS Paulicéia", "UBS Planalto", "UBS Represa",
    "UBS Riacho", "UBS Rudge Ramos", "UBS Santa Cruz", "UBS Santa Terezinha", "UBS São Pedro",
    "UBS São Pedro II", "UBS Selecta", "UBS Silvina", "UBS Taboão", "UBS União",
    "UBS Vila Dayse", "UBS Vila Esperança", "UBS Vila Euclides", "UBS Vila Marchi",
    "UBS Vila Rosa", "UGP", "Unidade de Coordenação de Programas", "Unidade Gestora do Projeto",
    "Unidades Externas", "UPA Alvarenga", "UPA Alves Dias", "UPA Baeta", "UPA Demarchi",
    "UPA Jardim Silvina / Selecta", "UPA Paulicéia", "UPA Riacho", "UPA Rudge",
    "UPA S. Pedro", "UPA Silvina"
]
PASTA_PLANILHAS = Path.home() / "Documents" / "Planilhas Chamados"
NOME_ARQUIVO = "chamados_{}.xlsx"
ARQUIVO_CONTROLE = PASTA_PLANILHAS / "controle.txt"

# --- Variáveis Globais ---
contadores = {unidade: 0 for unidade in UNIDADES}
total_chamados = 0
caminho_planilha = None
data_inicio_planilha = None
filtro_entry = None
canvas = None
frame = None
total_label = None  # Label para exibir o total de chamados

# --- Funções de Arquivo ---
def criar_pasta_planilhas():
    """Cria a pasta para armazenar as planilhas, se ela não existir."""
    PASTA_PLANILHAS.mkdir(parents=True, exist_ok=True)

def carregar_arquivo_controle():
    """Carrega a data de início da planilha e o total de chamados do arquivo de controle."""
    global data_inicio_planilha, total_chamados
    if ARQUIVO_CONTROLE.exists():
        try:
            with open(ARQUIVO_CONTROLE, "r") as f:
                linhas = f.readlines()
                data_inicio_planilha = datetime.strptime(linhas[0].strip(), "%Y%m%d").date()
                total_chamados = int(linhas[1].strip())
        except (FileNotFoundError, ValueError, IndexError):
            # Se o arquivo não existir ou estiver corrompido, define a data de início como hoje
            data_inicio_planilha = datetime.today().date()
            total_chamados = 0
            salvar_arquivo_controle()  # Cria um novo arquivo de controle
    else:
        data_inicio_planilha = datetime.today().date()
        total_chamados = 0
        salvar_arquivo_controle()  # Cria um novo arquivo de controle

def salvar_arquivo_controle():
    """Salva a data de início da planilha e o total de chamados no arquivo de controle."""
    try:
        with open(ARQUIVO_CONTROLE, "w") as f:
            f.write(data_inicio_planilha.strftime("%Y%m%d") + "\n")
            f.write(str(total_chamados) + "\n")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar o arquivo de controle: {e}")

def definir_caminho_planilha():
    """Define o caminho da planilha com base na data de início."""
    global caminho_planilha, data_inicio_planilha
    hoje = datetime.today().date()
    if data_inicio_planilha is None:
        carregar_arquivo_controle()  # Carrega a data de início se ainda não foi carregada

    if (hoje - data_inicio_planilha).days >= 31:
        # Cria nova planilha se passaram 31 dias
        data_inicio_planilha = hoje
        salvar_arquivo_controle()
    caminho_planilha = PASTA_PLANILHAS / NOME_ARQUIVO.format(data_inicio_planilha.strftime("%Y%m%d"))
    return caminho_planilha

def carregar_planilha():
    """Carrega os dados da planilha, se existir."""
    global contadores, caminho_planilha
    caminho_planilha = definir_caminho_planilha()  # Garante que o caminho está definido
    if caminho_planilha.exists():
        try:
            df = pd.read_excel(caminho_planilha)
            # Verifica se as colunas 'Unidade' e 'Chamados' existem no DataFrame
            if 'Unidade' in df.columns and 'Chamados' in df.columns:
                contadores = dict(zip(df["Unidade"], df["Chamados"]))
            else:
                messagebox.showinfo("Aviso", "Colunas 'Unidade' ou 'Chamados' não encontradas na planilha. Criando nova planilha.")
        except FileNotFoundError:
            messagebox.showinfo("Aviso", "Planilha não encontrada. Criando nova planilha.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar a planilha: {e}")

def salvar_planilha():
    """Salva os dados na planilha."""
    df = pd.DataFrame(list(contadores.items()), columns=["Unidade", "Chamados"])
    try:
        df.to_excel(caminho_planilha, index=False)
    except PermissionError:
        messagebox.showerror("Erro", "Feche a planilha antes de salvar.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar a planilha: {e}")

# --- Funções de Lógica ---
def registrar_chamado(unidade):
    """Registra um chamado para a unidade e atualiza a planilha."""
    global total_chamados
    contadores[unidade] += 1
    total_chamados += 1
    salvar_planilha()
    salvar_arquivo_controle()
    atualizar_interface()
    messagebox.showinfo("Registrado", f"Chamado registrado para {unidade}")

def zerar_planilha():
    """Zera todos os chamados."""
    global contadores, total_chamados
    contadores = {unidade: 0 for unidade in UNIDADES}
    total_chamados = 0
    salvar_planilha()
    salvar_arquivo_controle()
    atualizar_interface()
    messagebox.showinfo("Zerado", "Todos os chamados foram zerados!")

# --- Funções de Interface ---
def atualizar_interface():
    """Atualiza os números exibidos na interface gráfica."""
    filtro = filtro_entry.get().lower()
    unidades_filtradas = [u for u in UNIDADES if filtro in u.lower()]
    for i, unidade in enumerate(unidades_filtradas):
        # Verifica se o widget já existe
        if i < len(frame.winfo_children()) // 2:  # Cada unidade tem um botão e um label
            btn = frame.winfo_children()[i*2]
            lbl = frame.winfo_children()[i*2 + 1]
            btn.config(text=unidade, command=lambda u=unidade: registrar_chamado(u))
            lbl.config(text=str(contadores.get(unidade, 0)))
        else:  # Cria novos widgets se necessário
            btn = tk.Button(frame, text=unidade, command=lambda u=unidade: registrar_chamado(u))
            btn.grid(row=i, column=0, padx=5, pady=5, sticky="ew")
            lbl = tk.Label(frame, text=str(contadores.get(unidade, 0)))
            lbl.grid(row=i, column=1, padx=5, pady=5, sticky="ew")

    # Remove widgets excedentes
    while len(frame.winfo_children()) > len(unidades_filtradas) * 2:
        frame.winfo_children()[-1].destroy()
        frame.winfo_children()[-1].destroy()

    # Atualiza o label do total de chamados
    total_label.config(text=f"Total de Chamados: {total_chamados}")

    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def on_mousewheel(event):
    """Função para lidar com o evento de rolar o mouse."""
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

# --- Inicialização da Interface ---
def criar_interface():
    """Cria a interface gráfica."""
    root = tk.Tk()
    root.title("Registro de Chamados")

    # Menu
    menu_bar = tk.Menu(root)
    opcoes_menu = tk.Menu(menu_bar, tearoff=0)
    opcoes_menu.add_command(label="Zerar Chamados", command=zerar_planilha)
    menu_bar.add_cascade(label="Opções", menu=opcoes_menu)
    root.config(menu=menu_bar)

    # Filtro
    global filtro_entry, canvas, frame, total_label  # Inclui total_label na lista de globais
    filtro_entry = tk.Entry(root)
    filtro_entry.pack(pady=5, fill="x")
    filtro_entry.bind("<KeyRelease>", lambda event: atualizar_interface())

    # Canvas e Scrollbar
    canvas = tk.Canvas(root)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor='nw')
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    # Layout do Frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)

    # Label para exibir o total de chamados
    total_label = tk.Label(root, text="Total de Chamados: 0", font=("Arial", 12))
    total_label.pack(pady=10)

    # Assinatura
    assinatura = tk.Label(root, text="Create By Arthur Renzo e Arthur Melo", fg="gray", font=("Arial", 8))
    assinatura.pack(side="bottom", pady=5)

    # Bind do evento de rolagem do mouse ao canvas
    canvas.bind("<MouseWheel>", on_mousewheel)  # Para Windows
    canvas.bind("<Button-4>", on_mousewheel)  # Para Linux
    canvas.bind("<Button-5>", on_mousewheel)  # Para Linux

    return root

# --- Main ---
if __name__ == "__main__":
    criar_pasta_planilhas()
    carregar_arquivo_controle()  # Carrega a data de início da planilha
    carregar_planilha()

    root = criar_interface()
    atualizar_interface()  # Carrega a interface inicial
    root.mainloop()
