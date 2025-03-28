import random

def lancar_dado():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

resultado = lancar_dado()
print(f"O resultado foi {resultado}")