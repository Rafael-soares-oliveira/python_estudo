# Programa gerador de CPF válido

def func_gerador_cpf():
    
    from faker import Faker
    import re

    gerador = Faker('pt_BR',use_weighting=True)
    validadores = [11,10,9,8,7,6,5,4,3,2,1]
    
    while True:
        cpf = gerador.bothify('###########')
        cpf_teste = ([q for q in cpf])
        cpf_filtered_test = cpf_teste[:9]
        
        step1_1 = [int(x)*int(y) for x,y in zip(cpf_filtered_test,validadores[1:])]
        step2_1 = sum(step1_1)
        step3_1 = step2_1 * 10
        step4_1 = step3_1 % 11
        if step4_1 > 7: step5_1 = 0
        else: step5_1 = step4_1

        cpf_filtered_test
        cpf_filtered_test.append(str(step5_1))

        step1_2 = [int(x)*int(y) for x,y in zip(cpf_filtered_test,validadores)]
        step2_2 = sum(step1_2)
        step3_2 = step2_2 * 10
        step4_2 = step3_2 % 11
        if step4_2 > 7: step5_2 = 0
        else: step5_2 = step4_2
        cpf_filtered_test.append(str(step5_2))

        if cpf_filtered_test == cpf_teste:
            return cpf
        else:
            continue