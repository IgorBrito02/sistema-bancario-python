import textwrap
from datetime import datetime
from abc import ABC, abstractmethod


class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor > self._saldo:
            print("@@@ Saldo insuficiente. @@@")
            return False
        if valor <= 0:
            print("@@@ Valor inválido para saque. @@@")
            return False

        self._saldo -= valor
        print("=== Saque realizado com sucesso! ===")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("@@@ Valor inválido para depósito. @@@")
            return False

        self._saldo += valor
        print("=== Depósito realizado com sucesso! ===")
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        saques_realizados = len([t for t in self.historico.transacoes if t['tipo'] == 'Saque'])

        if valor > self._limite:
            print("@@@ Valor excede o limite de saque. @@@")
        elif saques_realizados >= self._limite_saques:
            print("@@@ Limite de saques diários atingido. @@@")
        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""
        Agência:	{self.agencia}
        C/C:		{self.numero}
        Titular:	{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)


# Funções de menu e execução

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

def criar_cliente(clientes):
    cpf = input("CPF: ")
    if any(c.cpf == cpf for c in clientes):
        print("@@@ CPF já cadastrado. @@@")
        return

    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento: ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/UF): ")

    cliente = Cliente(nome, cpf, nascimento, endereco)
    clientes.append(cliente)
    print("=== Cliente criado com sucesso! ===")

def criar_conta(numero, clientes, contas):
    cpf = input("CPF do cliente: ")
    cliente = next((c for c in clientes if c.cpf == cpf), None)

    if not cliente:
        print("@@@ Cliente não encontrado. @@@")
        return

    conta = ContaCorrente(numero, cliente)
    cliente.adicionar_conta(conta)
    contas.append(conta)
    print("=== Conta criada com sucesso! ===")

def selecionar_conta_por_cpf(clientes):
    cpf = input("Informe o CPF: ")
    cliente = next((c for c in clientes if c.cpf == cpf), None)

    if not cliente or not cliente.contas:
        print("@@@ Conta não encontrada. @@@")
        return None

    return cliente.contas[0]  # assumindo que só há uma conta por cliente

def depositar(clientes):
    conta = selecionar_conta_por_cpf(clientes)
    if not conta:
        return
    valor = float(input("Valor do depósito: "))
    transacao = Deposito(valor)
    conta.cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    conta = selecionar_conta_por_cpf(clientes)
    if not conta:
        return
    valor = float(input("Valor do saque: "))
    transacao = Saque(valor)
    conta.cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    conta = selecionar_conta_por_cpf(clientes)
    if not conta:
        return
    print("\n================ EXTRATO ================")
    for t in conta.historico.transacoes:
        print(f"{t['tipo']}: R$ {t['valor']:.2f} em {t['data']}")
    print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
    print("==========================================")

def listar_contas(contas):
    for conta in contas:
        print("=" * 50)
        print(conta)

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            print("Obrigado por usar o sistema bancário!")
            break
        else:
            print("@@@ Opção inválida. Tente novamente. @@@")


if __name__ == "__main__":
    main()