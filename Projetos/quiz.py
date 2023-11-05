# Bibliotecas ------------------------------------------------------------------------------------------------
import sys
import os

# Variáveis----------------------------------------------------------------------------------------------------
perguntas = {
    "Questão 1": {
        'Pergunta': 'Quanto é 2+2?',
        'Opçoẽs': ['1','3','4','5'],
        'Resposta': '4',
    },
    'Questão 2': {
        'Pergunta': 'Quanto é 5*5?',
        'Opçoẽs': ['25','55','10','51'],
        'Resposta': '25',
        },
    'Questão 3': {
        'Pergunta': 'Quanto é 10/2?',
        'Opçoẽs': ['4','5','2','1'],
        'Resposta': '5',
        }
}

i = 0 # Incremental
acertos = 0

keys = [] # Isolar apenas as keys
for key in perguntas:
    keys.append(key)
    
# Funções --------------------------------------------------------------------------------------------------
def menu(): # Logo
    menu = '### QUIZ ###'
  
def questao(): # Irá alterar a questão conforme o incremental i altera
    print(f"  {keys[i]}\n{perguntas[keys[i]]['Pergunta']}")

def resposta(): # Input para responder
    return input('Escolha a alternativa: ')

def alternativas():
    for alternativa,opcoes in enumerate(perguntas[keys[i]]['Opçoẽs']):
        print(f'{alternativa}) {opcoes}')

def resposta_corresta():
    resposta_corresta = list(perguntas[keys[i]]['Opçoẽs']).index(perguntas[keys[i]]['Resposta'])
    return str(resposta_corresta)
 
#Inicio do quiz --------------------------------------------------------------------------------------------
while True:
    menu()
    
    while i < len(keys):
        questao()
        alternativas()
        
        if resposta() == resposta_corresta():
            print('Resposta Correta!\N{thumbs up sign}\n')
            i += 1
            acertos += 1
        
        else: 
            print('Resposta incorreta!\N{thumbs down sign}\n')
            i += 1
            
    print(f"Fim de Jogo! Acertou {acertos}/{len(keys)}")
    break
