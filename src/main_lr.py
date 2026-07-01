#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Bibliotecas
import os
import joblib

from preprocessamento_lr import carregar_dados


# In[2]:


# Função principal
def main():

    base_dir = os.path.dirname(__file__)

    # Caminho do arquivo de entrada
    arquivo_entrada = os.path.join(
        base_dir,
        '..',
        'data',
        'raw',
        'desafio_nps_fase_1.csv'
    )

    # Carrega os dados
    df, X = carregar_dados(arquivo_entrada)

    # Carrega o modelo treinado
    arquivo_modelo = os.path.join(
        base_dir,
        '..',
        'models',
        'modelo_lr.pkl'
    )

    modelo = joblib.load(arquivo_modelo)

    # Realiza as previsões
    df['nps_previsto'] = modelo.predict(X)

    # Caminho do arquivo de saída
    arquivo_saida = os.path.join(
        base_dir,
        '..',
        'outputs',
        'data_regressao.csv'
    )

    # Salva o resultado
    df.to_csv(
        arquivo_saida,
        index=False,
        encoding='utf-8-sig'
    )

    print(f'Arquivo salvo com sucesso: {arquivo_saida}')
    print(df[['nps_score', 'nps_previsto']].head())


# In[ ]:


# Executa o programa
if __name__ == '__main__':
    main()
