# Validador de Formulário com Expressões Regulares

Este projeto tem como objetivo implementar, utilizando a linguagem de programação Python, uma aplicação para **validar o preenchimento de um formulário de usuário** e realizar a **extração de e-mails válidos** a partir de um texto fornecido. A solução utiliza a biblioteca nativa de expressões regulares do Python: `re`.

## Objetivo

Validar computacionalmente os seguintes campos de um formulário utilizando **expressões regulares (regex)**:

- **Nome**: até 50 caracteres alfabéticos (maiúsculos, minúsculos e espaços).
- **CPF**: deve conter apenas números ou estar no formato `000.000.000-00`.
- **E-mail**: deve seguir a estrutura `usuario@dominio.tipo`, onde:
  - O nome de usuário contém pelo menos 2 símbolos alfanuméricos, pontos ou underline;
  - O domínio segue o mesmo padrão do usuário;
  - O tipo de domínio (TLD) contém exatamente 3 letras minúsculas.
- **Telefone**: dois formatos válidos:
  - Apenas números, com 11 dígitos (`11999998888`);
  - Formato com parênteses e hífen (`(11)99999-8888`).

Além disso, a aplicação varre um texto e **extrai somente os e-mails válidos**.

## Tecnologias e Bibliotecas

- **Python 3**
- Biblioteca padrão `re` (expressões regulares)

## Funcionalidades

- Validação individual de cada campo do formulário.
- Extração de e-mails válidos a partir de um bloco de texto.
- Rejeição de entradas inválidas com mensagens apropriadas.

## Exemplo de Texto para Extração de E-mails

```text
Prezado usuário,

Aqui estão os contatos do nosso time de suporte:

- alice.souza@gmail.com  
- suporte_23@empresa-tech.com  
- joao99@dominio123.org  
- erro.email@gmail..com

Por favor, envie suas dúvidas para qualquer um dos e-mails válidos acima.

Atenciosamente,  
Equipe de Atendimento
