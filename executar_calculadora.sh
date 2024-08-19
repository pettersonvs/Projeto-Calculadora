#!/bin/bash

# Verifica se o Python 3 está instalado
if ! command -v python3 &> /dev/null
then
    echo "Python 3 não está instalado. Instalando agora..."
    
    sudo apt-get update
    
    sudo apt-get install -y python3
    
    echo "Python 3 foi instalado com sucesso."
fi

# Executa o script Python
python3 calculadora.py

