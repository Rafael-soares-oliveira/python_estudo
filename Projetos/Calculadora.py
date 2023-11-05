''' Calculadora
- Irá rodar até que seja digitado t!
- Ao digitar r irá reiniciar o programa
- Há a opção do programa pedir se o usuário deseja continuar ou terminar o programa.
'''
import os # importa a biblioteca os
import sys # importa a biblioteca sys

def menu(): # função do menu inicial
    print('''   #### CALCULADORA ####
        
        Operadores
        ** -> Potenciação
        // -> Divisão inteira
        % -> Módulo
        * -> Multiplicação
        / -> Divisão
        + -> Adição
        - -> Subtração
        
        Comandos
        t -> encerrar
        r -> reiniciar
        
        ## Será aceito apenas números! ##\n''')

def potenciacao(x,y):
    resultado = x**y
    print(f'\nResultado = {resultado}\n')
    
def divisao_inteira(x,y):
    resultado = x//y
    print(f'\nResultado = {resultado}\n')
    
def modulo(x,y):
    resultado = x % y
    print(f'\nResultado = {resultado}\n')

def multiplicacao(x,y):
    resultado = x * y
    print(f'\nResultado = {resultado}\n')
    
def divisao(x,y):
    resultado = x / y
    print(f'\nResultado = {resultado}\n')
    
def soma(x,y):
    resultado = x + y
    print(f'\nResultado = {resultado}\n')
    
def subtracao(x,y):
    resultado = x - y
    print(f'\nResultado = {resultado}\n')

def encerrar(): # função para encerrar o programa
    print("Encerrando...")
    sys.exit(0) # comando para encerrar o programa

def main(): # função principal

    available_operators = ['**','*','/','-','+','//','%'] # lista os operadores aceitos
    condition1 = 'n' # Condição para aceitar a primeira entrada
    condition2 = 'n' # condição para aceitar a segunda entrada
    operator = "" # Definição do operador

    menu()

    while condition1 == 'n': # Irá repetir até que o valor da varíavel condition1 altere
        input1 = input('\nDigite o primeiro número: ') # Entrada do primeiro número
        
        if input1 == 't': # Se inserir a letra t irá encerrar o programa
            encerrar() # executa a função de encerrar o programa
        
        elif input1 == 'r': # se inserir a letra r irá reiniciar o programa
            os.system('clear') # comando para limpar a tela do terminal
            menu()
        else:
            
            '''Irá tentar transformar a entrada em float, caso consiga, quer dizer que a entrada é um número 
            e a variável condition1 altera para "y". '''
            try:
                input1 = float(input1) 
                condition1 = 'y'
            except:
                print("Valor incorreto!")
            
            if condition1 == 'y': # Nesse caso aceita a entrada e continua o algoritmo
                print(input1)
                
                # Enquanto o operador inserido não estiver dentro da variável available_operators irá repetir a entrada
                while operator not in available_operators:
                    operator = input("\nDigite o operador: ")
                    
                    if operator == 'r': # Reinicia caso seja inserido a letra r
                        os.system('clear')
                        menu()
                        break
                    
                    if operator == 't':
                        encerrar()
                    
                    elif operator in available_operators: # Continua caso o operador estiver dentro da available_operators
                        print(input1, operator)
                        
                        while condition2 == 'n': # Repete a condição do primeiro número para o segundo
                            input2 = input('\nDigite o segundo número: ')
                            
                            if input2 == 'r': # Reinicia o programa
                                os.system('clear')
                                break
                            
                            elif input2 == 't':
                                encerrar()
                            
                            try: # Se a entrada for um número irá mudar a variável condition para 'y'
                                input2 = float(input2)
                                condition2 = 'y'
                            except:
                                print("Valor incorreto!")
                            
                            if condition2 == 'y': # Caso a entrada for um número continua
                                print(input1, operator, input2)                    
                                
                                if operator == '**': # Operação de exponenciação
                                    potenciacao(input1,input2)                              
                                    
                                elif operator == '//': # Operação de Divisão inteira
                                    divisao_inteira(input1,input2)
                                                                    
                                elif operator == '%': # Operação de Módulo
                                    modulo(input1,input2)
                                                                      
                                elif operator == '*': # Operação de Multipĺicação
                                    multiplicacao(input1,input2)                               
                                    
                                elif operator == '/': # Operação de Divisão
                                    divisao(input1,input2)
                                                                
                                elif operator == '+': # Operação de Adição
                                    soma(input1,input2)
                                                                  
                                elif operator == '-': # Operação de Subtração
                                    subtracao(input1,input2)

                                # Reinicia o programa
                                menu()
                                break
                        
        # Irá resetar os valores das varíaveis e o programa rodará infinitamente até que seja inserido a letra t
        condition1 = 'n' 
        condition2 = 'n'
        operator = ""
        
main()