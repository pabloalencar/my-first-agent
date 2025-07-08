# My First Agent 🤖

Um agente de IA simples para dar as boas vindas usando a API da OpenAI.

## 📋 Pré-requisitos

- Python 3.8+
- Poetry
- Conta na OpenAI com API key

## 🚀 Instalação

1. **Clone o repositório e navegue até a pasta:**
   ```bash
   cd my-first-agent
   ```

2. **Instale as dependências com Poetry:**
   ```bash
   poetry install
   ```

3. **Configure as variáveis de ambiente:**
   ```bash
   cp .env.example .env
   ```
   
   Edite o arquivo `.env` e adicione sua API key da OpenAI:
   ```
   OPENAI_API_KEY=sua_api_key_aqui
   ```

## 🎯 Como usar

1. **Execute o agente:**
   ```bash
   poetry run python main.py
   ```

2. **Ou ative o ambiente virtual e execute:**
   ```bash
   poetry shell
   python main.py
   ```

3. **Digite seu nome quando solicitado e receba uma mensagem de boas vindas personalizada!**

## 🛠️ Estrutura do Projeto

```
my-first-agent/
├── main.py              # Arquivo principal do agente
├── pyproject.toml        # Configuração do Poetry
├── .env.example          # Exemplo de variáveis de ambiente
├── .env                  # Suas variáveis de ambiente (não commitado)
└── README.md            # Este arquivo
```

## 🔧 Configurações

- **OPENAI_API_KEY**: Sua chave da API OpenAI (obrigatória)
- **OPENAI_MODEL**: Modelo a ser usado (opcional, padrão: gpt-3.5-turbo)

## 📝 Funcionalidades

- ✅ Mensagens de boas vindas personalizadas
- ✅ Suporte a nomes de usuários
- ✅ Tratamento de erros
- ✅ Configuração via variáveis de ambiente
- ✅ Interface simples de linha de comando

## 🔑 Obtendo sua API Key

1. Visite [platform.openai.com](https://platform.openai.com)
2. Faça login ou crie uma conta
3. Vá para "API Keys" no menu
4. Clique em "Create new secret key"
5. Copie a chave e cole no arquivo `.env`

## 🤝 Contribuindo

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novas funcionalidades!

## 📄 Licença

Este projeto é apenas para fins educacionais. 