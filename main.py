import sys

from conversor.funcoes_conversoes import converter_temperatura, converter_peso, converter_distancia, converter_moeda

def modo_interativo():
    print("Bem vindo ao conversor de medidas!")
    print("O que você quer converter?")
    print("1. Temperatura")
    print("2. Peso")
    print("3. Distância")
    print("4. Moeda")
    escolha = input("Escolha: ")
    while escolha not in {"1", "2", "3", "4"}:
        print("Opção inválida! Digite 1, 2, 3 ou 4.")
        escolha = input("Escolha: ")

    if escolha == "1":
        da_unidade = input("De qual unidade? (c, f, k): ")
        para_unidade = input("Para qual unidade? (c, f, k): ")
        valor = float(input("Valor: "))
        resultado = converter_temperatura(valor, da_unidade, para_unidade)
    elif escolha == "2":
        da_unidade = input("De qual unidade? (kg, g, lb, oz, t): ")
        para_unidade = input("Para qual unidade? (kg, g, lb, oz, t): ")
        valor = float(input("Valor: "))
        resultado = converter_peso(valor, da_unidade, para_unidade)
    elif escolha == "3":
        da_unidade = input("De qual unidade? (m, km, cm, mm, mi, ft, in, yd): ")
        para_unidade = input("Para qual unidade? (m, km, cm, mm, mi, ft, in, yd): ")
        valor = float(input("Valor: "))
        resultado = converter_distancia(valor, da_unidade, para_unidade)
    elif escolha == "4":
        da_unidade = input("De qual moeda? (usd, brl, eur...): ")
        para_unidade = input("Para qual moeda? (usd, brl, eur...): ")
        valor = float(input("Valor: "))
        resultado = converter_moeda(valor, da_unidade, para_unidade)
    else:
        print("Opção inválida!")
        sys.exit(1)

    print(f"{valor} {da_unidade.upper()} = {resultado:.2f} {para_unidade.upper()}")
    

if len(sys.argv) == 1:
    modo_interativo()
    sys.exit(0)
elif len(sys.argv) != 4:
    print("Precisa informar 3 valores!")
    print("Exemplo: python convert.py 100 usd brl")
    sys.exit(1)

try:
    valor = float(sys.argv[1])
except ValueError:
    print("Erro: o valor precisa ser algum número, ex: 100, 50.5")
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

print(f"{valor} {da_unidade.upper()} = {resultado:.2f} {para_unidade.upper()}")