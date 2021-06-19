# Q01 Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
# continue pedindo até que o usuário informe um valor válido.
"""
nota = int(input("digite uma nota: "))
while nota > 10 or nota < 0:
    nota = int(input("digite uma nota valida: "))
print(f"nota valida ({nota})")
"""

# Q02 Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.
from operator import index

"""
user = input("digite um nome de usuario: ")
senha = input("digite sua senha: ")
while senha == user:
    senha = input("por favor digite outra senha: ")
print(f"senha valida!")
"""

# Q03 Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';
"""
nome = input("digite seu nome: ")
while len(nome) <= 3:
    nome = input("por favor digite um nome com mais caracteres: ")

idade = int(input("digite sua idade: "))
while 150 < idade or idade <= 0:
    idade = int(input("por favor digite um idade valida:"))

salario = int(input("digite seu salario: "))
while salario <= 0:
    salario = int(input("por favor digite um salario valido: "))

sexo = input("digite o seu sexo: \n f - feminino \n m - masculino\n")
sexo = sexo.strip().lower()
while sexo != "f" and sexo != "m":
    sexo = input("digite uma letra valida: ")
    sexo = sexo.strip().lower()

estado = input("digite o seu estado civil: \n s - solteiro(a)\n c - casado(a)\n v - viuvo(a)\n d - divorciado(a)\n")
estado = estado.strip().lower()
while estado != "s" and estado != "c" and estado != "v" and estado != "d":
    estado = estado.strip().lower()

print(f"informacoes validas\n {nome}\n {idade}\n {salario}\n {sexo}\n {estado}")
"""

# Q04 Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento
# de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa
# que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população
# do país B, mantidas as taxas de crescimento.
"""
cidA = 80000
cidB = 200000
ano = 0
while cidA < cidB:
    cidA += cidA* 0.03
    cidB += cidB * 0.015
    ano += 1
print(f"a cidade a vai demorar {ano} anos para ultrapassar a populacao da cidade b")
"""

# Q05 Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.
"""
cidA = int(input("digite a populacao da primeira cidade: "))
cidB = int(input("digite a populacao da segunda cidade: "))
taxaA = float(input("digite a taxa da primeira cidade: "))
taxaB = float(input("digite a taxa da segunda cidade: "))
ano = 0
if cidA < cidB and taxaA > taxaB:
    while cidA < cidB:
        cidA += cidA* taxaA
        cidB += cidB * taxaB
        ano += 1
print(f"a cidade a vai demorar {ano} anos para ultrapassar a populacao da cidade b")
"""

# Q06 Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa
# para que ele mostre os números um ao lado do outro.
"""
for i  in range (1,21):
     print(i)
     
for i  in range (1,21):
     print(i,end="")
"""

# Q07 Faça um programa que leia 5 números e informe o maior número.
"""
lista = []
for i in range(5):
    num1 = int(input("digite um numero: "))
    lista = lista + [num1]
print(f" o maio numero e: {max(lista)}")
print(lista)
"""

# Q08 Faça um programa que leia 5 números e informe a soma e a média dos números.
"""lista = []
for i in range(5):
    num = int(input("digite um numero: "))
    lista += [num]

print(f"a soma dos numeros e de: {num(lista)}")
print(f"a media dos numeros e de: {sum(lista) / len(lista)}")
"""

# Q08.1 (Extra) Faça um programa que leia quantos números o usuario quiser e informe a soma e a média dos números.
"""
lista = []
x = 1
print("digite 0 para parar a entrada de numeros!")
while x != 0:
    num = int(input("digite um numero: "))
    lista += [num]
    x = num
print(f"a soma dos numeros e de: {sum(lista)}")
print(f"a media dos numeros e de: {sum(lista)/len(lista)}")
print(f"o total de numeros digitados e de: {len(lista)}")
"""

# Q09 Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
"""
for i in range(1,50,2):
    print(i)
"""

# Q10 Faça um programa que receba dois números inteiros e gere os números inteiros que estão no
# intervalo compreendido por eles.
"""
num1 = int(input("digite um numero: "))
num2 = int(input("digite um numero: "))
for i in range(num1+1, num2):
    print(i)
"""

# Q11 Altere o programa anterior para mostrar no final a soma dos números.
"""
num1 = int(input("digite um numero: "))
num2 = int(input("digite um numero: "))
soma = 0
for i in range(num1+1, num2):
    soma += i
print(soma)
"""

# Q12 Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50
"""
num = int(input("digite o numero que deseja ver a tabuada: "))
if 10 <= num or num >= 1:
    for i in range(1,11):
        print(f"{num} X {i} = {num * i}")
"""

# Q13 Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado
# ao segundo número. Não utilize a função de potência da linguagem

"""
base = int(input("digite a base: "))
exp = int(input("digite o expoente: "))
resultado = base
for i in range(exp-1):
    resultado = (resultado*base)

print(f"o resultado e de: {resultado}")


    # outro jeito
num = int(input("digite um numero: "))
res = 1
for i in range(num):
    res = res * num
    print(res)


"""

# Q14 Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares
# e a quantidade de números impares.
"""
cont = 0
for i in range(9):
    num = int(input("digite um numero: "))
    if num % 2 == 0:
        cont += 1

print(f" a quantidade de numeros pares e de {cont} e {10-cont} numeros impares")

"""

# Q15 A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz
# de gerar a série até o n−ésimo termo.
"""
num = int(input("digite um numero: "))
n1, n2 = 0, 1
count = 0
for i in range(num):
    print(f"{n1} ", end="")
    nth = n1 + n2
    #update numbers
    n1 = n2
    n2 = nth
"""

# Q16 A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
# Faça um programa que gere a série até que o valor seja maior que 500.

"""n1, n2 = 0, 1
count = 0
while n1 < 500:
    print(f"{n1} ", end="")
    nth = n1 + n2
    num = nth
    #update numbers
    n1 = n2
    n2 = nth
    count += 1
print(f"{count} = numero de sequencias")
"""

# Q17 Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""
num = int(input("digite um numero: "))
conta = num
x = num
if num == 1:
    print(f"o fatorial de {num} = 1 !")
elif 0 < num < 16:
    for c in range(1, num):
        conta = conta * (x-1)
        resu = conta
        x -= 1
    print(f"o fatorial de {num} = {resu} !")

"""

# Q18 Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""
lista = []
x = 0
soma = 0
print("digite 0 para parar")
while x == 0:
    num = int(input("digite um numero: "))
    if num == 0:
        x = 1
    else:
        lista.append(num)
        soma += num
print(f"soma = {soma}")
print(f"menor valor = {min(lista)}")
print(f"maior valor = {max(lista)}")
"""

# Q19 Altere o programa anterior para que ele aceite apenas números entre 0 e 1000. coloquei entre 1 e 1000
"""
lista = []
x = 0
soma = 0
print("digite 0 para parar")
while x == 0:
    num = int(input("digite um numero: "))
    if num > 1000 or num < 0:
        print("digite um numero valido!")
    elif num == 0:
        print(f"soma = {soma}")
        print(f"menor valor = {min(lista)}")
        print(f"maior valor = {max(lista)}")
        x = 1
        break
    else:
        lista.append(num)
        soma += num

"""

# Q20 Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
# fatorial a números inteiros positivos e menores que 16.
"""
cont = 0
while cont == 0:
    num = int(input("digite um numero: "))
    conta = num
    x = num
    if num == 1:
        print(f"o fatorial de {num} = 1 !")
    elif 0 < num < 16:
        for c in range(1, num):
            conta = conta * (x-1)
            resu = conta
            x -= 1
        print(f"o fatorial de {num} = {resu} !")
    else:
        print("digite um numero valido!")
        #print('\033[0:30:45mteste\033[m')
"""

# Q21 Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é 
# aquele que é divisível somente por ele mesmo e por 1.
"""
num = int(input("digite um numero: "))
conta = 0
for i in range(1, num+1):
    if num % i == 0:
        conta += 1

if conta == 2:
    print(f"o numero {num} e primo!")
else:
    print(f"o numero nao e primo!")
"""



