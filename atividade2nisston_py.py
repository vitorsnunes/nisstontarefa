# -*- coding: utf-8 -*-
"""atividade2nisston.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oDCn1HV_qsMPLY7Txh2iSCrEia1KUn7_

1. Crie uma classe chamada “Circulo” que tenha um atributo “raio”. Implemente um método chamado “calcular_area” que retorna a área do círculo.
"""

import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2

"""2. Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”. Implemente um método chamado “detalhes” que retorna uma string com as informações do livro."""

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}"

livro1 = Livro("Dom Casmurro", "Machado de Assis")

detalhes_livro1 = livro1.detalhes()
print(detalhes_livro1)

"""3. Crie uma classe chamada “Retangulo” que tenha atributos “base” e “altura”. Implemente um método chamado “calcular_area” que retorna a área do retângulo."""

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

"""4. Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”. Implemente métodos “depositar” e “sacar” para manipular o saldo."""

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de {valor} realizado com sucesso. Novo saldo: {self.saldo}")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de {valor} realizado com sucesso. Novo saldo: {self.saldo}")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

"""5. Crie uma classe chamada “Pessoa” com atributos “nome” e “idade”. Implemente um método chamado “falar” que imprime uma mensagem com o nome da pessoa."""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Olá, meu nome é {self.nome}.")

"""6. Crie uma classe chamada “Produto” com atributos “nome”, “preco” e “quantidade”. Implemente um método chamado “calcular_total” que retorna o valor total do produto (preço * quantidade)."""

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade

"""7. Crie uma classe chamada “Carro” com atributos “marca”, “modelo” e “ano”. Implemente um método chamado “detalhes” que retorna uma string com as informações do carro."""

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        return f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}"

"""8. Crie uma classe chamada “Aluno” com atributos “nome” e “notas”. Implemente um método chamado “calcular_media” que retorna a média das notas do aluno."""

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        else:
            return 0

"""9. Crie uma classe chamada “Triangulo” com atributos “lado1”, “lado2” e “lado3”. Implemente um método chamado “calcular_perimetro” que retorna o perímetro do triângulo."""

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

"""10. Crie uma classe chamada “Funcionario” com atributos “nome”, “salario” e “cargo”. Implemente um método chamado “aumentar_salario” que recebe um valor percentual de aumento e atualiza o salário do funcionário"""

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual):
        if percentual > 0:
            aumento = self.salario * (percentual / 100)
            self.salario += aumento
            print(f"O salário de {self.nome} foi aumentado para R${self.salario:.2f}")
        else:
            print("Percentual de aumento inválido.")