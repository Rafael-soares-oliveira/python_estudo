Projetos de Sitema Bancário

- Cada parte do projeto é um sistema bancário único mais complexo que o anterior
- Parte 3 seria o mais complexo

Sistema Bancário Parte 3
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
    - Impor limites para cada tipo de conta -> acrescentar limitações dentro da classe Conta
    - Opção de remover contas e armazená-las em outro arquivo JSON
    - Opção de alterar modelo da conta e dados dos usuários e password dentro da Operação Acessar Conta