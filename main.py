# Escolha uma das funções (def) já criadas e crie 2 funções de teste,
# uma lendo uma lista de valores no próprio script e outra lendo um arquivo csv.
# Ambas devem conter pelo menos 2 testes.

# Função escolhida: Fósforos

import pytest
import csv

teste_palitos_fosforos_positivo = [
    (2,80),        #teste1
    (10,400)       #teste2
]

teste_palitos_fosforos_negativo = [
    (-1, 'Numero inválido. Digite um número positivo.'),      #teste1
    (-3, 'Numero inválido. Digite um número positivo.')       #teste2
]

def calcular_fosforos(caixa):
    if caixa > 0:
        return caixa * 40
    else:
        return 'Numero inválido. Digite um número positivo.'


# Testes
@pytest.mark.parametrize('caixa,resultado', teste_palitos_fosforos_positivo)
def test_calcular_fosforos_positivo(caixa, resultado):
    assert calcular_fosforos(caixa) == resultado

@pytest.mark.parametrize('caixa,resultado', teste_palitos_fosforos_negativo)
def test_calcular_fosforos_negativo(caixa, resultado):
    assert calcular_fosforos(caixa) == resultado

def ler_dados_csv():
    teste_dados_csv = []
    nome_arquivo = 'fosforos.csv'
    try:
        with open(nome_arquivo,newline='') as csvfile:
            dados = csv.reader(csvfile,delimiter=',')
            next(dados)
            for row in dados:
                i = [int(row[0])]
                teste_dados_csv.append(row)
        return teste_dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {nome_arquivo}')
    except Exception as err:
        print(f'Erro imprevisto: {err}')

@pytest.mark.parametrize('caixa,resultado', ler_dados_csv())
def test_calcular_fosforos_csv(caixa, resultado):
    assert calcular_fosforos(int(caixa)) == int(resultado)