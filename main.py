"""
Desafio: Criar uma calculadora estatística simples em Python

Tarefa:
Implemente as funções abaixo para calcular média, mediana e moda de uma lista de números.

Instruções:
1. Faça o fork deste repositório no seu GitHub.
2. Clone o seu fork para sua máquina.
3. Complete as funções abaixo.
4. Teste o código executando: python calculadora_estatistica.py
5. Envie um Pull Request com a sua solução.

💡 Dica: não use bibliotecas externas como numpy ou statistics.
"""

# Função para calcular a média
def calcular_media(lista):
    soma = 0
    for item in lista:
       soma += item

    return soma/len(lista)


def calcular_mediana(lista):
    tamanho = len(lista)
    if tamanho&2 != 0:
        return lista[tamanho//2]

    return (lista[tamanho/2 -1] + lista[tamanho/2]) / 2


def calcular_moda(lista):
    contagem = {}
    for item in lista:
        if num in contagem:
            contagem[num] += 1
        else:
            contagem[num] = 1

    max_ocorrencias = max(contagem.values())
    return = [num for num, freq in contagem.items() if freq == max_ocorrencias]


def main():
    try:
        numeros = [10, 20, 20, 30, 40, 40, 40, 50]

        print("📊 Calculadora Estatística")
        print(f"Lista de números: {numeros}")
        print(f"Média: {calcular_media(numeros)}")
        print(f"Mediana: {calcular_mediana(numeros)}")
        print(f"Moda: {calcular_moda(numeros)}")

    except Exception as e:
        print(f"⚠️ Ocorreu um erro: {e}")


if __name__ == "__main__":
    main()
