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

def verif_cnpj():
    import re
    validadores = [5,4,3,2,9,8,7,6,5,4,3,2]

    while True:
        cnpj = input('CNPJ: ')
        cnpj_filtrado = re.sub(r'[^0-9]','',cnpj)
        
        if len(cnpj_filtrado) != 14:
            print('CNPJ Inválido!')
            continue
        else:
            break
        
    cnpj_list = [x for x in cnpj_filtrado[:12]]
    
    cnpj_passo1_1 = [int(x)*int(y) for x,y in zip(cnpj[:12],validadores)]
    cnpj_passo2_1 = sum(cnpj_passo1_1)
    cnpj_passo3_1 = cnpj_passo2_1%11
    cnpj_passo4_1 = 0 if cnpj_passo3_1 < 2 else 11-cnpj_passo3_1

    cnpj_list.append(str(cnpj_passo4_1))
    validadores.insert(0,6)

    cnpj_passo1_2 = [int(x)*int(y) for x,y in zip(cnpj_list[:13],validadores)]
    cnpj_passo2_2 = sum(cnpj_passo1_2)
    cnpj_passo3_2 = cnpj_passo2_2%11
    cnpj_passo4_2 = 0 if cnpj_passo3_2 < 2 else 11-cnpj_passo3_2
    cnpj_list.append(str(cnpj_passo4_2))

    return cnpj_filtrado if [x for x in cnpj_filtrado] == cnpj_list else print('CNPJ Inválido!')