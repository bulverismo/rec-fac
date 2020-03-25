#!/usr/bin/env python3

import os
import pickle

# arquivo do banco de dados tem que ser criado
# de forma semelhante a esta
# arquivo_dat = 'registro-faces.dat'

def criadat(arquivo_dat):
    # aqui é onde deve buscar o banco de rosto ja guardados
    if os.path.exists(arquivo_dat):
        print("O arquivo ",arquivo_dat," ja existia")
        # abrir o arquivo_dat
        
        with open(arquivo_dat, 'rb') as f:
            codificacoesDeFaceConhecidas = pickle.load(f)
            
        # preencher as variaveis com os valores do arquivo_dat e
        # carregar todas as codificações das faces
    
        # grave uma lista dos nomes e uma das codificações ou inicialize com vazio caso não tenha nada salvo
        if (len(codificacoesDeFaceConhecidas)>0):
                
            nomesDeFaceConhecidas = list(codificacoesDeFaceConhecidas.keys())
            codificacoesDeFaceConhecidas = list(codificacoesDeFaceConhecidas.values())
        else:
            
            nomesDeFaceConhecidas = [] 
            codificacoesDeFaceConhecidas = []
    
    else:
        # caso o arquivo do banco de dados não exista crie e preencha as variaveis com vazio
        pickle.dump([], open( arquivo_dat, "wb" ))
        print("O arquivo ",arquivo_dat," não existia e foi criado")
    
        # abrir o arquivo recém criado que esta vazio
        with open(arquivo_dat, 'rb') as f:
            codificacoesDeFaceConhecidas = pickle.load(f)
            
        # preencher as variaveis com os valores do arquivo_dat e
        # carregar todas as codificações das faces
    
        # grave uma lista dos nomes e uma das codificações
        nomesDeFaceConhecidas = [] 
        codificacoesDeFaceConhecidas = []
    
    return [ nomesDeFaceConhecidas, codificacoesDeFaceConhecidas ]
# exemplo de como usar o retorno
# retorno = criadat(arquivo_dat)
# print("Nome das faces carregadas do arquivo ",arquivo_dat)
# print(retorno[0])

