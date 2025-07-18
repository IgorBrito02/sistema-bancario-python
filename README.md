# 💰 Sistema Bancário em Python

Este projeto é um sistema bancário completo desenvolvido em Python, como parte do desafio proposto na Formação Python da DIO.  
Aqui você pode simular um sistema com múltiplos usuários, várias contas por CPF, autenticação, e operações bancárias como depósitos, saques, transferências e extrato.

---

## 🚀 Funcionalidades

- **👥 Cadastro de Usuários**
  - Registre novos clientes informando nome, data de nascimento, CPF (único) e endereço.

- **🏦 Criação de Contas Bancárias**
  - Um cliente pode ter várias contas associadas ao seu CPF.
  - Cada conta possui número, agência, e é vinculada a um usuário.

- **🔐 Autenticação**
  - O cliente deve informar CPF e senha para acessar suas contas.

- **💵 Depósito**
  - Permite adicionar valores positivos ao saldo da conta selecionada.
  - Registra a operação no extrato da conta.

- **🏧 Saque**
  - Verifica saldo disponível antes da operação.
  - Aplica limite de valor por saque (R$ 500) e número máximo de saques diários (3 por dia).
  - Registra a operação no extrato.

- **💸 Transferência**
  - Permite transferir saldo entre contas existentes.
  - Apenas o remetente registra a operação no extrato.

- **📄 Extrato**
  - Exibe todas as movimentações (depósitos, saques, transferências) e o saldo atual da conta.

- **🔁 Trocar Conta**
  - Possibilidade de trocar entre contas associadas ao mesmo CPF.

- **❌ Sair**
  - Encerra o programa com uma mensagem de agradecimento.

---

## ⚙️ Como executar

1️⃣ Clone o repositório:

git clone https://github.com/IgorBrito02/sistema-bancario-python.git

2️⃣ Acesse a pasta do projeto:

cd sistema-bancario-python

3️⃣ Execute o arquivo Python:

python sistema_bancario.py


💡 Objetivos do projeto
- Praticar lógica de programação e organização de sistemas com Python.
- Simular um sistema bancário completo com operações reais.
- Exercitar uso de listas, dicionários, autenticação e múltiplas entidades (usuário e conta).

💙 Créditos
Projeto criado como parte da formação em Python da Digital Innovation One (DIO).

📝 Licença
Este projeto está sob a licença MIT.
Sinta-se à vontade para usar, modificar e compartilhar!