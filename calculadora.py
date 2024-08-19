# Dicionário com as formas de encerrar o programa
fechar_programa = {'esc', 'ESC', 'Esc'}

print('\nCALCULADORA\n')

while True:
    print('\nDigite "esc" a qualquer momento para fechar o programa.\n')


    # Solicita os números ao usuário
    num1 = input('\nDigite o primeiro número: ')
    if num1 in fechar_programa:
        print('\nPrograma encerrado.')
        break

    num2 = input('Digite o segundo número: ')
    if num2 in fechar_programa:
        print('\nPrograma encerrado.')
        break


    # Converte os números para float e lida com entradas inválidas
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print('\nEntrada inválida. Por favor, insira números válidos.\n')
        continue


    # Exibe as opções de operação e realiza de acordo com a escolha do usuário
    print('\nEscolha a operação:')
    print('1: Adição')
    print('2: Subtração')
    print('3: Multiplicação')
    print('4: Divisão')


    valor = input('\nSelecione a operação desejada: ')


    if valor == '1':
        resultado = num1 + num2
        print('\n', str(num1) + ' + ' + str(num2) + ' = ' + str(resultado),'\n')
    elif valor == '2':
        resultado = num1 - num2
        print('\n', str(num1) + ' - ' + str(num2) + ' = ' + str(resultado),'\n')
    elif valor == '3':
        resultado = num1 * num2
        print('\n', str(num1) + ' * ' + str(num2) + ' = ' + str(resultado),'\n')
    elif valor == '4':
        if num2 != 0:   # Verifica se o denominador (segundo número) é zero
            resultado = num1 / num2
            print('\n', str(num1) + ' / ' + str(num2) + ' = ' + str(resultado),'\n')
        else:
            print('Erro: Divisão por zero não é permitida.\n')
    elif valor in fechar_programa:
        print('\nPrograma encerrado.')
        break
    else:
        print('Opção inválida. Por favor, escolha uma operação válida.')
