from math import sqrt, ceil

def eh_primo(n):
    for count in range(2,n):
        if(n % count == 0):
            return False

    return True

def baby_step_giant_step(a, b, p):
    # Verifica se 'a' é um gerador do grupo multiplicativo módulo 'p'
    if pow(a, (p - 1) // 2, p) != 1:
        raise ValueError("'a' não é um gerador do grupo multiplicativo módulo 'p'")

    # Calcula o tamanho aproximado da tabela
    m = ceil(sqrt(p - 1))

    # Baby step: cria uma tabela de baby steps
    baby_steps = {}
    val = 1
    for i in range(m):
        if val not in baby_steps:
            baby_steps[val] = i
        val = (val * a) % p

    # Calcula o inverso multiplicativo de a^(m)
    inv_a_m = pow(pow(a, m, p), p - 2, p)

    # Giant step: verifica cada possível valor de x e procura um correspondente na tabela de baby steps
    val = b
    for j in range(m):
        if val in baby_steps:
            return j * m + baby_steps[val]
        val = (val * inv_a_m) % p

    # Se nenhum correspondente for encontrado, não há solução
    raise ValueError("Não foi encontrada uma solução")

p = int(input("Digite um número primo: "))
a = int(input("Digite um gerador do grupo multiplicativo módulo p: "))
b = int(input("Digite o valor para encontrar o expoente 'x': "))

if(eh_primo(p)):
    x = baby_step_giant_step(a, b, p)
    print(f"O valor de 'x' é: {x}")
else:
    print("não é primo!")
