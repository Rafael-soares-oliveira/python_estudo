'''
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra.
    - Se a letra digitada não estiver na palavra secreta; exiba *.
- Faça a contagem de tentativas do seu usuário.
'''

letras_corretas = []
palavra_secreta = input(f"""## Jogo da Forca ##\n\nDigite a palavra secreta: """)
letras_incorretas = []
tentativa = 0

while True:
    letra = input("Digite a letra: ")
    
    if len(letra) == 1:
        if letra in palavra_secreta:
            
            if letra in letras_corretas:
                print("Letra correta, porém já usada!")
            else:
                letras_corretas += letra
                
        else:
            if letra in letras_incorretas:
                print("Letra incorreta e já escolhida!")
            else:
                letras_incorretas += letra
                tentativa += 1
            print(f"Letra incorreta - Tentativa - {tentativa}/3")
        
        if tentativa == 3:
            print("Fim de Jogo!")
            break
        
        palavra_formada = ''
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_corretas:
                palavra_formada += letra_secreta
                
            else:
                palavra_formada += '*'
        
        print(palavra_formada)
                
        if palavra_formada == palavra_secreta:
            print("Parabéns! A palavra era:", palavra_secreta)
            break
    else:
        print("Digite apenas uma letra!")