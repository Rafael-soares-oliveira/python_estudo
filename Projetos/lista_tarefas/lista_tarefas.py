# Lista de Tarefas com desfazer e refazer

# todo = [] -> lista de tarefas <br>
# todo = ['fazer cafe'] -> Adicionar fazer café <br>
# todo = ['fazer café, 'caminhar'] -> Adicionar caminhar <br>
# desfazer = ['fazer café'] -> Refazer ['caminhar']
# desfazer = [] -> refazer ['caminhar', 'café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café','caminhar']

import os
import sys
import json

# Irá abrir o arquivo como leitura. Toda informação salva na lista de tarefas ou diretamente no 
# arquivo json continuará disponível na próxima execução
def ler(tarefas,caminho_arquivo): 
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados

# Irá abrir o arquivo como escrita. Irá salvar qualquer alteração na lista de tarefas no arquivo json
def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados

PATH_FILE = './Projetos/lista_tarefas.json' # Caminho do arquivo json
lista = ler([],PATH_FILE) # Lista será igual ao que está presente no arquivo json
lista_refazer = [] # Armazenará os itens desfeitos e que podem ser refeitos

# Função responsável pela adição de itens na lista. O loop será interrompido caso seja digitado 0(zero)
def adicionar_itens(tarefas):
    while True:
        item = input('Digite a tarefa ou 0 para voltar: ')
        item1 = input('Digite a tarefa ou 0 para voltar: ')
        item2 = input('Digite a tarefa ou 0 para voltar: ')
        item3 = input('Digite a tarefa ou 0 para voltar: ')
        item4 = input('Digite a tarefa ou 0 para voltar: ')
        if item == '0':
            os.system('clear')
            break
        else:
            tarefas.append([item1,item2,item3,item4])
    return tarefas

def listar(tarefas):
    if tarefas == []:
        print('Lista vazia!')
    for numero,itens in enumerate(tarefas):
            print(numero,'-',itens)
            
def desfazer(tarefas,tarefas_refazer):
    if tarefas == []:
        print('Lista vazia!')
    else:
        tarefas_refazer.append(tarefas[-1])
        tarefas.pop()
    return listar(tarefas)

def refazer(tarefas,tarefas_refazer):
    if tarefas_refazer == []:
        print('Não há o que refazer!')
    else:
        tarefas.append(tarefas_refazer[-1])
        tarefas_refazer.pop()
        return listar(tarefas)


def menu():
    while True:
        print('\nComandos:\n \
    [1]adicionar \n \
    [2]listar \n \
    [3]desfazer \n \
    [4]refazer \n \
    [5]limpar tela \n \
    [6]encerrar \n \
    [7]excluir lista\n \
    ')
        tarefa = input('Digite uma tarefa ou comando: ')
        
        if tarefa == '1':
            os.system('clear')
            adicionar_itens(lista)
        elif tarefa == '2':
            os.system('clear')
            listar(lista)
        elif tarefa == '3':
            os.system('clear')
            desfazer(lista,lista_refazer)
        elif tarefa == '4':
            os.system('clear')
            refazer(lista, lista_refazer)
        elif tarefa == '5':
            os.system('clear')
        elif tarefa == '6':
            break
        elif tarefa == '7':
            os.system('clear')
            print('Lista excluída!')
            lista.clear()
        else:
            print('Opção inválida!')
            
        salvar(lista,PATH_FILE)
menu()
