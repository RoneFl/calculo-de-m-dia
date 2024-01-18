# Função para validar a entrada de notas entre 0 e 10
def validar_nota():
    while True:
        nota = float(input("Digite uma nota entre 0 e 10: "))
        if 0 <= nota <= 10:
            return nota
        else:
            print("Entrada inválida. Digite uma nota entre 0 e 10.")

# Solicita ao usuário que insira as três notas
nota1 = validar_nota()
nota2 = validar_nota()
nota3 = validar_nota()

# Calcula a média das notas
media = (nota1 + nota2 + nota3) / 3

# Exibe a média
print("Média:", media)

# Verifica se a média é maior ou igual a 7
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
