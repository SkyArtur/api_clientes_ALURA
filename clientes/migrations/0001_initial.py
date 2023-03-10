# Generated by Django 4.1.7 on 2023-03-02 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('email', models.EmailField(blank=True, max_length=30)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('rg', models.CharField(max_length=9, unique=True)),
                ('celular', models.CharField(max_length=14)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
    ]
