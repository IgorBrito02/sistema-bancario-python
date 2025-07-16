# Função para validar senha
def autenticar(senha_digitada, senha_correta):
    return senha_digitada == senha_correta


# Função para depósito
def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


# Função para saque
def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques


# Função para exibir extrato
def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


# Função para transferência entre contas (somente quem envia registra no extrato)
def transferir(saldo_origem, saldo_destino, valor, extrato_origem):
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
    elif valor > saldo_origem:
        print("Operação falhou! Você não tem saldo suficiente.")
    else:
        saldo_origem -= valor
        saldo_destino += valor
        extrato_origem.append(f"Transferência realizada: R$ {valor:.2f}")
        print("Transferência realizada com sucesso!")
    return saldo_origem, saldo_destino, extrato_origem


# Função principal
def main():
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3
    senha_correta = "1234"

    saldo2 = 1000
    extrato2 = []

    menu = """
    [d] Depositar
    [s] Sacar
    [t] Transferir
    [e] Extrato
    [q] Sair
    => """

    print("Bem-vindo ao sistema bancário!")
    senha_digitada = input("Digite sua senha para acessar: ")

    if not autenticar(senha_digitada, senha_correta):
        print("Senha incorreta! Encerrando...")
        return

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES
            )

        elif opcao == "t":
            valor = float(input("Informe o valor da transferência: "))
            saldo, saldo2, extrato = transferir(
                saldo, saldo2, valor, extrato
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "q":
            print("Obrigado por usar o sistema! Encerrando...")
            break

        else:
            print("Operação inválida, por favor selecione novamente.")


if __name__ == "__main__":
    main()