# Horário
from datetime import datetime
from pytz import timezone
 
format = "%d-%m-%Y %H:%M:%S" # Define o formato que apresentado, também é possível colocar direto na variável
 
horario_atual = datetime.now(timezone('UTC'))
agora_brasil = horario_atual.astimezone(timezone('America/Sao_Paulo'))


# Menu Inicial
menu = '''
---------------------------------------
              BANCO DIO
---------------------------------------

DIGITE A OPERAÇÃO QUE DESEJA REALIZAR:

  d - DEPOSITAR
  s - SACAR
  e - EXTRATO
  t - TERMINAR
  
  '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:

  opcao = input(menu)

# Depósito --------------------------------------------------------------------

  if opcao == 'd':
    valor_deposito = float(input(f'''Informe o valor a ser depositado: '''))

    if valor_deposito > 0:
      saldo  += valor_deposito
      extrato += f'Data: {agora_brasil.strftime(format)}  -  Depósito: R${valor_deposito: .2f}\n'
      print(f'Data: {agora_brasil.strftime(format)}  -  Depósito: R$ {valor_deposito: .2f} - ')
    else:
      print('Operação falhou! O valor informado é inválido')

# Saque -----------------------------------------------------------------------

  elif opcao == 's':
    valor_saque = float(input(f'''Informe o valor do saque: '''))
    excedeu_numero_saques = numero_saques >= limite_saques
    excedeu_saldo = valor_saque > saldo
    excedeu_limite = valor_saque > limite

    if excedeu_numero_saques:
      print('Operação falhou! Número máximo de saques excedido.')

    elif excedeu_saldo:
      print('Operação falhou! O valor do saque excede o saldo.')

    elif excedeu_limite:
      print('Operação falhou! O valor do saque excede o limite.')

    elif valor_saque > 0:
      saldo -= valor_saque
      extrato += f'Data: {agora_brasil.strftime(format)}  -  Saque: R${valor_saque: .2f}\n'
      numero_saques += 1
      print(f'Data: {agora_brasil.strftime(format)}  -  Saque: R$ {valor_saque: .2f}')
      print(f'Quantidade de saques utilizados: {numero_saques} / {limite_saques}')
    else:
      print('Operação falhou! O valor informado é inválido')

# Extrato ---------------------------------------------------------------------

  elif opcao == 'e':
    print('==========EXTRATO==========')
    if not extrato:
        print('Não foram realizadas movimentações.')
    else: 
        print(extrato) 
    print(f'Saldo Total: R${saldo: .2f}')
    print('===========================')

# Terminar --------------------------------------------------------------------

  elif opcao == 't':
    print(f'''
---------------------------------------
              BANCO DIO
---------------------------------------
        
                 FIM!''')
    break

# Erro -----------------------------------------------------------------------

  else:
    print('Operação inválida, por favor selecione novamente a operação desejada.')
