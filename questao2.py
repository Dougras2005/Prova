'''
Questão 2: Implementar uma Calculadora com Loop
Escreva uma função chamada calculadora que recebe três argumentos: dois números (a e b) e uma string representando a operação (operacao). 
A função deve retornar o resultado da operação aplicada aos dois números. As operações suportadas são:

    + para adição
    - para subtração
    * para multiplicação
    / para divisão

A função deve lidar com a divisão por zero e retornar uma mensagem apropriada nesse caso.

Segue um trecho mostrando como deve ser implementada a função:
    def calculadora(a, b, operacao):
        if operacao == '+':
            return a + b


Na entrada dos números deve ser feito o tratamento de exceções, para que seja tratado os casos que não sejam digitados números.

O programa deve ficar em loop, solicitando ao usuário os valores e a operação até que o usuário digite s para sair.

Os números digitados devem ser armazenados em uma lista e depois de encerrar, mostrar a lista, o maior número, o menor número e a média dos números.

'''

def calculadora(a, b, operação):
    if operação == '+':
        return a + b
    elif operação == '-':
        return a - b
    elif operação == '*':
        return a * b
    else:
        return a / b
    


while True:


    try:

        a = float(input('Digíte um número (Digíte s para encerrar): '))
        b = float(input('Digíte um número (Digíte s para encerrar): '))
        operação = input('Digíte a operação desejada(+ para adição, - para subtração, * para multiplicação e / para divisão)(Digíte s para encerrar): ')


    except ZeroDivisionError:       
        print('Impossilvel dividir um número por zero')
    except ValueError:
        print('Digíte o número correto!')
    finally:
        opçao = input('Digite s para encerrar: ')
        if opçao == 's':
            break



    
        

    
            
        print(calculadora(a, b, operação))
       