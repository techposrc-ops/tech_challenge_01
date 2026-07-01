#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Bibliotecas
import os
import joblib

from preprocessamento_rf import carregar_dados


# In[5]:


def main():

    base_dir = os.path.dirname(__file__)

    arquivo_entrada = os.path.join(
        base_dir, '..', 'data', 'raw', 'desafio_nps_fase_1.csv')

    df, X_pre, preprocesso = carregar_dados(arquivo_entrada)

    # carrega modelo
    modelo = joblib.load(os.path.join(base_dir, '..', 'models', 'modelo_rf.pkl'))

    # previsão
    df['nps_classificacao_prevista'] = modelo.predict(X_pre)

    # salva resultado
    arquivo_saida = os.path.join(base_dir, '..', 'outputs', 'data_classificacao.csv')

    df.to_csv(arquivo_saida, index=False, encoding='utf-8-sig')

    print("Arquivo salvo:", arquivo_saida)
    print(df[['nps_classification', 'nps_classificacao_prevista']].head())


# In[ ]:


# Executa o programa
if __name__ == '__main__':
    main()

