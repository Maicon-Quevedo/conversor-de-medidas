import urllib.request
import json, sys, os
from datetime import datetime
from colorama import Fore

def converter_temperatura(valor, temperatura_origem, temperatura_destino):
    temperatura_origem = temperatura_origem.lower()
    temperatura_destino = temperatura_destino.lower()
    if temperatura_origem == "c":
        celsius=valor
    elif temperatura_origem == "f":
        celsius=(valor-32)*5/9
    elif temperatura_origem == "k":
        celsius=valor-273.15
    if temperatura_destino == "c":
        return celsius
    elif temperatura_destino == "f":
        return celsius*9/5+32
    elif temperatura_destino == "k":
        return celsius+273.15
    
peso_para_kg = {
    "kg": 1,
    "g": 0.001,
    "lb": 0.453592,
    "oz": 0.0283495,
    "t": 1000,
}

def converter_peso(valor, peso_origem, peso_destino):
    peso_origem=peso_origem.lower()
    peso_destino=peso_destino.lower()
    
    em_kg = valor*peso_para_kg[peso_origem]
    return em_kg/peso_para_kg[peso_destino]

distancia_para_m = {
    "m": 1,
    "km": 1000,
    "cm": 0.01,
    "mm": 0.001,
    "mi": 1609.33999997549,
    "ft": 0.3048,
    "in": 0.0254,
    "yd": 0.9144,
}

def converter_distancia(valor, distancia_origem, distancia_destino):
    distancia_origem=distancia_origem.lower()
    distancia_destino=distancia_destino.lower()

    distancia_metro = valor*distancia_para_m[distancia_origem]
    return distancia_metro/distancia_para_m[distancia_destino]

def converter_moeda(valor, moeda_origem, moeda_destino):
    moeda_origem = moeda_origem.upper()
    moeda_destino = moeda_destino.upper()

    url = f"https://open.er-api.com/v6/latest/{moeda_origem}"
    with urllib.request.urlopen(url, timeout=5) as resposta:
        dados = json.loads(resposta.read())

    if dados.get("result") != "success":
        print(Fore.RED + f"Erro: '{moeda_origem}' não é uma moeda válida.")
        sys.exit(1)

    if moeda_destino not in dados["rates"]:
        print(Fore.RED + f"Erro: '{moeda_destino}' não é uma moeda válida.")
        sys.exit(1)

    taxa = dados["rates"][moeda_destino]
    return valor * taxa

def salvar_historico(valor, da_unidade, para_unidade, resultado):
    registro = {
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "valor": valor,
        "de": da_unidade.upper(),
        "para": para_unidade.upper(),
        "resultado": round(resultado, 2),
    }
    if os.path.exists("historico.json"):
        with open("historico.json", "r") as arquivo:
            historico = json.load(arquivo)
    else:
        historico = []

    historico.append(registro)

    with open("historico.json", "w") as arquivo:
        json.dump(historico, arquivo, indent=4)