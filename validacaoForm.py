import re

def validar_nome(nome):
    return bool(re.fullmatch(r'[a-zA-Z ]{1,50}', nome))

def validar_cpf(cpf):
    return bool(re.fullmatch(r'\d{11}|\d{3}\.\d{3}\.\d{3}-\d{2}', cpf))

def validar_email(email):
    return bool(re.fullmatch(r'[a-zA-Z0-9._]{2,}@[a-zA-Z]{1,50}\.[a-z]{3}', email))

def validar_telefone(telefone):
    return bool(re.fullmatch(r'\d{11}|\(\d{2}\)\d{5}-\d{4}', telefone))

nome = input("Digite o nome: ")
cpf = input("Digite o CPF: ")
email = input("Digite o email: ")
telefone = input("Digite o telefone: ")

print("\nResultados da Validação:")
print("Nome válido?" , validar_nome(nome))
print("CPF válido?" , validar_cpf(cpf))
print("Email válido?" , validar_email(email))
print("Telefone válido?" , validar_telefone(telefone))

with open("texto.txt", "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()


padrao_email = r'[a-zA-Z0-9._]{2,}@[a-zA-Z]{1,50}\.[a-z]{3}'
emails_encontrados = re.findall(padrao_email, texto)

print("\nE-mails válidos extraídos do texto:")
for email in emails_encontrados:
    print("-", email)
