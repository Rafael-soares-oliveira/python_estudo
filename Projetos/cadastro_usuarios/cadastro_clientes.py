# Library
import json
import os
from datetime import date
import re
import copy

class Client:
    def __init__(self,id_number):
        self.ID = id_number # All IDs are unique
        self.NAME = self.name()
        self.BIRTH = self.birth_date()
        self.CPF = self.cpf()
        self.PHONE = self.phone()

    def name(self):
        self.NAME = input('Name: ').upper()
        return self.NAME

    def birth_date(self):
        while True:
            try:
                x1 = int(input('DAY: '))
                x2 = int(input('MONTH: '))
                x3 = int(input('YEAR: '))
                x4 = date(x3,x2,x1) # Transform inputs in date format
                self.BIRTH = str(x4.day).zfill(2) + '-' + str(x4.month).zfill(2) + '-' + str(x4.year)
                return self.BIRTH
            except ValueError: # If any input does not match a valid data, restart the loop
                print('Invalid date!')

    def cpf(self):
        self.CPF = verif_cpf() # Restricions on verif_cpf() function
        return self.CPF
    
    def phone(self):
        while True:
            ddd = input('DDD: ')
            if len(ddd) != 2: # Max 2 digits
                print('INVALID DDD!')
            else:
                break
        while True:
            phone = input('PHONE: ')
            if len(phone) < 8 or len(phone) > 9: #  8 or 9 digits
                print('INVALID PHONE NUMBER!')
            else:
                break
        self.PHONE = str(ddd) + '-' + str(phone)
        return self.PHONE

def read(list,path): # Read a json file that constains all the registrations or deleted datas
    dados = []
    try:
        with open(path, 'r', encoding='utf8') as file:
            dados = json.load(file)
    except FileNotFoundError:
        print('Criado arquivo JSON!')
        save(list,path)
    return dados

def save(list,path): # Save the registrations or deleted data in a json file
    register = list
    with open(path, 'w', encoding='utf8') as file:
        register = json.dump(list, file,indent=2, ensure_ascii=False)
    return register

def list_register(list): # List the data
    print("\n===== LISTA CADASTROS =====\n")
    if not list == []:
        for registros in list:
            print("=================")
            for chave,valor in registros.items():
                print(chave,':',valor)
        print("=================")
        print()
    else:
        print('EMPTY LIST!')
            
# List of deleted data
def list_deleted(list):
    print("\n===== CADASTROS DELETADOS =====\n")
    if not list == []:
        for registros in list:
            print("=================")
            for chave,valor in registros.items():
                print(chave,':',valor)
        print("=================")
        print()
    else:
        print('EMPTY LIST!')

# Remove the registration of the given ID from the main list and store in a dictionary of deleted data
# Mandatory to inform reason for removal.
def delete(list,deleted,path_register,path_deleted):
    if list == []:
        return
    else:
        print("\n===== DELETE =====\n")
        while True:
            excluir = input('Número do cadastro para excluir: ')
            if excluir == 'CANCEL' or excluir == 'cancel':
                break
            elif excluir.isnumeric():
                excluir = excluir.zfill(4)
                if [i for i in list if i['ID'] == excluir] == []:
                    print('Cadastro não existe!')
                else:
                    reason = input('Reason to delete: ')
                    for registro in [i for i in list if i['ID'] == excluir]:
                        registro
                    list.remove(registro)
                    deletado = copy.deepcopy(registro)
                    deletado.update({"REASON":reason})
                    deleted.append(deletado)
                    save(list,path_register)
                    save(deleted,path_deleted)
                    return

# Function responsible for checking whether a CPF number is valid or not. 
# Calculates the last two digits. Consists of two parts
def verif_cpf():
    while True:
        while True:
            cpf = input("CPF WITHOUT DOT OR DASH: ")
            cpf_filtered = re.sub(r'[^0-9]','',cpf) # Filter for number only
            if len(cpf_filtered) == 11: # Only accepted if it has 11 digits
                break
            else:
                print("INVALID CPF!")
                continue

        """Part 1 - Calculation of the first digit
        Step 1: Multiplies each of the first 9 digits by a countdown starting at 10
        Ex:     -- 10 --- 9 -- 8 -- 7 -- 6 -- 5 -- 4 -- 3 -- 2
                --- 7 --- 4 -- 6 -- 8 -- 2 -- 4 -- 8 -- 9 -- 0 -> CPF
                -- 70 -- 36 - 48 - 56 - 12 - 20 - 32 - 27 -- 0
        Step 2: Sum all the results -> 70+36+48+56+12+20+32+27+0 = 301
        Step 3: Multiply the previous result by 10 -> 301 * 10 = 3010
        Step 4: Get the remainder from dividing the previous account by 11 -> 3010 % 11 = 7
        Step 5: If the previous result is greater than 9: result is equal to 0, otherwise is equal to step 4
        """       
        cpf_filtered_9digits = []
        step1_1 = []
        i1 = 0
        m1 = 10

        while i1 < 9 : # Only the first 9 digits
            cpf_filtered_9digits.append(cpf_filtered[i1])
            cpf_filtered_9digits[i1] = int(cpf_filtered_9digits[i1])
            step1_1.append(cpf_filtered_9digits[i1] * m1) # Step 1
            i1 += 1
            m1 -= 1

        step2_1 = sum(step1_1) # step 2
        step3_1 = step2_1 * 10 # step 3
        step4_1 = step3_1 % 11 # step 4
        # step5
        if step4_1 > 7: step5_1 = 0
        else: step5_1 = step4_1

        """Part 2 - Calculation of the second digit
        Step 1: Multiplies each of the first 9 digits plus the result of part 1 by a countdown starting at 11
        Ex: 746.824.890-70 (746824890) 
                -- 11 -- 10 -- 9 -- 8 -- 7 -- 6 -- 5 -- 4 -- 3 -- 2
                --- 7 --- 4 -- 6 -- 8 -- 2 -- 4 -- 8 -- 9 -- 0 -- 7 -> CPF
                -- 70 -- 36 - 48 - 56 - 12 - 20 - 32 - 27 -- 0 - 14
        Step 2: Sum all the results -> 70+36+48+56+12+20+32+27+0+14 = 363
        Step 3: Multiply the previous result by 10 -> 363 * 10 = 3630
        Step 4: Get the remainder from dividing the previous account by 11: -> 3630 % 11 = 0
        Step 5: If the previous result is greater than 9: result is equal to 0, otherwise is equal to step 4
        """
        cpf_verified = cpf_filtered_9digits
        cpf_verified.append(step5_1)
        step1_2 = []
        i2 = 0
        m2 = 11

        while i2 < 10 :
            cpf_verified[i2] = int(cpf_verified[i2]) # Assegura que os valores são int
            step1_2.append(cpf_verified[i2] * m2) # step 1
            i2 += 1
            m2 -= 1

        step2_2 = sum(step1_2) # step 2
        step3_2 = step2_2 * 10 # step 3
        step4_2 = step3_2 % 11 # step 4
        # step5
        if step4_2 > 7: step5_2 = 0
        else: step5_2 = step4_2
        cpf_verified.append(step5_2) # Adiciona o resultado do step 5

        cpf_test = ''
        for i in range(len(cpf_filtered)): # Junta todos os caracteres em uma única posíção, igual ao valor de entrada
            cpf_test += str(cpf_verified[i])
            i += 1

        if cpf_test == cpf_filtered: # Compara o cpf inserido com o resultado final do algoritmo
            return cpf_filtered
        else:
            print("CPF INVALID! CPF DOES NOT EXIST!")
            continue

def menu():
    print('\n====== CLIENT REGISTER ====== \n\
    \nCOMANDS: \n\
[1] REGISTER \n\
[2] CLIENTS LIST \n\
[3] DELETE ID \n\
[4] DELETED LIST \n\
[5] CLEAN TERMINAL \n\
[6] EXIT \n\
')
    return input('TYPE A COMAND: ')

def main():
    PATH_FILE_REGISTER = './Projetos/cadastro_usuarios/cadastro_usuarios.json' # Path of json file, registrations
    PATH_FILE_DELETED = './Projetos/cadastro_usuarios/deletados_usuarios.json' # Path of json file, deleted registrations2
    PATH_FILE_ID = './Projetos/cadastro_usuarios/numeros_id.json' # Path of json file, maximum id_number
    lista_cadastros = read([],PATH_FILE_REGISTER) # List of registrations
    deleted_list = read([],PATH_FILE_DELETED) # List of deleted registrations
    id_list = read((1),PATH_FILE_ID) # Number of maximum id. Start = 1
    
    while True:
        command = menu()
        
        if command == '1': # Register
            id_list = int(id_list)
            while True:
                os.system('clear')
                print("\n===== CADASTRAR =====\n")
                variavel = Client(str(id_list).zfill(4))
                confirm = input('CONFIRM: \nYES | NO | CANCEL: ').upper() # Ask for confirm
                if confirm == 'YES':
                    lista_cadastros.append(variavel.__dict__) # Store the registration in dict format
                    id_list += 1
                    break
                elif confirm == 'NO':
                    continue
                elif confirm == 'CANCEL':
                    break
                else:
                    print('INVALID!')

            save(id_list,PATH_FILE_ID)
            save(lista_cadastros,PATH_FILE_REGISTER)
        
        elif command == '2': # List
            os.system('clear')
            list_register(lista_cadastros)
            
        elif command == '3': # Delete
            os.system('clear')
            list_register(lista_cadastros)
            delete(lista_cadastros,deleted_list,PATH_FILE_REGISTER,PATH_FILE_DELETED)
            
        elif command == '4': # Deleted
            os.system('clear')
            list_deleted(deleted_list)
        
        elif command == '5': # Clear terminal
            os.system('clear')
            
        elif command == '6': # Exit
            print('EXITING...')
            break
        
        else: # Error
            print('INVALID COMMAND!')
        
if __name__ == '__main__':
    main()
