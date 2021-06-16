import math

# Q01 Faça um Programa que peça dois números e imprima o maior deles.
"""
num1 = int(input("digite um primeiro numero: "))
num2 = int(input("digite um secundo numero: "))
if (num1 > num2):
    print("o primeiro numero e o maior")
elif (num2 > num1):
    print("o  segundo numero e o maior")
else:
    print("os numeros sao iguais")
    """

# Q02 Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""
num = int(input("digite um numero: "))
if (num >0 ):
    print("o numero e positivo!")
elif (num < 0 ):
    print("o numero e negativo")
else:
    print("o numero e 0")
    """

# Q03 Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino,
# M - Masculino, Sexo Inválido.
"""
letra= input("digite uma letra F ou M: ")
letra =letra.strip()
letra =letra.upper()
if (letra == "F"):
    print("sexo feminino")
elif (letra == "M"):
    print("sexo masculino")
else: print("letra invalida ")
"""

# Q04 Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
letra = str(input("digite uma letra: "))
if (letra == "a" or letra == "e" or letra =="i"or letra =="o" or letra =="u"):
    print("e uma vogal!")

else:
    print("e uma consoante!")
    """

# Q05 Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada
# por aluno e apresentar: A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""
notaUm = float(input("digita a primeira nota: "))
notaDois = float(input("digite a segunda nota: "))
media = (notaUm+notaDois)/2

if (media >= 7 and media <10):
    print("aprovado! :)")
elif (media < 7):
    print("reprovado! :(")
elif (media == 10):
    print("aprovado com distincao! XD")
"""

# Q06 faça um Programa que leia três números e mostre o maior deles.
"""
num1 = int(input("digite um numero: "))
num2 = int(input("digite outro numero: "))
num3 = int(input("digite mais um numero: "))
if (num1 > num2 and num1 > num3):
    print(f"o primeiro numero ({num1}) e o maior dos tres!")
elif (num2 > num1 and num2 > num3):
    print(f"o segundo numero ({num2}) e o maior dos tres!")
elif (num3 > num1 and num3 > num2):
    print(f"o terceiro numero ({num3}) e o maior dos tres!")
elif (num1 == num2 and num1 == num3):
    print("todos os numeros sao iguais !")
"""

# Q07 Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
num1 = int(input("digite um numero: "))
num2 = int(input("digite outro numero: "))
num3 = int(input("digite mais um numero: "))
if (num1 < num2 and num1 < num3):
    print(f"o primeiro numero ({num1}) e o menor dos tres!")
elif (num2 < num1 and num2 < num3):
    print(f"o segundo numero ({num2}) e o menor dos tres!")
elif (num3 < num1 and num3 < num2):
    print(f"o terceiro numero ({num3}) e o menor dos tres!")
elif (num1 == num2 and num1 == num3):
    print("todos os numeros sao iguais !")
"""

# Q08 Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a
# decisão é sempre pelo mais barato.
"""
num1 = int(input("digite um numero: "))
num2 = int(input("digite outro numero: "))
num3 = int(input("digite mais um numero: "))
if (num1 < num2 and num1 < num3):
    print(f"voce deve comprar o primeiro produto ({num1})R$!")
elif (num2 < num1 and num2 < num3):
    print(f"voce deve comprar o primeiro o segundo ({num2})R$!")
elif (num3 < num1 and num3 < num2):
    print(f"voce deve comprar o primeiro o terceiro({num3})R$!")
elif (num1 == num2 and num1 == num3):
    print("todos os precos sao iguais !")
"""

# Q09 Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
num1 = int(input("digite um nuemero: "))
num2 = int(input("digite outro numero: "))
num3 = int(input("digite mais um numero: "))

if num2 < num1 > num2 > num3:
    print(f"ordem decrescente: {num1}, {num2}, {num3}")
elif num3 < num1 > num3 > num2:
    print(f'ordem decrescente: {num1}, {num3}, {num2}')
elif num1 < num2 > num1 > num3:
    print(f"ordem decrescente: {num2}, {num1}, {num3}")
elif num3 < num2 > num3 > num1:
    print(f"ordem decrescente: {num2}, {num3}, {num1}")
elif  num2 < num3 > num2 > num1:
    print(f"ordem decrescente: {num3}, {num2}, {num1}")
elif num1 < num3 > num1 > num2:
    print(f"ordem decrescente: {num3}, {num1}, {num2}")
"""

# Q10 Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou
# N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""
turno = input("digite uma letra para um turno\n M - matutino V - vespertino ou N - noturno: ")
turno = turno.strip()
turno = turno.upper()
print("Bom Dia!") if turno == "M" else ()
print("Boa Tarde!") if turno == "V" else ()
print("Boa Noite!") if turno == "N" else ()
print("opcao invalida!") if turno != "M" and turno != "N" and turno != "V" else ()
"""

# Q11 As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
# desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o
# reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.
"""
salario = float(input("digite o seu salario: "))
if salario <= 280:
    salario = salario * 1.2
elif 280 < salario >= 700:
    salario = salario * 1.15
elif 700 < salario >= 1500:
    salario = salario * 1.10
elif salario > 1500:
    salario = salario * 1.05

print(f"o seu novo salario e de: {salario:.2f} R$")
"""

# Q12 Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
# depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
# Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
# descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20%
# Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
"""
valorHora = float(input("digite o valor da hora trabalhada: "))
horasTrab = float(input("digite quantas horas voce trabalha por mes: "))
sal = valorHora * horasTrab

if sal <= 900:
    totalDes = 0
    ir = 0
elif sal <= 1500:
    totalDes = (sal * 0.05) + (sal * 0.1)
    ir = 5
    tx = 0.05
elif sal <= 2500:
    totalDes = (sal * 0.1) + (sal * 0.1)
    ir = 10
    tx = 0.1
if sal > 2500:
    totalDes = (sal * 0.2) + (sal * 0.1)
    ir = 20
    tx = 0.2

print(f"Salário Bruto:({valorHora:.0f}*{horasTrab:.0f})      : R$ {sal:.2f}\n(-) IR ({ir}%)             : R$ {sal*tx:.2f}\n(-) INSS (10%)"
      f"        : R$ {sal*0.1:.2f}\nFGTS (11%)             : R$ {sal*0.11:.2f}\nTotal de descontos      : R$ {totalDes:.2f}\n"
      f"Salario Liquido        : R$ {sal-totalDes}")
"""

# Q13 Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido.

# using a dictionary mapping to return value
"""
op = int(input(
    "1 - domingo\n2 - segunda\n3 - terca\n4 - quarta\n5 - quinta\n6 - sexta\n7 - Sabado\nDigite um dia da semana: "))
dia = {1: "domingo",
       2: "segunda",
       3: "terca ",
       4: "quarta",
       5: "quinta",
       6: "sexta",
       7: "sabado"

       }
if op <= 7 and op >= 1:
    print("o dia da semana selecionado e: " , dia.get(op, -1))
else:
    print("numero invalido")
"""

# Q14 Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e
# calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito
# for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
media = (nota1 + nota2) / 2
conceito = str()

if 9 < media <= 10:
    conceito = "A"
elif 7.5 < media <= 9:
    conceito = "B"
elif 6 < media <= 7.5:
    conceito = "C"
elif 4 < media <= 6:
    conceito = "D"
elif 0 <= media <= 4:
    conceito = "E"

apro = {
    "A": "APROVADO",
    "B": "APROVADO",
    "C": "APROVADO",
    "D": "REPROVADO",
    "E": "REPROVADO"
}
print(f"Sua Media {media:.2f}\nConceito: {conceito}\nSituacao: {apro.get(conceito,)}")
"""

# Q15 Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser
# um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados differentes;
"""
lado1 = float(input("digite o primeiro lado: "))
lado2 = float(input("o segundo: "))
lado3 = float(input("o terceiro: "))
if lado1 == lado2 == lado3:
       print("Triângulo Equilátero")
elif lado2 == lado1 or lado2 == lado3 or lado1 == lado3:
       print("Triângulo Isósceles")
else:
       print("Triângulo Escaleno")
"""

# Q16 Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá
# pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os
# demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""
a = float(input("digite o valor de a: "))
cont = a
while cont != 0:
    b = float(input("digite o valor de b: "))
    c = float(input("digite o valor de c: "))
    delta = (b**2) - (4 * a * c)
    if delta < 0:
        print("essa equacao nao possui raizes!")
        cont = 0

    elif delta == 0:
        x = -b / (2*a)
        print(f"essa equacao so possui uma raiz real de: {x}")
        cont = 0

    elif delta > 0:
        delta = math.sqrt(delta)
        x = (-b + delta) / (2 * a)
        print(f"o valor da equacao e de: {x}")
        x = (-b - delta) / (2 * a)
        print(f"o segundo valor da equacao e de: {x}")
        cont = 0
if a == 0:
    print("essa equacao nao e de segundo grau!")
"""

# Q17 Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou
# não bissexto.
"""anobi = int(input("digite um ano: "))
print("esse ano e bissexto!") if ano % 4 == 0 else print("esse ano nao e bissexto")
"""

# Q18 Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""
data = input("digite sua data de nascimento (dd/mm/aaa): ")
data = data.strip()
dia = int(data[:2])
mes = (data[3:5])
ano = int(data[6:])
# 12 3 45 6 7891
if mes == "04" or mes == "06" or mes == "07" or mes == "09":
    print("essa data e valida") if 1 <= dia <= 30 else print("essa data e invalida!")
elif mes == "01" or mes == "03" or mes == "05" or mes == "07" or mes == "08" or mes == "12":
    print("essa data e valida") if 1 <= dia <= 31 else print("esse data e invalida!")
elif mes == "02":
    if ano % 4 == 0:
        print("essa data e valida") if 1 <= dia <= 29 else print("essa data e invalida!")
    else:
        print("essa data e valida") if 1 <= dia <= 28 else print("essa data e invalida!")
else:
    print("essa data e invalida")
    """

# #Q19 Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
# dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros.
# Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

"""
#1

num = input("digite um numero inteiro menor 1000: ")
#2
mensagem = str()

#3
compa = num
num = int(num)
#4
if 1 <= num <= 999:
    num = str(num)

    #5
    if len(compa) == 1:
        cen = 0
        dez = 0
        un = int(compa[:1])
    elif len(compa) == 2:
        cen = 0
        dez = int(compa[:1])
        un = int(compa[1:])
    elif len(compa) == 3:
        cen = int(compa[:1])
        dez = int(compa[1:2])
        un = int(compa[2:])
    print(f"{num} e composto por: ")
#6
    if cen > 1:
        mensagem = f" {cen} centenas "
    elif cen == 0:
        mensagem = f""
    else:
        mensagem = f"{cen} centena "

    if dez > 1:
        mensagem = mensagem + f"{dez} dezenas "
    elif dez == 0:
        mensagem = mensagem + f""
    else:
        mensagem = mensagem + f"{dez} dezena "

    if un > 1:
        mensagem = mensagem + f"{un} unidades "
    elif un == 0:
        mensagem = mensagem + f""
    else:
        mensagem = mensagem + f"{un} unidade "

    print(mensagem)
else:
    print("numero invalido!")

 1. recebemos o numero 2. criamos uma string vazia para armazenar a mudaca da frase
 3. criamos uma var para ser usado como base para o slice, e mudamos o tipo do num
 4. verificamos se o num esta no range > 1 e <1000 5. verificamos quantos carc o num tem e cortamos de acordo
 6. vamos mudar a frase de acordo com o tanto de unidades dezenas e centenas 
 
 """

# Q21 Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois
# informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
# O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas
# existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50,
# uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
# uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

"""
valor = int(input("digite o valor so saque: "))
nota100, nota1, nota5, nota10, nota50 = int,int,int,int,int

nota100 = valor // 100
valor = valor - (nota100 * 100)
if valor % 100 != 0:
    nota50 = valor // 50
    valor = valor - (nota50 * 50)
    if valor % 50 != 0:
        nota10 = valor // 10
        valor = valor - (nota10 * 10)
        if valor % 10 != 0:
            nota5 = valor // 5
            valor = valor - (nota5 * 5)
            if valor % 5 !=0:
                nota1 = valor // 1
                valor = valor - (nota1 * 1)

print(f"notas \n{nota100} notas de R$ 100\n{nota50} notas de R$ 50\n{nota10} notas de R$ 10\n{nota5} "
      f"notas de R$ 5\n{nota1} notas de R$ 1")

"""

# Q22 Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão).
"""
num = int(input("digite um numero: "))
print("numero par") if  num % 2 == 0 else print("numero impar")
"""

# Q23 Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
# Dica: utilize uma função de arredondamento.
"""
num = float(input("digite um numero: "))
print("numero inteiro") if num == round(num) else print("numero decimal")
"""

# Q24 Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

"""
num = int(input("digite um numero: "))
num2 = int(input("digite outro numero: "))
op = int(input("qual operacao deseja fazer? \n 1 - adicao\n 2 - subtracao\n 3 - multiplicacao\n 4 - divisao\n "))

if op == 1:
    num = num + num2
if op == 2 :
    num = num - num2
if op == 3 :
    num = num * num2
if op == 4 :
    num = num / num2
frase = str

if num % 2 == 0:
    frase = f" o {num} = numero par,"
else:
    frase = f" o {num} = numero impar,"

if num == round(num):
    frase = frase + f" numero inteiro,"
else:
    frase = frase + " numero decimal,"
if num > 0:
     frase = frase + " numero positivo"
else:
    frase = frase + ' numero negativo'

print(frase)

"""

# Q25 Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no 
# crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como 
# "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
pergunta1 = input("voce telefonou para vitima? ")
pergunta1 = pergunta1.strip().lower()
num = 0
pergunta2 = input("voce esteve no local do crime? ")
pergunta2 = pergunta2.strip().lower()
pergunta3 = input("voce mora perto da vitima? ")
pergunta3 = pergunta3.strip().lower()
pergunta4 = input("voce devia para vitima? ")
pergunta4 = pergunta4.strip().lower()
pergunta5 = input("voce ja trabalhou para vitima? ")
pergunta5 = pergunta5.strip().lower()


if pergunta1 == "sim":
    num = num +1
if pergunta2 == "sim":
    num = num +1
if pergunta3 == "sim":
    num = num +1
if pergunta4 == "sim":
    num = num +1
if pergunta5 == "sim":
    num = num +1


if num == 5:
    print("assasino")
elif num == 2:
    print("suspeito")
elif num == 3 or num == 4:
    print("cumplice")
else:
    print("inocente")
"""

# Q26 Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de
# combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
# sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""
litros = float(input("digite o valor dos litros vendidos: "))
tipo = input("digite o tipo: \n G - gasolina\n A - alcool\n")
tipo = tipo.strip().upper()
valortotal = ()

if tipo == "A":
    valortotal = litros * (1.90)
    if litros <= 20: 
        valortotal = valortotal - (valortotal*0.04)
    if litros > 20:
        valortotal = valortotal - (valortotal * 0.06)
elif tipo == "G":
    valortotal = litros * (2.50)
    if litros <= 20:
        valortotal = valortotal - (valortotal * 0.03)
    elif litros > 20 :
        valortotal = valortotal - (valortotal * 0.05)
    
print(f"valot total a pagar: R${valortotal}")

"""

# Q27 Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos
# e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""
fruta = input("digite a fruta: \n MA - maca\n MO - morango\n ")
peso = float(input("digite o peso: "))
fruta = fruta.strip().upper()
valor = ()
if fruta == "MA":
    if peso <= 5:
        valor = peso * 1.8
    elif 5 < peso < 8:
        valor = peso * 1.5
    elif peso >= 8:
        valor = peso * 1.50
        valor = valor - (valor*0.1)
if fruta == "MO":
    if peso <= 5:
        valor = peso * 2.5
    elif 5 < peso < 8:
        valor = peso * 2.2
    elif peso >= 8:
        valor = peso * 1.50
        valor = valor - (valor*0.1)

print(f"o valor total e de R$ {valor:.2f}")
"""



