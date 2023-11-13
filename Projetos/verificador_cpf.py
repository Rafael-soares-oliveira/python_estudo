"""VERIFICADOR DE CPF"""

def verif_cpf():
    import re
    while True:
        while True:
            cpf = input("CPF: ")
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
        
        