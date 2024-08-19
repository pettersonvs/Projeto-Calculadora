# Calculadora

Este repositório contém um script Python que simula uma calculadora básica

## Explicando os arquivos

- calculadora.py: Contém o código da calculadora Python.
- executar_calculadora.sh: É um script shell que verifica se o Python está instalado e, em seguida, executa o script da calculadora.py.

### Executando o arquivo .sh

Para executar o script Python usando o arquivo `.sh`, siga os passos abaixo:

1. Precisa ter os dois arquivos no diretório
2. Abra o terminal
3. Navegue até o diretório do repositório clonado.
- Ex. :
   ```bash
   cd /mnt/c/Users/SeuUsuario/repositorio
5. Execute o seguinte comando no terminal:
   ```bash
   ./executar_calduladora.sh

### Explicação do código em Python

1. Dicionário de fechamento
```python
fechar_programa = {'esc', 'ESC', 'Esc'}
```
- Armazena as formas permitidas para encerrar o programa.
- Permite verificar se a entrada do usuário corresponde a uma das palavras para fechar o programa.

2. Estrutura do loop principal
  ```python
  print('\nCALCULADORA\n')
  
  while True:
    print('\nDigite "esc" a qualquer momento para fechar o programa.\n')
  ```
- Objetivo: Imprime uma mensagem inicial e inicia um loop infinito.
- Uso: O loop permite que o programa continue rodando até que o usuário escolha encerrar.

3. Solicitação de Entrada do Usuário
```python
    num1 = input('\nDigite o primeiro número: ')
    if num1 in fechar_programa:
        print('\nPrograma encerrado.')
        break

    num2 = input('Digite o segundo número: ')
    if num2 in fechar_programa:
        print('\nPrograma encerrado.')
        break
```
- Objetivo: Solicita dois números ao usuário.
- Verificação de Fechamento: Checa se a entrada é uma das palavras para encerrar o programa. Se for, imprime uma mensagem e encerra o loop.

4. Conversão e Validação das Entradas
```python
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print('\nEntrada inválida. Por favor, insira números válidos.\n')
        continue
```
- Converte as entradas para float e lida com entradas inválidas.
- Se a conversão falhar (por exemplo, se o usuário inserir texto não numérico), imprime uma mensagem de erro e continua para a próxima iteração do loop.

5. Exibição das Opções de Operação e Realização da Operação
```python
    print('\nEscolha a operação:')
    print('1: Adição')
    print('2: Subtração')
    print('3: Multiplicação')
    print('4: Divisão')

    valor = input('\nSelecione a operação desejada: ')
```
- Exibe as opções de operações matemáticas disponíveis.
- Solicita ao usuário que escolha uma operação.

6. Processamento da Operação Selecionada
```python
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
```
- Realiza a operação matemática de acordo com a escolha do usuário e imprime o resultado.
- Se o usuário escolher uma opção não válida ou uma forma de encerrar o programa, lida adequadamente com esses casos.
