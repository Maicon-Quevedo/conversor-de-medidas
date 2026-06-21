import sys

from conversor.funcoes_conversoes import converter_temperatura, converter_peso, converter_distancia, converter_moeda, salvar_historico, pedir_valor, pedir_unidade
from colorama import Fore, Style, init
init(autoreset=True)

def modo_interativo():
    print("Bem vindo ao conversor de medidas!")
    print("O que você quer converter?")
    print("1. Temperatura")
    print("2. Peso")
    print("3. Distância")
    print("4. Moeda")
    escolha = input("Escolha: ")
    while escolha not in {"1", "2", "3", "4"}:
        print(Fore.RED + "Opção inválida! Digite 1, 2, 3 ou 4.")
        escolha = input("Escolha: ")

    if escolha == "1":
        da_unidade = pedir_unidade("De qual unidade? (c, f, k): ")
        para_unidade = pedir_unidade("Para qual unidade? (c, f, k): ")
        valor = pedir_valor()
        resultado = converter_temperatura(valor, da_unidade, para_unidade)
    elif escolha == "2":
        da_unidade = pedir_unidade("De qual unidade? (kg, g, lb, oz, t): ")
        para_unidade = pedir_unidade("Para qual unidade? (kg, g, lb, oz, t): ")
        valor = pedir_valor()
        resultado = converter_peso(valor, da_unidade, para_unidade)
    elif escolha == "3":
        da_unidade = pedir_unidade("De qual unidade? (m, km, cm, mm, mi, ft, in, yd): ")
        para_unidade = pedir_unidade("Para qual unidade? (m, km, cm, mm, mi, ft, in, yd): ")
        valor = pedir_valor()
        resultado = converter_distancia(valor, da_unidade, para_unidade)
    elif escolha == "4":
        da_unidade = pedir_unidade("De qual moeda? (usd, brl, eur...): ")
        para_unidade = pedir_unidade("Para qual moeda? (usd, brl, eur...): ")
        valor = pedir_valor()
        resultado = converter_moeda(valor, da_unidade, para_unidade)

    salvar_historico(valor, da_unidade, para_unidade, resultado)
    print(Fore.GREEN + f"{valor} {da_unidade.upper()} = {resultado:.2f} {para_unidade.upper()}")
    

if len(sys.argv) == 1:
    modo_interativo()
    sys.exit(0)
elif len(sys.argv) != 4:
    print(Fore.RED + "Precisa informar 3 valores!")
    print("Exemplo: python convert.py 100 usd brl")
    sys.exit(1)

try:
    valor = float(sys.argv[1])
except ValueError:
    print(Fore.RED + "Erro: o valor precisa ser algum número, ex: 100, 50.5")
    sys.exit(1)
da_unidade = sys.argv[2]
para_unidade = sys.argv[3]

temperaturas = {"c", "f", "k"}
pesos = {"kg", "g", "lb", "oz", "t"}
distancias = {"m", "km", "cm", "mm", "mi", "ft", "in", "yd"}

if da_unidade.lower() in temperaturas:
    resultado = converter_temperatura(valor, da_unidade, para_unidade)
elif da_unidade.lower() in pesos:
    resultado = converter_peso(valor, da_unidade, para_unidade)
elif da_unidade.lower() in distancias:
    resultado = converter_distancia(valor, da_unidade, para_unidade)
else:
    resultado = converter_moeda(valor, da_unidade, para_unidade)

salvar_historico(valor, da_unidade, para_unidade, resultado)
print(Fore.GREEN + f"{valor} {da_unidade.upper()} = {resultado:.2f} {para_unidade.upper()}")