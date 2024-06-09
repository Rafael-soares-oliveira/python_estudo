"""Sistema Bancário
É possível:
- Criar Conta:
    - Pessoa Física
        - Conta Salário
        - Conta Corrente Padrão
        - Conta Corrente Premium
        - Conta Poupança
    - Pessoa Jurídica
        - Conta Jurídica Padrão
        - Conta Jurídica Premium

- Acessar Conta:
    - Saque -> não é possível sacar valor maior que o seu saldo
    - Depósito
    - Extrato
    - Ver Saldo
    - Ver Dados

- Restrições de cadastro:
    - CPF e CNPJ único com verificação dos dois últimos dígitos
    - Senha Mascarada com * com contra-prova para criar
    - DDD possui apenas 2 digítos
    - Telefone possui 8 ou 9 dígitos
    - Data conforme calendário

- Possíveis melhorias:
    - Impor limites para cada tipo de conta -> acrescentar limitações dentro da
    classe Conta
    - Opção de remover contas e armazená-las em outro arquivo JSON
    - Opção de alterar modelo da conta e dados dos usuários e password dentro
    da Operação Acessar Conta
"""

import json
import os
import sys
# Módulos
from datetime import date, datetime

import maskpass
from pytz import timezone


class PessoaFisica:
    # Classes de criação
    def __init__(self):
        self.TIPO = "PESSOA FISICA"
        self.NOME = self.nome()
        self.CPF = self.cpf()
        self.ENDERECO = self.endereco()
        self.ANIVERSARIO = self.data_nascimento()
        self.TELEFONE = self.telefone()
        self.EMAIL = self.email()

    def nome(self):
        self.NOME = input("NOME: ").upper()
        return self.NOME

    def cpf(self):
        self.CPF = verif_cpf()
        return self.CPF

    def data_nascimento(self):
        while True:
            try:
                x1 = int(input("DIA NASCIMENTO: "))
                x2 = int(input("MÊS NASCIMENTO: "))
                x3 = int(input("ANO NASCIMENTO: "))
                x4 = date(x3, x2, x1)  # Transform inputs in date format
                self.ANIVERSARIO = (
                    str(x4.day).zfill(2)
                    + "-"
                    + str(x4.month).zfill(2)
                    + "-"
                    + str(x4.year)
                )
                return self.ANIVERSARIO
            except ValueError:
                print("DATA INVÁLIDA!")

    def telefone(self):
        while True:
            ddd = input("DDD: ")
            if len(ddd) != 2:  # Max 2 digits
                print("DDD INVÁLIDO!")
            else:
                break
        while True:
            telefone = input("TELEFONE: ")
            if len(telefone) < 8 or len(telefone) > 9:  # 8 or 9 digits
                print("TELEFONE INVÁLIDO!")
            else:
                break
        self.TELEFONE = str(ddd) + "-" + str(telefone)
        return self.TELEFONE

    def endereco(self):
        rua = input("ENDERECO: ").upper()
        complemento = input("COMPLEMENTO: ")
        self.ENDERECO = rua + " - " + complemento
        return self.ENDERECO

    def email(self):
        self.EMAIL = input("EMAIL: ")
        return self.EMAIL


class ContaPessoaFisica:
    def __init__(self):
        self.TIPO = None
        self.AGENCIA = "0001"
        self.NUMERO = None
        self.SALDO = 0
        self.PASSWORD = self.password()

    @classmethod
    def conta_salario(cls, numero):
        conta = cls()
        conta.TIPO = "SALÁRIO"
        conta.NUMERO = str(numero).zfill(4)
        return conta

    @classmethod
    def conta_corrente_padrao(cls, numero):
        conta = cls()
        conta.TIPO = "CORRENTE PADRÂO"
        conta.NUMERO = str(numero).zfill(4)
        return conta

    @classmethod
    def conta_corrente_premium(cls, numero):
        conta = cls()
        conta.TIPO = "CORRENTE PREMIUM"
        conta.NUMERO = str(numero).zfill(4)
        return conta

    @classmethod
    def conta_poupanca(cls, numero):
        conta = cls()
        conta.TIPO = "POUPANÇA"
        conta.NUMERO = str(numero).zfill(4)
        return conta

    def password(self):
        while True:
            self.PASSWORD = maskpass.askpass(prompt="\nPASSWORD: ", mask="*")
            confirm_password = maskpass.askpass(
                prompt="CONFIRMAÇÂO PASSWORD: ", mask="*"
            )
            if self.PASSWORD == confirm_password:
                return self.PASSWORD
            print("Senhas não coincidem!\n")


class PessoaJuridica:
    def __init__(self):
        self.TIPO = "PESSOA JURIDICA"
        self.NOME = self.nome()
        self.CNPJ = self.cnpj()
        self.ENDERECO = self.endereco()
        self.FUNDACAO = self.data_fundacao()
        self.CFO = self.cfo()
        self.TELEFONE = self.telefone()
        self.EMAIL = self.email()

    def nome(self):
        self.NOME = input("NOME: ").upper()
        return self.NOME

    def cnpj(self):
        self.CNPJ = verif_cnpj()
        return self.CNPJ

    def data_fundacao(self):
        while True:
            try:
                x1 = int(input("DIA FUNDAÇÃO: "))
                x2 = int(input("MÊS FUNDAÇÃO: "))
                x3 = int(input("ANO FUNDAÇÃO: "))
                x4 = date(x3, x2, x1)  # Transform inputs in date format
                self.FUNDACAO = (
                    str(x4.day).zfill(2)
                    + "-"
                    + str(x4.month).zfill(2)
                    + "-"
                    + str(x4.year)
                )
                return self.FUNDACAO
            except ValueError:
                print("DATA INVÁLIDA!")

    def telefone(self):
        while True:
            ddd = input("DDD: ")
            if len(ddd) != 2:  # Max 2 digits
                print("DDD INVÁLIDO!")
            else:
                break
        while True:
            telefone = input("TELEFONE: ")
            if len(telefone) < 8 or len(telefone) > 9:  # 8 or 9 digits
                print("TELEFONE INVÁLIDO!")
            else:
                break
        self.TELEFONE = str(ddd) + "-" + str(telefone)
        return self.TELEFONE

    def endereco(self):
        rua = input("ENDEREÇO: ").upper()
        complemento = input("COMPLEMENTO: ")
        self.ENDERECO = rua + " - " + complemento
        return self.ENDERECO

    def cfo(self):
        self.CFO = input("RESPONSÁVEL FINANCEIRO: ")
        return self.CFO

    def email(self):
        self.EMAIL = input("EMAIL: ")
        return self.EMAIL


class ContaPessoaJuridica:
    def __init__(self):
        self.TIPO = None
        self.AGENCIA = "0001"
        self.NUMERO = None
        self.SALDO = 0
        self.PASSWORD = self.password()

    @classmethod
    def conta_juridica_padrao(cls, numero):
        conta = cls()
        conta.TIPO = "JURIDICO PADRÃO"
        conta.NUMERO = str(numero).zfill(4)
        return conta

    @classmethod
    def conta_juridica_premium(cls, numero):
        conta = cls()
        conta.TIPO = "JURIDICO PREMIUM"
        conta.NUMERO = str(numero).zfill(4)
        return conta

    def password(self):
        while True:
            self.PASSWORD = maskpass.askpass(prompt="\nPASSWORD: ", mask="*")
            confirm_password = maskpass.askpass(
                prompt="CONFIRMAÇÂO PASSWORD: ", mask="*"
            )
            if self.PASSWORD == confirm_password:
                return self.PASSWORD
            print("Senhas não coincidem!\n")


# Funções de validação
def verif_cnpj():
    """Validador de CNPJ

    PARTE 1
    Algorismos validadores parte 1 = [5,4,3,2,9,8,7,6,5,4,3,2]
    Ex: 11.222.333/0001-81
    -- 5 -- 4 -- 3 -- 2 --- 9 --- 8 --- 7 --- 6 -- 5 -- 4 -- 3 -- 2
    -- 1 -- 1 -- 2 -- 2 --- 2 --- 3 --- 3 --- 3 -- 0 -- 0 -- 0 -- 1
    -- 5 -- 4 -- 6 -- 4 -- 18 -- 24 -- 21 -- 18 -- 0 -- 0 -- 0 -- 2

    Passo 1: Multiplica os 12 primeiros dígitos pelos algarismos validadores:
    Passo 2: Soma dos valores = 102
    Passo 3: Resto da divisão entre Passo 2 e 11 = 3
    Passo 4: Se o resto da divisão for menor que 2, o resultado é 0, caso
    contrário o resultado é igual a 11 - Passo 3. -> 11-3 = 8

    =======================================================================
    PARTE 2
    Algorismos validadores parte 2 = [6,5,4,3,2,9,8,7,6,5,4,3,2]
    -- 6 -- 5 -- 4 -- 3 -- 2 --- 9 --- 8 --- 7 -- 6 -- 5 -- 4 -- 3 --- 2
    -- 1 -- 1 -- 2 -- 2 -- 2 --- 3 --- 3 --- 3 -- 0 -- 0 -- 0 -- 1 --- 8
    -- 6 -- 5 -- 8 -- 6 -- 4 -- 27 -- 24 -- 21 -- 0 -- 0 -- 0 -- 3 -- 16

    Passo 1: Multiplica os 12 primeiros dígitos pelos algarismos validadores:
    Passo 2: Soma dos valores = 120
    Passo 3: Resto da divisão entre Passo 2 e 11 = 10
    Passo 4: Se o resto da divisão for menor que 2, o resultado é 0, caso
    contrário o resultado é igual a 11 - Passo 3. -> 11-10 = 1
    """
    import re

    validadores = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    while True:
        cnpj = input("CNPJ: ")
        cnpj_filtrado = re.sub(r"[^0-9]", "", cnpj)

        if len(cnpj_filtrado) != 14:
            print("CNPJ Inválido!")
            continue
        else:
            break

    cnpj_list = [x for x in cnpj_filtrado[:12]]

    cnpj_passo1_1 = [int(x) * int(y) for x, y in zip(cnpj[:12], validadores)]
    cnpj_passo2_1 = sum(cnpj_passo1_1)
    cnpj_passo3_1 = cnpj_passo2_1 % 11
    cnpj_passo4_1 = 0 if cnpj_passo3_1 < 2 else 11 - cnpj_passo3_1

    cnpj_list.append(str(cnpj_passo4_1))
    validadores.insert(0, 6)

    cnpj_passo1_2 = [int(x) * int(y) for x, y in zip(cnpj_list[:13], validadores)]
    cnpj_passo2_2 = sum(cnpj_passo1_2)
    cnpj_passo3_2 = cnpj_passo2_2 % 11
    cnpj_passo4_2 = 0 if cnpj_passo3_2 < 2 else 11 - cnpj_passo3_2
    cnpj_list.append(str(cnpj_passo4_2))

    if [x for x in cnpj_filtrado] == cnpj_list:
        return cnpj_filtrado
    else:
        print("CNPJ Inválido!")


def verif_cpf():
    """Válidador de CPF

    Part 1 - Calculation of the first digit
    Step 1: Multiplies each of the first 9 digits by a countdown starting at 10
    Ex:     -- 10 --- 9 -- 8 -- 7 -- 6 -- 5 -- 4 -- 3 -- 2
            --- 7 --- 4 -- 6 -- 8 -- 2 -- 4 -- 8 -- 9 -- 0 -> CPF
            -- 70 -- 36 - 48 - 56 - 12 - 20 - 32 - 27 -- 0
    Step 2: Sum all the results -> 70+36+48+56+12+20+32+27+0 = 301
    Step 3: Multiply the previous result by 10 -> 301 * 10 = 3010
    Step 4: Get the remainder from dividing the step 3 by 11 -> 3010 % 11 = 7
    Step 5: If the previous result is greater than 9: result is equal to 0,
    otherwise is equal to step 4

    Part 2 - Calculation of the second digit
    Step 1: Multiplies each of the first 9 digits plus the result of part 1 by
    a countdown starting at 11
    Ex: 746.824.890-70 (746824890)
            -- 11 -- 10 -- 9 -- 8 -- 7 -- 6 -- 5 -- 4 -- 3 -- 2
            --- 7 --- 4 -- 6 -- 8 -- 2 -- 4 -- 8 -- 9 -- 0 -- 7 -> CPF
            -- 70 -- 36 - 48 - 56 - 12 - 20 - 32 - 27 -- 0 - 14
    Step 2: Sum all the results -> 70+36+48+56+12+20+32+27+0+14 = 363
    Step 3: Multiply the previous result by 10 -> 363 * 10 = 3630
    Step 4: Get the remainder from dividing the step 3 by 11: -> 3630 % 11 = 0
    Step 5: If the previous result is greater than 9: result is equal to 0,
    otherwise is equal to step 4
    """
    import re

    while True:
        while True:
            cpf = input("CPF: ")
            cpf_filtered = re.sub(r"[^0-9]", "", cpf)  # Filter for number only
            if len(cpf_filtered) == 11:  # Only accepted if it has 11 digits
                break
            else:
                print("INVALID CPF!")
                continue

        cpf_filtered_9digits = []
        step1_1 = []
        i1 = 0
        m1 = 10

        while i1 < 9:  # Only the first 9 digits
            cpf_filtered_9digits.append(cpf_filtered[i1])
            cpf_filtered_9digits[i1] = int(cpf_filtered_9digits[i1])
            step1_1.append(cpf_filtered_9digits[i1] * m1)  # Step 1
            i1 += 1
            m1 -= 1

        step2_1 = sum(step1_1)  # step 2
        step3_1 = step2_1 * 10  # step 3
        step4_1 = step3_1 % 11  # step 4
        # step5
        if step4_1 > 7:
            step5_1 = 0
        else:
            step5_1 = step4_1

        cpf_verified = cpf_filtered_9digits
        cpf_verified.append(step5_1)
        step1_2 = []
        i2 = 0
        m2 = 11

        while i2 < 10:
            # Assegura que os valores são int
            cpf_verified[i2] = int(cpf_verified[i2])
            step1_2.append(cpf_verified[i2] * m2)  # step 1
            i2 += 1
            m2 -= 1

        step2_2 = sum(step1_2)  # step 2
        step3_2 = step2_2 * 10  # step 3
        step4_2 = step3_2 % 11  # step 4
        # step5
        if step4_2 > 7:
            step5_2 = 0
        else:
            step5_2 = step4_2
        cpf_verified.append(step5_2)  # Adiciona o resultado do step 5

        cpf_test = ""
        for i in range(len(cpf_filtered)):
            cpf_test += str(cpf_verified[i])
            i += 1

        if cpf_test == cpf_filtered:  # Compara o cpf inserido com o resultado
            return cpf_filtered
        else:
            print("CPF INVALID! CPF DOES NOT EXIST!")
            continue


# Classes de menu


class Menu:
    def __init__(self):
        self.texto = None

    @staticmethod
    def inicial():
        print("\n======== BANCO XYZ ========")
        print()
        print(
            "1 - Criar Conta \n2 - Acessar Conta \n3 - Limpar Tela\
              \n4 - Encerrar\n"
        )
        option = input("Escolha a operação: ")
        return option

    @staticmethod
    def cadastro_cliente():
        print("\n==== CADASTRO DE CLIENTES ====")
        print()
        print("1 - Pessoa Física \n2 - Pessoa Jurídica\n")
        option = input("Escolha o tipo de cliente: ")
        return option

    @staticmethod
    def cadastro_conta_pf():
        print("\n==== CADASTRO DE CONTAS - PESSOA FÍSICA ====")
        print()
        print(
            "1 - Conta Salário \n2 - Conta Corrente Padrão\
              \n3 - Conta Corrente Premium \n4 - Conta Poupança\n"
        )
        option = input("Escolha o tipo de conta: ")
        return option

    @staticmethod
    def cadastro_conta_pj():
        print("\n==== CADASTRO DE CONTAS - PESSOA JURÍDICA ====")
        print()
        print("1 - Conta Jurídica Padrão \n2 - Conta Jurídica Premium\n")
        option = input("Escolha o tipo de conta: ")
        return option

    @staticmethod
    def login():
        print("======== BANCO XYZ ========")
        print()
        print("AGÊNCIA: 0001")
        numero = input("NÚMERO: ")
        password = maskpass.askpass(prompt="PASSWORD: ", mask="*")
        print()
        return numero, password

    @staticmethod
    def operacoes():
        print("\n======== BANCO XYZ ========\n")
        print("OPERAÇÕES")
        print(
            "1 - SACAR \n2 - DEPOSITAR \n3 - EXTRATO \n4 - CONSULTA SALDO\
              \n5 - CONSULTAR CADASTRO \n6 - ENCERRAR\n"
        )
        return input("OPERAÇÃO: ")


# Funções de operação


def cadastro_pessoa_fisica(cadastros):
    while True:
        os.system("clear")
        print("\n==== CADASTRO PESSOA FÍSICA ====")
        print()
        variavel = vars(PessoaFisica())
        os.system("clear")
        for x, y in variavel.items():
            print(x, ":", y)
        print()

        while True:
            confirm = input("Confirma os dados: \n1 - Sim \n2 - Não \n3 - Cancelar ")
            if confirm == "1":
                try:
                    if variavel["CPF"] in [x["CPF"] for x in cadastros]:
                        print("\nCPF já cadastrado!\n")
                        return 0
                    else:
                        return variavel
                except KeyError:
                    return variavel
            elif confirm == "2":
                break
            elif confirm == "3":
                sys.exit()
            else:
                print("Opção inválida!")
                continue


def cadastro_pessoa_juridica(cadastro):
    while True:
        os.system("clear")
        print("\n==== CADASTRO PESSOA JURÍDICA ====")
        print()
        variavel = vars(PessoaJuridica())
        os.system("clear")
        for x, y in variavel.items():
            print(x, ":", y)
        while True:
            confirm = input("\nConfirma os dados: \n1 - Sim \n2 - Não \n3 - Cancelar ")
            if confirm == "1":
                try:
                    if variavel["CNPJ"] in [x["CNPJ"] for x in cadastro]:
                        print("CNPJ já cadastrado!\n")
                        return 0
                    else:
                        return variavel
                except KeyError:
                    return variavel
            elif confirm == "2":
                break
            elif confirm == "3":
                sys.exit()
            else:
                print("Opção inválida!")
                continue


def cadastro_contas_pf(
    variavel,
    tipo_conta,
    cadastro,
    contas,
    caminho_cadastro,
    caminho_contas,
    extrato,
    caminho_extrato,
):
    variavel2 = vars(tipo_conta)
    variavel2.update({"CPF": variavel["CPF"]})
    cadastro.append(variavel)
    contas.append(variavel2)
    extrato.append({"NUMERO": variavel2["NUMERO"], "EXTRATO": []})
    save(cadastro, caminho_cadastro)
    save(contas, caminho_contas)
    save(extrato, caminho_extrato)


def cadastro_contas_pj(
    variavel,
    tipo_conta,
    cadastro,
    contas,
    caminho_cadastro,
    caminho_contas,
    extrato,
    caminho_extrato,
):
    variavel2 = vars(tipo_conta)
    variavel2.update({"CNPJ": variavel["CNPJ"]})
    cadastro.append(variavel)
    contas.append(variavel2)
    extrato.append({"NUMERO": variavel2["NUMERO"], "EXTRATO": []})
    save(cadastro, caminho_cadastro)
    save(contas, caminho_contas)
    save(extrato, caminho_extrato)


def acessar_conta(tentativa, funcao, lista_pf, lista_pj):
    if tentativa == 3:
        print("Máxima tentativa de acesso! Sistema será encerrado!")
        sys.exit()
    # PF
    else:
        numero_inserido, password_inserido = funcao
        condicao1 = [x for x in lista_pf if x["NUMERO"] == numero_inserido]
        condicao2 = [x for x in lista_pf if x["PASSWORD"] == password_inserido]
        if condicao1 == condicao2 and condicao1 != []:
            os.system("clear")
            return condicao1, "pf"
        # PJ
        else:
            condicao1 = [x for x in lista_pj if x["NUMERO"] == numero_inserido]
            condicao2 = [x for x in lista_pj if x["PASSWORD"] == password_inserido]
            if condicao1 == condicao2 and condicao1 != []:
                os.system("clear")
                return condicao1, "pj"
            else:
                print("Acesso Negado!\n")
                print(f"Tentativa {tentativa}/3\n")
                return 0, 0


def sacar(
    acesso,
    lista_pf,
    y,
    path_conta_pf,
    lista_pj,
    path_conta_pj,
    list_extrato,
    path_extrato,
    horario,
):
    os.system("clear")
    print("\n======== SAQUE ========")
    print()
    valor = input("Valor do saque: ")
    try:
        valor = float(valor)
        saldo = acesso["SALDO"] - valor
        if saldo < 0:
            print("Saldo Insuficiente!")
            return
        acesso.update({"SALDO": saldo})
        extrato = f"{horario} -> Saque: R$ {valor:.2f}"
        for x in list_extrato:
            if acesso["NUMERO"] in x["NUMERO"]:
                x["EXTRATO"].append(extrato)
        save(list_extrato, path_extrato)

        os.system("clear")
        print(f"Saque Realizado! \n{horario} -> R$ {valor:.2f}")
        if y == "pf":
            save(lista_pf, path_conta_pf)
            return
        elif y == "pj":
            save(lista_pj, path_conta_pj)
            return
    except ValueError:
        print("Valor inválido!")


def depositar(
    acesso,
    lista_pf,
    y,
    path_conta_pf,
    lista_pj,
    path_conta_pj,
    list_extrato,
    path_extrato,
    horario,
):
    os.system("clear")
    print("\n======== DEPÓSITO ========")
    print()
    valor = input("Valor do depósito: ")
    try:
        valor = float(valor)
        saldo = acesso["SALDO"] + valor
        acesso.update({"SALDO": saldo})
        extrato = f"{horario} -> Depósito: R$ {valor:.2f}"
        for x in list_extrato:
            if acesso["NUMERO"] in x["NUMERO"]:
                x["EXTRATO"].append(extrato)
        save(list_extrato, path_extrato)

        os.system("clear")
        print(f"Depósito Realizado! \n{horario} -> \tR$ {valor:.2f}")
        if y == "pf":
            save(lista_pf, path_conta_pf)
            return
        elif y == "pj":
            save(lista_pj, path_conta_pj)
            return
    except ValueError:
        print("Valor inválido!")


def consulta_extrato(list_extrato, acesso):
    os.system("clear")
    print("\n======== EXTRATO ========")
    print()
    try:
        for x in list_extrato:
            if acesso["NUMERO"] in x["NUMERO"]:
                for item in x["EXTRATO"]:
                    print(item)
    except KeyError:
        print("Vazio!")


def saldo(acesso):
    os.system("clear")
    print("\n======== CONSULTA SALDO ========\n")
    print(f"R$ {acesso['SALDO']:.2f}")


def consulta_cadastro(y, lista_pf, lista_pj, acesso):
    os.system("clear")
    print("\n======== DADOS CADASTRAIS ========\n")
    if y == "pf":
        for x in lista_pf:
            if acesso["CPF"] in x["CPF"]:
                for chave, valor in x.items():
                    print(f"{chave}: {valor}")
    elif y == "pj":
        for x in lista_pj:
            if acesso["CNPJ"] in x["CNPJ"]:
                for chave, valor in x.items():
                    print(f"{chave}: {valor}")


def read(list, path):  # Ler os dados a partir de um arquivo JSON
    dados = []
    try:
        with open(path, "r", encoding="utf8") as file:
            dados = json.load(file)
    except FileNotFoundError:
        print("Criado arquivo JSON!")
        save(list, path)
    return dados


def save(list, path):  # Salvar todos operações em um arquivo JSON
    register = list
    with open(path, "w", encoding="utf8") as file:
        register = json.dump(list, file, indent=2, ensure_ascii=False)
    return register


def sistema():
    # Caminho do arquivo JSON que possui todos os cadastros de pessoa física
    PATH_CADASTROS_PF = "./Projetos/sistema_bancario/cadastros_pf.json"
    # Caminho do arquivo JSON que possui todos os cadastros de pessoa jurídica
    PATH_CADASTROS_PJ = "./Projetos/sistema_bancario/cadastros_pj.json"
    # Caminho do arquivo JSON que possui todos as contas de pessoa física
    PATH_CONTAS_PF = "./Projetos/sistema_bancario/contas_pf.json"
    # Caminho do arquivo JSON que possui todos as contas de pessoa jurídica
    PATH_CONTAS_PJ = "./Projetos/sistema_bancario/contas_pj.json"
    # Caminho do arquivo JSON que armazena o último número de conta criado.
    PATH_NUMEROS = "./Projetos/sistema_bancario/numeros.json"
    # Caminho do arquivo JSON que armazena as operações feitas pelo usuário.
    PATH_EXTRATOS = "./Projetos/sistema_bancario/extratos.json"
    lista_cadastros_pf = read([], PATH_CADASTROS_PF)
    lista_cadastros_pj = read([], PATH_CADASTROS_PJ)
    lista_contas_pf = read([], PATH_CONTAS_PF)
    lista_contas_pj = read([], PATH_CONTAS_PJ)
    nro_conta = read((1), PATH_NUMEROS)
    listas_extratos = read([], PATH_EXTRATOS)
    format = "%d-%m-%Y %H:%M:%S"  # Define o formato da data
    horario_atual = datetime.now(timezone("UTC"))
    # Horário atual no fuso-horário do Brasil/São Paulo
    agora_brasil = horario_atual.astimezone(timezone("America/Sao_Paulo"))

    while True:
        option1 = Menu.inicial()

        if option1 == "1":  # Cadastrar
            os.system("clear")
            option2 = Menu.cadastro_cliente()

            if option2 == "1":  # Pessoa Física
                p = cadastro_pessoa_fisica(lista_cadastros_pf)
                if p == 0:
                    continue

                while True:
                    option3 = Menu.cadastro_conta_pf()
                    if option3 == "1":  # Conta Salário
                        cadastro_contas_pf(
                            p,
                            ContaPessoaFisica.conta_salario(nro_conta),
                            lista_cadastros_pf,
                            lista_contas_pf,
                            PATH_CADASTROS_PF,
                            PATH_CONTAS_PF,
                            listas_extratos,
                            PATH_EXTRATOS,
                        )
                        break

                    elif option3 == "2":  # Conta Corrente Padrão
                        cadastro_contas_pf(
                            p,
                            ContaPessoaFisica.conta_corrente_padrao(nro_conta),
                            lista_cadastros_pf,
                            lista_contas_pf,
                            PATH_CADASTROS_PF,
                            PATH_CONTAS_PF,
                            listas_extratos,
                            PATH_EXTRATOS,
                        )
                        break

                    elif option3 == "3":  # Conta Corrente Premium
                        cadastro_contas_pf(
                            p,
                            ContaPessoaFisica.conta_corrente_premium(nro_conta),
                            lista_cadastros_pf,
                            lista_contas_pf,
                            PATH_CADASTROS_PF,
                            PATH_CONTAS_PF,
                            listas_extratos,
                            PATH_EXTRATOS,
                        )
                        break

                    elif option3 == "4":  # Conta Poupança
                        cadastro_contas_pf(
                            p,
                            ContaPessoaFisica.conta_poupanca(nro_conta),
                            lista_cadastros_pf,
                            lista_contas_pf,
                            PATH_CADASTROS_PF,
                            PATH_CONTAS_PF,
                            listas_extratos,
                            PATH_EXTRATOS,
                        )
                        break

                    else:
                        print("Opção Inválida")

                os.system("clear")
                print("Conta Criada com Sucesso!\n")
                nro_conta = +1
                save(nro_conta, PATH_NUMEROS)

            if option2 == "2":  # Pessoa Jurídica
                p = cadastro_pessoa_juridica(lista_cadastros_pj)
                if p == 0:
                    continue

                while True:
                    option3 = Menu.cadastro_conta_pj()
                    if option3 == "1":  # Conta Jurídica Padrão
                        cadastro_contas_pj(
                            p,
                            ContaPessoaJuridica.conta_juridica_padrao(nro_conta),
                            lista_cadastros_pj,
                            lista_contas_pj,
                            PATH_CADASTROS_PJ,
                            PATH_CONTAS_PJ,
                            listas_extratos,
                            PATH_EXTRATOS,
                        )
                        break

                    elif option3 == "2":  # Conta Jurídica Premium
                        cadastro_contas_pj(
                            p,
                            ContaPessoaJuridica.conta_juridica_premium(nro_conta),
                            lista_cadastros_pj,
                            lista_contas_pj,
                            PATH_CADASTROS_PJ,
                            PATH_CONTAS_PJ,
                            listas_extratos,
                            PATH_EXTRATOS,
                        )
                        break

                    else:
                        print("Opção inválida!")

                os.system("cls")
                print("Conta Criada com Sucesso!\n")
                nro_conta = +1
                save(nro_conta, PATH_NUMEROS)

        # Tentar acessar alguma conta porém não há alguma conta cadastrada
        elif option1 == "2" and listas_extratos == []:
            os.system("cls")
            print("Nenhuma conta cadastrada!")

        elif option1 == "2":  # Acessar Conta
            os.system("clear")
            tentativa = 1
            while True:

                """x é a conta acessada e y será utilizado para diferenciar
                entre PF e PJ"""
                dados_acessado, y = acessar_conta(
                    tentativa, Menu.login(), lista_contas_pf, lista_contas_pj
                )

                """Toda tentativa incorreta irá retornar x == 0"""
                if dados_acessado != 0:
                    break

                else:
                    tentativa += 1

            operacao = "S"
            while operacao == "S":
                """Retira os dados de dentro do parentêses e transforma em
                dicionário. Mais simples de manipular"""
                for dados in dados_acessado:
                    conta_acesso = dados

                    option2 = Menu.operacoes()
                    if option2 == "1":  # Sacar
                        sacar(
                            conta_acesso,
                            lista_contas_pf,
                            y,
                            PATH_CONTAS_PF,
                            lista_contas_pj,
                            PATH_CONTAS_PJ,
                            listas_extratos,
                            PATH_EXTRATOS,
                            str(agora_brasil.strftime(format)),
                        )

                    elif option2 == "2":  # Depositar
                        depositar(
                            conta_acesso,
                            lista_contas_pf,
                            y,
                            PATH_CONTAS_PF,
                            lista_contas_pj,
                            PATH_CONTAS_PJ,
                            listas_extratos,
                            PATH_EXTRATOS,
                            str(agora_brasil.strftime(format)),
                        )

                    elif option2 == "3":  # Consultar Extrato
                        consulta_extrato(listas_extratos, conta_acesso)

                    elif option2 == "4":  # Consultar Saldo
                        saldo(conta_acesso)

                    elif option2 == "5":  # Consultar Dados Cadastrais
                        consulta_cadastro(
                            y, lista_cadastros_pf, lista_cadastros_pj,
                            conta_acesso
                        )

                    elif option2 == "6":  # Encerrar
                        print("Encerrando...")
                        operacao = "N"

                    else:
                        print("Opção inválida!")
            os.system("cls")
        elif option1 == "3":  # Limpa Tela
            os.system("cls")

        elif option1 == "4":  # Encerrar
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")


# Inicializador
if __name__ == "__main__":
    sistema()
