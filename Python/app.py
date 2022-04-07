# "Imprimir" na tela
print("Olá, Mundo!")

# Imprimindo nome
nome = 'Lucas'
print(nome)

# Se, senao se, senao
nota1 = 7
nota2 = 7
nota3 = 7

media = (nota1 + nota2 + nota3) / 3

if (media >= 7):
    print("Aprovado")
elif (media >= 5) and (media < 7):
    print("Recuperação!")
else:
    print("Reprovado!")
print("Boa sorte na próxima!")           

# Lista
palavra = "programadores"
lista = [letra for letra in palavra]
print(lista)

# Idade
idade = 25

if (idade >= 18):
    print("Adulto")
elif (idade >= 14 and idade <= 17):
    print("Adolescente")  
else:
    print("Criança")

# Calculadora
num1 = 9
num2 = 3

soma = num1 + num2 
subtrair = num1 - num2 
divisao = num1 / num2 
multiplicar = num1 * num2 

print(soma)
print(subtrair)
print(divisao)
print(multiplicar)
