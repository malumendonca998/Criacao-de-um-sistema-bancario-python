menu = """
[c] Criar usuário
[cc] Criar conta corrente
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
agencia = "0001"
num_conta = 1

usuarios = []
contas_correntes = []

def encontrar_usuario(cpf,usuarios):
    for i in usuarios:
        if i["cpf"] == cpf:
            return i
    return None

while True:

    opcao = input(menu)
    
    if opcao == "c":
        nome = input("Insira seu nome:")
        data_de_nasc = int(input("Insira sua data de nasc:"))
        print("Insira seu cpf sem os caracteres. exp: 15478545896")
        cpf = int(input("Insira seu cpf:"))
        endereco = input("Insira seu endereço:")
        #verificar se o usuario ja existe
        if encontrar_usuario (cpf,usuarios):
            print("Erro! Já existe um usuário com esse CPF.")
        else:
            usuarios.append({"nome": nome, "data_de_nasc": data_de_nasc, "cpf" : cpf, "endereco": endereco})
            print("Usuário cadastrado com sucesso!")
            
    elif opcao == "cc":
        cpf = int(input("Insira o CPF para criar sua conta corrente:"))
        usuario = encontrar_usuario(cpf, usuarios)
        if usuario:
            conta = {"agencia": agencia, "num_conta": num_conta, "usuario": usuario}
            contas_correntes.append(conta)
            print(f"Conta corrente criada com sucesso! Agência: {agencia}, Conta: {num_conta}")
            num_conta += 1
        else:
       
            print("Erro! Nenhum usuário encontrado com esse CPF.")
            
    elif opcao == "d":

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
