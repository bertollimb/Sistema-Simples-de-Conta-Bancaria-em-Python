# Sistema Simples de Conta Bancaria em Python

 Este projeto apresenta uma implementação simples de uma **classe ContaBancaria em Python**, utilizando conceitos fundamentais de Programação Orientada a Objetos (POO), como:

- Encapsulamento

- Atributos privados

- Propriedades (@property)

- Métodos de negócio (depositar, sacar)

**O objetivo é simular operações básicas de uma conta bancária.**

---

## **📌 Funcionalidades**

A classe ContaBancaria implementa:

✔️ Atributos privados

- `__titular` — nome do titular

- `__saldo` — saldo da conta

- `__limite` — limite máximo permitido para saque

✔️ Métodos disponíveis

- `depositar(valor)` — adiciona saldo à conta

- `sacar(valor)` — realiza saque respeitando o saldo e o limite

- `mostrar_info()` — exibe o titular e o saldo atual

- `Propriedade saldo` — permite ler e modificar o saldo apenas de forma controlada

---

## **🧠 Conceitos de POO Utilizados**

- Encapsulamento: uso de atributos privados (__atributo)

- Getters e Setters com @property: controle seguro sobre leitura e mudança de valores

- Lógica aplicada: verificação de limite e saldo antes do saque

---

## **🚀 Objetivo do Projeto**

- Este código foi criado como parte dos estudos de POO em Python, servindo de base para projetos mais avançados como:

- Simuladores bancários

- APIs financeiras com Flask ou FastAPI

- Sistemas de contas e transações

