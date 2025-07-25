# 💰 Sistema Bancário em Python (com POO)

Este projeto é um sistema bancário simples desenvolvido em Python, utilizando os princípios da **Programação Orientada a Objetos (POO)**.  
Ele foi criado como parte do desafio da Formação Python da Digital Innovation One (DIO).

A aplicação simula um sistema bancário básico, com funcionalidades de cadastro de clientes, criação de contas, depósitos, saques e emissão de extratos.

---

## 🚀 Funcionalidades

- **👥 Cadastro de Clientes**
  - Nome completo, CPF (único), data de nascimento e endereço.
  - Verificação de duplicidade de CPF.

- **🏦 Criação de Contas Correntes**
  - Vinculadas a um cliente já existente.
  - Cada conta possui número, agência fixa (0001), saldo e histórico de transações.

- **💵 Depósito**
  - Adiciona saldo à conta.
  - Valor deve ser positivo.
  - Registra a transação no histórico.

- **🏧 Saque**
  - Permite saque se o saldo for suficiente.
  - Limite por saque: R$ 500,00.
  - Máximo de 3 saques diários por conta.
  - Transação registrada no histórico.

- **📄 Extrato**
  - Lista todas as transações (saques e depósitos) da conta.
  - Exibe saldo atual.

- **📋 Listar Contas**
  - Mostra todas as contas criadas com seus dados principais.

- **❌ Sair**
  - Encerra o programa com uma mensagem de agradecimento.

---

## 💡 Tecnologias e Conceitos Utilizados

- Python 3
- Programação Orientada a Objetos (POO)
  - Encapsulamento
  - Herança
  - Polimorfismo
  - Classes Abstratas
- Listas e buscas com `next()` e `filter`
- Estrutura de menus interativos com `input()` e `print()`

---

## ⚙️ Como executar

1️⃣ Clone o repositório:

git clone https://github.com/IgorBrito02/sistema-bancario-python.git

2️⃣ Acesse a pasta do projeto:

cd sistema-bancario-python

3️⃣ Execute o arquivo Python:

python sistema_bancario.py


💡 Objetivos do projeto
- Praticar a estruturação de código com POO.
- Aplicar abstração e modularização para facilitar a manutenção.
- Simular operações bancárias reais com lógica de negócio implementada.

💙 Créditos
Projeto criado como parte da formação em Python da Digital Innovation One (DIO).

📝 Licença
Este projeto está sob a licença MIT.
Sinta-se à vontade para usar, modificar e compartilhar!