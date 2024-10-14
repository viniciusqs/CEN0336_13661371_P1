# script_temp.py

# Função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    return (9/5) * celsius + 32

# Solicita ao usuário para inserir uma lista de temperaturas em graus Celsius
entrada = input("Digite as temperaturas em graus Celsius (separadas por espaço): ")

# Tenta dividir a entrada em uma lista de strings e converter para float
try:
    # Cria uma lista de temperaturas, convertendo cada valor de string para float
    temperaturas_celsius = [float(temp) for temp in entrada.split()]
except ValueError:
    print("Erro: Por favor, insira apenas números válidos.")
    exit(1)

# Inicializa uma lista vazia para armazenar as temperaturas convertidas
temperaturas_fahrenheit = []

# Converte cada temperatura de Celsius para Fahrenheit usando um loop
for celsius in temperaturas_celsius:
    fahrenheit = celsius_para_fahrenheit(celsius)
    temperaturas_fahrenheit.append(fahrenheit)

# Exibe as temperaturas em uma tabela
print("Celsius   Fahrenheit")
for celsius, fahrenheit in zip(temperaturas_celsius, temperaturas_fahrenheit):
    print(f"{celsius:7}   {fahrenheit:.1f}")
