
import json


def salvar_fichas(dicionario_fichas):
    dados_para_salvar={}
    for chave,dados in dicionario_fichas.items():
        dados_para_salvar[chave]=vars(dados)
    
    with open("dados_para_salvar.json", "w") as arquivo:
        json.dump(dados_para_salvar, arquivo, indent=4)
   
   
def carregar_fichas():
    with open("dados_para_salvar.json", "r") as arquivo:
         return json.load(arquivo)