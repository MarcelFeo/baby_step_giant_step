from math import sqrt, ceil

def eh_primo(n):
    for count in range(2,n):
        if(n % count == 0):
            return False

    return True


p = int(input("Digite um número primo: "))
a = int(input("Digite um gerador do grupo multiplicativo módulo p: "))
b = int(input("Digite o valor para encontrar o expoente 'x': "))

if(eh_primo(p)):
    print("é primo!")
else:
    print("não é primo!")
