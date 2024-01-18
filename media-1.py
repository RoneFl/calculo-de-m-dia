'''
1. O bloco "else" em Python é utilizado para executar um conjunto de instruções quando 
a condição associada ao "if" anterior é avaliada como falsa. 
Em outras palavras, enquanto o bloco "if" é acionado quando a condição é verdadeira, 
o bloco "else" é acionado quando a condição é falsa.
O "else" é uma maneira de fornecer alternativas nos seus programas. 
Se a condição do "if" não for atendida, o código dentro do bloco "else" será executado.

2. A condição "else" não aceita uma expressão de comparação como o ">=". 
O correto seria utilizar "elif" (abreviação de "else if") 
para verificar uma segunda condição. 

3. Por convenção, a condição "else if", não é permitido usar em Python. 
É uma decisão de design da linguagem. A linguagem Python optou por usar a palavra-chave "elif" 
em vez de "else if" para tornar o código mais limpo e mais legível.

'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
print()

media = (nota1 + nota2 + nota3) / 3
print('=================', '\n')
print('Sua Média foi: ', media, '\n')

if media < 7:
    print("Você foi reprovado")
elif media >= 7:
    print('Parabéns! Você foi aprovado.')