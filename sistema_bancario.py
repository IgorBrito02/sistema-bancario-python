import textwrap


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if any(usuario["cpf"] == cpf for usuario in usuarios):
        print("@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("=== Usuário criado com sucesso! ===")


def buscar_usuario_por_cpf(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do titular: ")
    usuario = buscar_usuario_por_cpf(cpf, usuarios)

    if not usuario:
        print("@@@ Usuário não encontrado! Crie um usuário primeiro. @@@")
        return

    conta = {
        "agencia": agencia,
        "numero": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "extrato": [],
        "numero_saques": 0
    }

    contas.append(conta)
    print("=== Conta criada com sucesso! ===")


def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    for conta in contas:
        linha = f"""
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 50)
        print(textwrap.dedent(linha))


def selecionar_conta(contas):
    if not contas:
        print("Nenhuma conta disponível.")
        return None

    numero = int(input("Número da conta: "))
    agencia = input("Agência: ")

    for conta in contas:
        if conta["numero"] == numero and conta["agencia"] == agencia:
            return conta

    print("Conta não encontrada.")
    return None


def depositar(conta, /):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"].append(f"Depósito: R$ {valor:.2f}")
        print("=== Depósito realizado com sucesso! ===")
    else:
        print("@@@ Operação falhou! Valor inválido. @@@")


def sacar(*, conta, limite, limite_saques):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > conta["saldo"]
    excedeu_limite = valor > limite
    excedeu_saques = conta["numero_saques"] >= limite_saques

    if excedeu_saldo:
        print("@@@ Operação falhou! Saldo insuficiente. @@@")
    elif excedeu_limite:
        print("@@@ Operação falhou! Valor excede o limite. @@@")
    elif excedeu_saques:
        print("@@@ Operação falhou! Limite de saques excedido. @@@")
    elif valor > 0:
        conta["saldo"] -= valor
        conta["extrato"].append(f"Saque: R$ {valor:.2f}")
        conta["numero_saques"] += 1
        print("=== Saque realizado com sucesso! ===")
    else:
        print("@@@ Operação falhou! Valor inválido. @@@")


def exibir_extrato(conta, /):
    print("\n================ EXTRATO ================")
    if not conta["extrato"]:
        print("Não foram realizadas movimentações.")
    else:
        for operacao in conta["extrato"]:
            print(operacao)
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    print("==========================================")


def menu():
    opcoes = """
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nu]\tNovo usuário
    [nc]\tNova conta
    [lc]\tListar contas
    [q]\tSair
    => """
    return input(textwrap.dedent(opcoes))


def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    LIMITE_SAQUE_VALOR = 500

    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            conta = selecionar_conta(contas)
            if conta:
                depositar(conta)

        elif opcao == "s":
            conta = selecionar_conta(contas)
            if conta:
                sacar(conta=conta, limite=LIMITE_SAQUE_VALOR, limite_saques=LIMITE_SAQUES)

        elif opcao == "e":
            conta = selecionar_conta(contas)
            if conta:
                exibir_extrato(conta)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(AGENCIA, numero_conta, usuarios, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Obrigado por usar o sistema bancário!")
            break

        else:
            print("Operação inválida. Tente novamente.")


if __name__ == "__main__":
    main()