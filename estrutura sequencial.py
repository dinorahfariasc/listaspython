# exercicios de estrutura sequencial
# Q01 Faça um Programa que mostre a mensagem "Alo mundo" na tela. -

"""
print("Alo mundo")
"""
# Q02 Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
"""
num = int(input("digite um numero: "))
print(f"o numero informado foi {num}")"""

# Q03 Faça um Programa que peça dois números e imprima a soma.

"""numUm = int(input("digite um numero: "))
numDois = int(input("digite outro numero: "))
resultado = numUm+numDois
print(f"a soma desses numeros e de: {resultado}")"""

# Q04 Faça um Programa que peça as 4 notas bimestrais e mostre a média.

"""notaUm = int(input ("digite a primeira nota: "))
notaDois = int(input("digite a segunda nota: "))
notaTres = int(input("digite a terceira nota: "))
notaQuatro = int(input("digite a quarta nota: "))
media = (notaUm+notaDois+notaTres+notaQuatro)/4
print(f'a media das quatro notas e de {media}')
"""
# Q05 Faça um Programa que converta metros para centímetros.

"""valorMetros = int(input("digite a quantidade em metros para ser transformada pra centrimetros:"))
valorCent = valorMetros*100
print(f"o valor transformado e de: {valorCent}cm")
"""
# Q06 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

"""raio = int(input("digite o valor do raio:" ))
area = ((raio**2)*3.14)
print(f"o valor da area do circulo e igual a {area}")"""

# Q07 Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

"""lado =float(input("digite o tamanho do lado de um quadrado: "))
area = (lado**2)*2
print(f"o dobro da area deste quadrado e de {area}")
"""
# Q08 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre
# o total do seu salário no referido mês.

"""valorHora = int(input("quanto voce ganha por hora?: "))
horasMes = int(input("quantas horas voce trabalha por mes?"))
salario = valorHora*horasMes
print(f"o seu salario e de {salario}")"""

# Q09 Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

"""
temp = float(input("digite a temperatura em Fahrenheit para ser transformada pra Celsius:"))
tempCel = (((temp-32)/9)*5)
print(f"a temperatura {temp}F em Celsius e de {tempCel} graus")
"""

# Q10Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""
temp = float(input("digite a temperatura em Celsius para ser transformada para Fahrenheit :"))
tempFah =  ((temp * 9/5) + 32 )
print(f"a temperatura {temp} Celsius em farhrenheit e de {tempFah} graus")
"""
# Q11 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a: o produto do dobro do primeiro com metade do segundo .
# b: a soma do triplo do primeiro com o terceiro.
# c: o terceiro elevado ao cubo.
"""
numUm= int(input("digite o primeiro numero: "))
numDois = int(input("digite o segundo numero: "))
numTres = float(input("digite o terceiro numero: "))
a = (numUm*2)*(numDois/2)
b = (3*numUm)+(numTres)
c = numTres**3
print(a,b,c)
"""

# Q12 Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a
# seguinte fórmula: (72.7*altura) - 58
"""
altura = float(input("digite a sua altura: "))
peso = (altura*72.7)-58
print(f"o seu peso ideal e de {peso:.2f}")
"""
# Q13 Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para homens: (72.7*h) - 58

"""altura = float(input("digite a sua altura: "))
pesoHom = (altura*72.7)-58
pesoMul = (altura*62.1)-44.7
print(f"para homens com {altura}m de altura o peso ideal e de: {pesoHom:.2f}kg")
print(f"para mulheres com {altura}m de altura o peso ideal e de: {pesoMul:.2f}kg")
"""

# Q14 João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu
# trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de
# São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que
# leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do
# limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens
# adequadas.

"""
pesoPeixe = float(input("digite o peso do peixe: "))
excesso = float
if (pesoPeixe > 50):
    excesso = pesoPeixe - 50
    print(f"o valor da multa e de {excesso*4}R$ por {excesso}kg em excesso")
"""
# Q15 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre
# o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
# 5% para o sindicato, faça um programa que nos dê: salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato.
# o salário líquido.

"""horaPreco = float(input("digite quanto voce ganha por hora: "))
horaTrabalho = float(input("digite quantas hora voce trabalha por mes: "))
salBruto = horaTrabalho*horaPreco
ir = (salBruto*0.11)
inss = (salBruto*0.08)
sind = (salBruto*0.05)
salLiq = (salBruto-ir-inss-sind)
print(f"o valor do seu salario bruto e de R$ {salBruto:.2f} \no imposto de renda e de RS {ir:.2f} \no INSS e de R$ {inss:.2f}"
      f"\no sindicato R$ {sind:.2f}\no seu salario liquido e de R$ {salLiq:.2f}")
"""

# Q16 Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas
# de 18 litros que custam R$ 80,00 Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
tam = int(input("digite o tamanho em metros da area a ser pintada: "))
tinta = int(54)
total =  int(tam/tinta)
if (tam%tinta != 0):
    total = total +1
print(f"voce deve comprar {total:.0f} galoes de tinta\nvalor a total R$ {total*80:.2f}")
"""

# Q17 Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas
# de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# * comprar apenas latas de 18 litros;
# * comprar apenas galões de 3,6 litros;
# * misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde
# os valores para cima, isto é, considere latas cheias.
# nao fiz a parte de misturar as latas
"""
tam = int(input("digite o tamanho em metros da area a ser pintada: "))
tam = tam * 1.1
tinta = int(21.6)
total = int(tam / tinta)

tinta2 = int(108)
total2 = int(tam / tinta2)

galao3 = int(tam / tinta2)
lata3 = int(tam - galao3 * tinta2) / tinta

valor = int(galao3 * 80) + (lata3 *25)

if (tinta2 % tam > 0):
    total2 = total2 + 1

if (tinta % tam > 0):
    total = total + 1

print(f"voce deve comprar {total:.0f} galoes de 3.6L\nvalor total R$ {total * 25:.2f}")
print(f"voce deve comprar {total2:.0f} galoes de 18L\nvalor total R$ {total2 * 80:.2f}")
print(f"voce deve comprar {galao3:.0f} galoes de 18L e {lata3:.0f} latas de 3,6L\nvalor total R$ {valor:.2f}")
"""

# Q18 Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
# (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
arquivo = float(input("digite o tamanho do arquivo: "))
velocidade = float(input("digite a velocidade do link: "))
total = ((arquivo* 8 )/velocidade)/60
print(f"tempom aproximado {total:.2f} minutos")
"""
