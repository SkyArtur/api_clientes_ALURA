import re
from validate_docbr import CPF


def validate_cpf(cpf):
    valid = CPF()
    return valid.validate(cpf)


def validate_nome(nome):
    n = nome
    if ''.join(n.split()).isalpha():
        return nome


def validate_rg(rg):
    if len(rg) == 9:
        return rg


def validate_celular(celular):
    modelo = '\\([0-9]{2}\\) ([0-9]{5})-([0-9]{4})'
    if re.findall(modelo, celular):
        return celular


def validate_email(email):
    if '@' in email:
        return email
