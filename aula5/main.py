import pandas as pd
import numpy as np

def calcular_media_mediana(df, coluna):
    media = df[coluna].mean()
    mediana = df[coluna].median()
    return media, mediana


def calcular_variancia_desvio_padrao(df, coluna):
    variancia = df[coluna].var()
    desvio_padrao = df[coluna].std()
    return variancia, desvio_padrao


def calcular_soma_produto(df, coluna):
    soma = df[coluna].sum()
    produto = df[coluna].prod()
    return soma, produto


def calcular_correlacao(df, coluna1, coluna2):
    correlacao = df[coluna1].corr(df[coluna2])
    return correlacao


if __name__ == "__main__":
    data = {
      'A': [1,2,3,4,5],
      'B': [3,5,1,2,9],
      'C': [0,2,1,6,4]
    }
    df = pd.DataFrame(data)


    media_A, mediana_A = calcular_media_mediana(df, 'A')
    media_B, mediana_B = calcular_media_mediana(df, 'B')
    media_C, mediana_C = calcular_media_mediana(df, 'C')
    
    variancia_A, desvio_padrao_A = calcular_variancia_desvio_padrao(df, 'A')
    variancia_B, desvio_padrao_B = calcular_variancia_desvio_padrao(df, 'B')
    variancia_C, desvio_padrao_C = calcular_variancia_desvio_padrao(df, 'C')
    
    soma_A, produto_A = calcular_soma_produto(df, 'A')
    soma_B, produto_B = calcular_soma_produto(df, 'B')
    soma_C, produto_C = calcular_soma_produto(df, 'C')
    
    correlacao_A_B = calcular_correlacao(df, 'A', 'B')
    correlacao_B_C = calcular_correlacao(df, 'B', 'C')
    correlacao_C_A = calcular_correlacao(df, 'C', 'A')

    print("=======================================")
    print("Media - Mediana")
    print("=======================================")
    print(f"Media A: {media_A} - Mediana A: {mediana_A}")
    print(f"Media B: {media_B} - Mediana B: {mediana_B}")
    print(f"Media C: {media_C} - Mediana C: {mediana_C}")

    print("\n=======================================")
    print("Variancia - Desvio Padrão")
    print("=======================================")
    print(f"Variancia A: {variancia_A} - Desvio Padrão A: {desvio_padrao_A}")
    print(f"Variancia B: {variancia_B} - Desvio Padrão B: {desvio_padrao_B}")
    print(f"Variancia C: {variancia_C} - Desvio Padrão C: {desvio_padrao_C}")
    
    print("\n=======================================")
    print("Soma - Produto")
    print("=======================================")
    print(f"Soma A: {soma_A} - Produto A: {produto_A}")
    print(f"Soma B: {soma_B} - Produto B: {produto_B}")
    print(f"Soma C: {soma_C} - Produto C: {produto_C}")
    
    print("\n=======================================")
    print("Correlação")
    print("=======================================")
    print(f"Correlação entre A e B: {correlacao_A_B}")
    print(f"Correlação entre B e C: {correlacao_B_C}")
    print(f"Correlação entre C e A: {correlacao_C_A}")