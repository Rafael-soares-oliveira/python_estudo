'''
Faça uma lista de compras com listas
- O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
- Não permita que o programa quebre com erros de índices inexistentes na lista
'''

import os 
lista_compras = []

def list(): # Impressão da lista com índice
    print("\n## Lista de Compras ##\n \nc - cancelar último item \nr - remover item específico\nl - limpar lista \nt - terminar\n")
    for indice, nome in (enumerate(lista_compras, start=1)):
        print(indice, nome)
        
def limpar_tela(): # limpar o terminal
    os.system('clear')

while True:
    limpar_tela() # Irá iniciar com o terminal limpo
    list() # Irá apresentar a lista
    item = input("\nDigite o item a ser adicionado: ") # Entrada do item a ser adicionado
    limpar_tela() # Limpa a tela novamente
    
    if item == 't': # Se a entrada for t, irá encerrar o programa
        list()
        print("Encerrando...")
        break
    
    elif item == 'l': # Se a entrada for l, irá excluir a lista, porém pedirá confirmação
        confirmacao = input("Certeza que deseja limpar a lista? \n[s]im \n[n]ão\n ")
        if confirmacao == 's':
            lista_compras = []
        else:
            continue
    
    elif item == 'c': # Irá excluir o último item adicionado
        lista_compras.pop()
    
    elif item == '':
        continue
    
    elif item == 'r': # Irá remover um determinado item de acordo com a sua posição
        list()
        
        if len(lista_compras) <= 1: # Se a quantidade de itens na lista for 0 ou 1, irá remover o item da lista
            lista_compras = []
            
        
        else:
            while True:
                posicao = input("\nDigite o número do item que deseja remover: ") # Pedirá o número do item a ser removido
                
                if posicao == '': 
                    break
                
                elif not posicao.isnumeric():
                    continue
                    
                elif posicao.isnumeric():
                    posicao = int(posicao)
            
                    if posicao < 1 or posicao > len(lista_compras):
                        limpar_tela()
                        print(f"Item {posicao} inexistente.\n")
                        list()
                    
                    else:
                        lista_compras.pop(posicao-1)
                        break
                
    else:
        lista_compras.append(item)
        
