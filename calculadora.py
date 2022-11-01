again = 'SIM'

while (again == 'SIM'):
  print('\nBem-vindo a calculadora\n')
  operation = input('Por favor, digite o operador matemático refere a conta que deseja realizar:\n + para adição\n - para subtração\n * para multiplicação\n / para divisão\n\n')
  
  if operation == '+':
    num01 = float(input('\nDigite o primeiro valor: '))
    num02 = float(input('Digite o segundo valor: '))
    adicao = num01 + num02
    print(f'\nA soma entre {num01} e {num02} é: {adicao}\n')
    again = input('Gostaria de fazer outra operação? Sim ou não: ').upper()

  if operation == '-':
    num01 = float(input('\nDigite o primeiro valor: '))
    num02 = float(input('Digite o segundo valor: '))
    subtracao = num01 - num02
    print(f'\nA subtração entre {num01} e {num02} é: {subtracao}\n')
    again = input('Gostaria de fazer outra operação? Sim ou não: ').upper()

  if operation == '*':
    num01 = float(input('\nDigite o primeiro valor: '))
    num02 = float(input('Digite o segundo valor: '))
    multiplicacao = num01 * num02
    print(f'\nA multiplicação entre {num01} e {num02} é: {multiplicacao}\n')
    again = input('Gostaria de fazer outra operação? Sim ou não: ').upper()

  if operation == '/':
    num01 = float(input('\nDigite o primeiro valor: '))
    num02 = float(input('Digite o segundo valor: '))
    while num02 == 0:
      print('O segundo valor não pode ser zero!')
      num02 = float(input('\nDigite o segundo valor (diferente de zero): '))
    divisao = num01 / num02
    print(f'\nA divisão entre {num01} e {num02} é: {divisao}\n')
    again = input('Gostaria de fazer outra operação? Sim ou não: ').upper()
    
print('\nAté a próxima :)')