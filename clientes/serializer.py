from rest_framework import serializers
from clientes.models import Cliente
from clientes.validator import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not validate_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf': 'CPF inválido.'})
        if not validate_rg(data['rg']):
            raise serializers.ValidationError({'rg': 'O RG deve ter 9 digitos.'})
        if not validate_nome(data['nome']):
            raise serializers.ValidationError({'nome': 'Não inclua números.'})
        if not validate_email(data['email']):
            raise serializers.ValidationError({'email': 'Os dados inserido não é um email válido.'})
        if not validate_celular(data['celular']):
            raise serializers.ValidationError({'celular': 'O campo deve conter 11 digitos ou mais.'})
        return data
