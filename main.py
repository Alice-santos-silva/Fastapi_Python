from fastapi import FastAPI

app = FastAPI()

# criando as classes:
class Usuario:
    def __init__(self, id_usuario, nome_usuario, id_departamento):
        self.id_usuario = id_usuario
        self.nome_usuario = nome_usuario
        self.id_departamento = id_departamento

class Departamento:
    def __init__(self, id_departamento, nome_departamento):
        self.id_departamento = id_departamento
        self.nome_departamento = nome_departamento

class Chamado:
    def __init__(self, id_chamado, id_usuario, prioridade, id_departamento, mes):
        self.id_chamado = id_chamado
        self.id_usuario = id_usuario
        self.prioridade = prioridade
        self.id_departamento = id_departamento
        self.mes = mes

class Ativo:
    def __init__(self, id_maquina, id_usuario, id_departamento, num_serie):
        self.id_maquina = id_maquina
        self.id_usuario = id_usuario
        self.id_departamento = id_departamento
        self.num_serie = num_serie


#listas com os dados:
dados_usuarios = [
    {"id_usuario": 1, "nome_usuario": "Alice Santos", "id_departamento": 3},
    {"id_usuario": 2, "nome_usuario": "Gabriel Santos", "id_departamento": 1},
    {"id_usuario": 3, "nome_usuario": "Henrique Costa", "id_departamento": 2},
    {"id_usuario": 4, "nome_usuario": "Silvia Souza", "id_departamento": 5},
    {"id_usuario": 5, "nome_usuario": "Lais Ferreira", "id_departamento": 1},
    {"id_usuario": 6, "nome_usuario": "Luiza Teles", "id_departamento": 5},
    {"id_usuario": 7, "nome_usuario": "Luiz Vargas", "id_departamento": 3},
    {"id_usuario": 8, "nome_usuario": "Maria Silva", "id_departamento": 4},
    {"id_usuario": 9, "nome_usuario": "Jose Oliveira", "id_departamento": 4},
    {"id_usuario": 10, "nome_usuario": "Ana Barbosa", "id_departamento": 5}
]

dados_departamentos = [
    {"id_departamento": 1, "nome_departamento": "Juridico"},
    {"id_departamento": 2, "nome_departamento": "Financeiro"},
    {"id_departamento": 3, "nome_departamento": "T.I"},
    {"id_departamento": 4, "nome_departamento": "Marketing"},
    {"id_departamento": 5, "nome_departamento": "RH"}
]

dados_chamados = [
    {"id_chamado": 1, "id_usuario": 2, "prioridade": "Alta", "id_departamento": 1, 
"mes": "fevereiro"},
    {"id_chamado": 2, "id_usuario": 5, "prioridade": "Normal", "id_departamento": 1, 
 "mes": "fevereiro"},
    {"id_chamado": 3, "id_usuario": 2, "prioridade": "Normal", "id_departamento": 1, "mes": "março"},
    {"id_chamado": 4, "id_usuario": 1, "prioridade": "Baixa", "id_departamento": 3, "mes": "março"},
    {"id_chamado": 5, "id_usuario": 3, "prioridade": "Normal", "id_departamento": 2, "mes": "março"},
    {"id_chamado": 6, "id_usuario": 10, "prioridade": "Alta", "id_departamento": 5, "mes": "março"},
    {"id_chamado": 7, "id_usuario": 4, "prioridade": "Baixa", "id_departamento": 5, "mes": "abril"},
    {"id_chamado": 8, "id_usuario": 5, "prioridade": "Normal", "id_departamento": 1, "mes": "maio"},
    {"id_chamado": 9, "id_usuario": 7, "prioridade": "Alta", "id_departamento": 3, "mes": "maio"},
    {"id_chamado": 10, "id_usuario": 2, "prioridade": "Normal", "id_departamento": 1, "mes": "junho"}
]

dados_inventario = [
    {"id_maquina": 201, "id_usuario": 1, "id_departamento": 3, "num_serie": "ABC123456789"},
    {"id_maquina": 202, "id_usuario": 2, "id_departamento": 1, "num_serie": "XYZ987654321"},
    {"id_maquina": 203, "id_usuario": 3, "id_departamento": 2, "num_serie": "QWERTY123456"},
    {"id_maquina": 204, "id_usuario": 4, "id_departamento": 5, "num_serie": "7890ASDFG123"},
    {"id_maquina": 205, "id_usuario": 5, "id_departamento": 1, "num_serie": "MNBVCXZ98765"},
    {"id_maquina": 206, "id_usuario": 6, "id_departamento": 5, "num_serie": "12345POIUYT"},
    {"id_maquina": 207, "id_usuario": 7, "id_departamento": 3, "num_serie": "LKJHGFDS3210"},
    {"id_maquina": 208, "id_usuario": 8, "id_departamento": 4, "num_serie": "45678ZXCVBN"},
    {"id_maquina": 209, "id_usuario": 9, "id_departamento": 4, "num_serie": "987654QWERT"},
    {"id_maquina": 210, "id_usuario": 10, "id_departamento": 5, "num_serie": "UIOP1234567"}
]

# classe usuario:
usuario1 = Usuario(dados_usuarios[0]["id_usuario"], dados_usuarios[0]["nome_usuario"], dados_usuarios[0]["id_departamento"])
usuario2 = Usuario(dados_usuarios[1]["id_usuario"], dados_usuarios[1]["nome_usuario"], dados_usuarios[1]["id_departamento"])
usuario3 = Usuario(dados_usuarios[2]["id_usuario"], dados_usuarios[2]["nome_usuario"], dados_usuarios[2]["id_departamento"])
usuario4 = Usuario(dados_usuarios[3]["id_usuario"], dados_usuarios[3]["nome_usuario"], dados_usuarios[3]["id_departamento"])
usuario5 = Usuario(dados_usuarios[4]["id_usuario"], dados_usuarios[4]["nome_usuario"], dados_usuarios[4]["id_departamento"])
usuario6 = Usuario(dados_usuarios[5]["id_usuario"], dados_usuarios[5]["nome_usuario"], dados_usuarios[5]["id_departamento"])
usuario7 = Usuario(dados_usuarios[6]["id_usuario"], dados_usuarios[6]["nome_usuario"], dados_usuarios[6]["id_departamento"])
usuario8 = Usuario(dados_usuarios[7]["id_usuario"], dados_usuarios[7]["nome_usuario"], dados_usuarios[7]["id_departamento"])
usuario9 = Usuario(dados_usuarios[8]["id_usuario"], dados_usuarios[8]["nome_usuario"], dados_usuarios[8]["id_departamento"])
usuario10 = Usuario(dados_usuarios[9]["id_usuario"], dados_usuarios[9]["nome_usuario"], dados_usuarios[9]["id_departamento"])

# classe departamento
departamento1 = Departamento(dados_departamentos[0]["id_departamento"], dados_departamentos[0]["nome_departamento"])
departamento2 = Departamento(dados_departamentos[1]["id_departamento"], dados_departamentos[1]["nome_departamento"])
departamento3 = Departamento(dados_departamentos[2]["id_departamento"], dados_departamentos[2]["nome_departamento"])
departamento4 = Departamento(dados_departamentos[3]["id_departamento"], dados_departamentos[3]["nome_departamento"])
departamento5 = Departamento(dados_departamentos[4]["id_departamento"], dados_departamentos[4]["nome_departamento"])

# classe chamado
chamado1 = Chamado(dados_chamados[0]["id_chamado"], dados_chamados[0]["id_usuario"], dados_chamados[0]["prioridade"], dados_chamados[0]["id_departamento"], dados_chamados[0]["mes"])

chamado2 = Chamado(dados_chamados[1]["id_chamado"], dados_chamados[1]["id_usuario"], dados_chamados[1]["prioridade"], dados_chamados[1]["id_departamento"], dados_chamados[1]["mes"])

chamado3 = Chamado(dados_chamados[2]["id_chamado"], dados_chamados[2]["id_usuario"], dados_chamados[2]["prioridade"], dados_chamados[2]["id_departamento"], dados_chamados[2]["mes"])

chamado4 = Chamado(dados_chamados[3]["id_chamado"], dados_chamados[3]["id_usuario"], dados_chamados[3]["prioridade"], dados_chamados[3]["id_departamento"], dados_chamados[3]["mes"])

chamado5 = Chamado(dados_chamados[4]["id_chamado"], dados_chamados[4]["id_usuario"], dados_chamados[4]["prioridade"], dados_chamados[4]["id_departamento"], dados_chamados[4]["mes"])

chamado6 = Chamado(dados_chamados[5]["id_chamado"], dados_chamados[5]["id_usuario"], dados_chamados[5]["prioridade"], dados_chamados[5]["id_departamento"], dados_chamados[5]["mes"])

chamado7 = Chamado(dados_chamados[6]["id_chamado"], dados_chamados[6]["id_usuario"], dados_chamados[6]["prioridade"], dados_chamados[6]["id_departamento"], dados_chamados[6]["mes"])

chamado8 = Chamado(dados_chamados[7]["id_chamado"], dados_chamados[7]["id_usuario"], dados_chamados[7]["prioridade"], dados_chamados[7]["id_departamento"], dados_chamados[7]["mes"])

chamado9 = Chamado(dados_chamados[8]["id_chamado"], dados_chamados[8]["id_usuario"], dados_chamados[8]["prioridade"], dados_chamados[8]["id_departamento"], dados_chamados[8]["mes"])

chamado10 = Chamado(dados_chamados[9]["id_chamado"], dados_chamados[9]["id_usuario"], dados_chamados[9]["prioridade"], dados_chamados[9]["id_departamento"], dados_chamados[9]["mes"])

# classe inventario
ativo1 = Ativo(dados_inventario[0]["id_maquina"], dados_inventario[0]["id_usuario"], dados_inventario[0]["id_departamento"], dados_inventario[0]["num_serie"])
ativo2 = Ativo(dados_inventario[1]["id_maquina"], dados_inventario[1]["id_usuario"], dados_inventario[1]["id_departamento"], dados_inventario[1]["num_serie"])
ativo3 = Ativo(dados_inventario[2]["id_maquina"], dados_inventario[2]["id_usuario"], dados_inventario[2]["id_departamento"], dados_inventario[2]["num_serie"])
ativo4 = Ativo(dados_inventario[3]["id_maquina"], dados_inventario[3]["id_usuario"], dados_inventario[3]["id_departamento"], dados_inventario[3]["num_serie"])
ativo5 = Ativo(dados_inventario[4]["id_maquina"], dados_inventario[4]["id_usuario"], dados_inventario[4]["id_departamento"], dados_inventario[4]["num_serie"])
ativo6 = Ativo(dados_inventario[5]["id_maquina"], dados_inventario[5]["id_usuario"], dados_inventario[5]["id_departamento"], dados_inventario[5]["num_serie"])
ativo7 = Ativo(dados_inventario[6]["id_maquina"], dados_inventario[6]["id_usuario"], dados_inventario[6]["id_departamento"], dados_inventario[6]["num_serie"])
ativo8 = Ativo(dados_inventario[7]["id_maquina"], dados_inventario[7]["id_usuario"], dados_inventario[7]["id_departamento"], dados_inventario[7]["num_serie"])
ativo9 = Ativo(dados_inventario[8]["id_maquina"], dados_inventario[8]["id_usuario"], dados_inventario[8]["id_departamento"], dados_inventario[8]["num_serie"])
ativo10 = Ativo(dados_inventario[9]["id_maquina"], dados_inventario[9]["id_usuario"], dados_inventario[9]["id_departamento"], dados_inventario[9]["num_serie"])

# lista de usuarios:
usuarios = [usuario1, usuario2, usuario3, usuario4, usuario5, usuario6, usuario7, usuario8, usuario9, usuario10]

# lista de departamentos
departamentos = [departamento1, departamento2, departamento3, departamento4, departamento5]

# lista de chamados
chamados = [chamado1, chamado2, chamado3, chamado4, chamado5, chamado6, chamado7, chamado8, chamado9, chamado10]

# lista de ativos
ativos = [ativo1, ativo2, ativo3, ativo4, ativo5, ativo6, ativo7, ativo8, ativo9, ativo10]

@app.get("/")
async def root():
    return {"API EM FUNCIONAMENTO"}

@app.get("/usuarios/")
async def get_usuarios():
    return usuarios

@app.get("/departamentos/")
async def get_departamentos():
  return departamentos

@app.get("/chamados/")
async def get_chamados():
  return chamados

@app.get("/ativos/")
async def get_ativos():
  return ativos

