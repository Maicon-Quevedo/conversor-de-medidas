# Conversor de Medidas

Converta temperatura, peso, distância e moeda direto pelo terminal.

## Como usar

Você pode rodar de duas formas:

**Modo direto** (passando os valores na linha de comando):
```bash
python main.py <valor> <unidade de origem> <unidade de destino>
```

**Modo interativo** (o programa pergunta tudo passo a passo):
```bash
python main.py
```

## Exemplos

```bash
python main.py 100 usd brl
python main.py 37 c f
python main.py 70 kg lb
python main.py 10 km mi
```

## Unidades suportadas

| Categoria   | Unidades                                 |
|-------------|------------------------------------------|
| Temperatura | c, f, k                                  |
| Peso        | kg, g, lb, oz, t                         |
| Distância   | m, km, cm, mm, mi, ft, in, yd            |
| Moeda       | usd, brl, eur e mais de 150 moedas       |

## Requisitos

- Python 3.6+
- Biblioteca `colorama` (instale com o comando abaixo)

```bash
pip install colorama
```

## Histórico

Toda conversão feita é salva automaticamente em `historico.json`, com data, valor e resultado.

Esse arquivo é local — ou seja, fica só na sua máquina e não é enviado pro GitHub (já está configurado no `.gitignore`). Cada pessoa que rodar o projeto terá seu próprio histórico.
