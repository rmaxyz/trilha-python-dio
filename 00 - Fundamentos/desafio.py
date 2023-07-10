saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

menu = """
************************Menu********************************
                     [d] Deposito
                     [s] Sacar
                     [e] Extrato
                     [q] Sair
************************************************************
"""

while True:
    
    print(menu)
    opcao = input("Escolha uma opção: ")

    if opcao == 'd':
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R {valor_deposito:.2f}\n"
            
        else:
            print("Valor inválido!")

    elif opcao == 's':
                
        limite_saque = numero_saques < LIMITE_SAQUES
                
        if limite_saque:
            
            valor_saque = float(input("Digite o valor a ser sacado: "))
                                
            if saldo >= valor_saque <= limite:
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                numero_saques += 1
            else:
                print("Saldo insuficiente ou valor de saque inválido!")
        else:
            print("Limite máximo de saques diários atingido!")

    elif opcao == 'e':
        if extrato:
            print(f"Extrato:\n{extrato}Saldo atual: R {saldo:.2f}")
        else:
            print("Não foram realizadas movimentações no extrato.")

    elif opcao == 'q':
        break

    else:
        print("Opção inválida!")

print("Sistema encerrado.")
