menu = """

[d] Depositar
[e] Extrato
[s] Sacar
[f] Sair

=> """

saldo = 0
limite = 500
extrato = ""
num_saques = 0
LIM_SAQUE = 3

while True:

    opcao = input(menu)
    if opcao == "d":

        valor = float(input("digite um valor:"))

        if valor > 0:

            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falou! O valor informado é inválido!")

    elif opcao == "s":
        valor = float(input("digite um valor:"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = num_saques >= LIM_SAQUE

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente!")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite!")

        elif excedeu_saques:
            print("Operação falhou! Número de saques excedido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            num_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido!")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "f":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
