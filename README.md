#Assistente de Viagem Inteligente

Este é um aplicativo de desktop simples, criado com o framework Flet, que utiliza a inteligência artificial do Google Gemini para gerar roteiros de viagem personalizados.

O usuário informa o destino, seus interesses e a duração da viagem, e o aplicativo retorna uma sugestão de roteiro detalhado.

## ✨ Funcionalidades

    Interface de usuário moderna e responsiva, criada com Flet.

    Geração de roteiros de viagem em tempo real, powered by Gemini.

    Input de usuário para destino, interesses e duração da viagem.

    Uso de API Key de forma segura com arquivos de ambiente (.env).

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para clonar o repositório e rodar a aplicação em sua máquina local.

Pré-requisitos

Certifique-se de que você tem o Python 3.8+ instalado em seu sistema.

### Instalação

    Abra o terminal na pasta do projeto.

    Instale as bibliotecas necessárias usando pip:
    Bash

    pip install flet google-generativeai python-dotenv

### Configuração da API do Gemini

    Vá até o site do Google AI Studio para obter a sua chave de API:
    aistudio.google.com/app/apikey

    Crie um novo arquivo chamado .env na mesma pasta do projeto.

    Dentro dele, adicione sua chave de API desta forma, substituindo SUA_CHAVE_AQUI pela sua chave:

    API_KEY="SUA_CHAVE_AQUI"

### Executando o Aplicativo

Com a instalação e a configuração da chave concluídas, você pode rodar a aplicação com o seguinte comando:
Bash

flet run assistente_viagem.py

O aplicativo será iniciado em uma nova janela.