import sys

from conversor.funcoes_conversoes import converter_temperatura, converter_peso, converter_distancia, converter_moeda

if len(sys.argv) != 4:
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