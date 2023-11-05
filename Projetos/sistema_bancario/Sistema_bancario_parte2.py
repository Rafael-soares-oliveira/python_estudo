# Horário
from datetime import datetime
from pytz import timezone
import textwrap
 
format = "%d-%m-%Y %H:%M:%S" # Define o formato da data
 
horario_atual = datetime.now(timezone('UTC'))
agora_brasil = horario_atual.astimezone(timezone('America/Sao_Paulo'))

def menu():
    menu = """
    
----------------------------------------------
              BANCO DIO
----------------------------------------------
    
    ================ MENU ================
    
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [c]\tNova conta
    [l]\tListar contas
    [u]\tNovo usuário
    [t]\tTerminar
    
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Data: {agora_brasil.strftime(format)}  -  Depósito:\tR$ {valor:.2f}\n"
        print(f'\n Data: {agora_brasil.strftime(format)}  -  Depósito: R$ {valor: .2f}')
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite. ")

    elif excedeu_saques:
        print(" Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Data: {agora_brasil.strftime(format)}  -  Saque: \tR$ {valor:.2f}\n"
        numero_saques += 1
        print(f'\nData: {agora_brasil.strftime(format)}  -  Saque: R$ { valor: .2f}')
        print(f'Quantidade de saques utilizados: {numero_saques} / {limite_saques}')

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("\nNão foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios, endereco):
    cpf = input("Informe o CPF (somente número, sem traço): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nCPF já cadastrado!")
        return

    nome = input("Informe nome completo: ")
    data_nascimento = input("Informe data de nascimento (dd-mm-aaaa): ")
    logradouro = input("Informe logradouro e número: ")
    bairro = input("Informe o bairro: ")
    cidade_estado = input("Informe cidade/sigla do estado: ")
    # endereco = input("Informe endereço (logradouro, número - bairro - cidade/sigla estado): ")
    endereco.append({"logradouro": logradouro, "bairro": bairro, "cidade/estado": cidade_estado})

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("\n\t\t=== Usuário cadastrado! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf] # Faz busca no dicionário se já há cpf cadastrado
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(f"""\nCPF:\t {cpf} \nAgência: {agencia} \nC/C:\t {numero_conta}""")
        print("\n=== Conta criada! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado, fluxo de criação de conta encerrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}\n
            -------------------------------------
        """

        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3 # Quantidade máxima de saques por operação, constante
    AGENCIA = "0001" # Número da agência, constante

    saldo = 0
    limite = 500 # Limite de saque a cada saque
    extrato = "" 
    numero_saques = 0
    usuarios = []
    contas = []
    endereco = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            criar_usuario(usuarios, endereco)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "t":
            print(f'''
---------------------------------------
              BANCO DIO
---------------------------------------
        
                 FIM!''')
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
