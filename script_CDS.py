
import sys

# Verifica se o número correto de argumentos foi passado
if len(sys.argv) != 7:
    print("Uso: python script_CDS.py <sequência_DNA> <n1> <n2> <n3> <n4> <n5> <n6>")
    sys.exit(1)

# Atribui os argumentos a variáveis
sequencia_dna = sys.argv[1]
n1, n2, n3, n4, n5, n6 = sys.argv[2:8]

# Verifica se n1 a n6 são inteiros e estão dentro dos limites da sequência
try:
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    n4 = int(n4)
    n5 = int(n5)
    n6 = int(n6)

    if any(n > len(sequencia_dna) for n in [n1, n2, n3, n4, n5, n6]):
        raise ValueError("Um ou mais números inteiros são maiores que o tamanho da sequência de DNA.")
except ValueError as e:
    print(f"Erro: {e}")
    sys.exit(1)

# Extrai a sequência entre CDS 1 (n1) e CDS 2 (n2)
sequencia_cds1_cds2 = sequencia_dna[n1-1:n2]

# Verifica se a sequência começa com 'GT' e termina com 'AG'
if sequencia_cds1_cds2.startswith("GT") and sequencia_cds1_cds2.endswith("AG"):
    print("A sequência entre CDS 1 e CDS 2 é válida.")
else:
    print("A sequência entre CDS 1 e CDS 2 é inválida.")
    sys.exit(1)

# Extrai a sequência entre CDS 2 (n2) e CDS 3 (n3)
sequencia_cds2_cds3 = sequencia_dna[n2:n3]

# Verifica se a sequência começa com 'GT' e termina com 'AG'
if sequencia_cds2_cds3.startswith("GT") and sequencia_cds2_cds3.endswith("AG"):
    print("A sequência entre CDS 2 e CDS 3 é válida.")
else:
    print("A sequência entre CDS 2 e CDS 3 é inválida.")
    sys.exit(1)

# Concatena as CDS 1, 2 e 3
sequencia_resultante = sequencia_dna[n1-1:n4] + sequencia_dna[n3:n5] + sequencia_dna[n4-1:n6]

# Imprime a sequência resultante
print("A sequência resultante é:", sequencia_resultante)

