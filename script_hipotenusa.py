
# Importa o módulo sys para trabalhar com argumentos de linha de comando
import sys

# Verifica se o número correto de argumentos foi passado
if len(sys.argv) != 3:
    print("Erro: Você deve fornecer exatamente dois números inteiros positivos.")
    sys.exit(1)

# Captura os argumentos da linha de comando
arg_a = sys.argv[1]
arg_b = sys.argv[2]

# Verifica se os argumentos são inteiros e positivos menores que 500
if not arg_a.isdigit() or not arg_b.isdigit():
    print("Erro: Ambos os argumentos devem ser números inteiros positivos.")
    sys.exit(1)

# Converte os argumentos para inteiros
a = int(arg_a)
b = int(arg_b)

# Verifica se os números são menores que 500
if a >= 500 or b >= 500:
    print("Erro: Ambos os números devem ser menores que 500.")
    sys.exit(1)

# Calcula o quadrado da hipotenusa usando o Teorema de Pitágoras
# hipotenusa² = a² + b²
quadrado_hipotenusa = a**2 + b**2

# Imprime o resultado no formato desejado
print(f"O quadrado da hipotenusa para o triângulo retângulo com lados a={a} e b={b}, é {quadrado_hipotenusa}.")
