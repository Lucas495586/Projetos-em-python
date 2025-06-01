import random
import string

def gerar_senhas(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha 

senha_gerada = gerar_senhas(12)
print("senha gerada: ", senha_gerada)