# Calculadora

Este repositório contém um script Python que simula uma calculadora básica

## Explicando os arquivos

- calculadora.py: Contém o código da calculadora Python.
- executar_calculadora.sh: É um script shell que verifica se o Python está instalado e, em seguida, executa o script da calculadora.py.

### Executando o arquivo .sh

Para executar o script Python usando o arquivo `.sh`, siga os passos abaixo:

1. Abra o terminal
2. Navegue até o diretório do repositório clonado.
3. Execute o seguinte comando no terminal:
   ```bash
   ./executar_calduladora.sh

### Explicação do código em Python

1. Dicionário de fechamento
```python
fechar_programa = {'esc', 'ESC', 'Esc'}
```
- Objetivo: Armazena as formas permitidas para encerrar o programa.
- Tipo: Conjunto (set).
- Uso: Permite verificar se a entrada do usuário corresponde a uma das palavras para fechar o programa.
2. Estrutura do loop principal
  ```python
  print('\nCALCULADORA\n')

while True:
    print('\nDigite "esc" a qualquer momento para fechar o programa.\n')```
    
-Objetivo: Imprime uma mensagem inicial e inicia um loop infinito.
-Uso: O loop permite que o programa continue rodando até que o usuário escolha encerrar.
