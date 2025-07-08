#!/usr/bin/env python3
"""
Agente de IA simples para dar as boas vindas
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

class WelcomeAgent:
    def __init__(self):
        """Inicializa o agente com a API key da OpenAI"""
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY não encontrada nas variáveis de ambiente")
        
        self.client = OpenAI(api_key=api_key)
        self.model = os.getenv('OPENAI_MODEL', 'gpt-4.1-nano')
    
    def welcome_user(self, user_name: str | None = None) -> str:
        """
        Gera uma mensagem de boas vindas personalizada
        
        Args:
            user_name: Nome do usuário (opcional)
            
        Returns:
            Mensagem de boas vindas gerada pela IA
        """
        if user_name:
            prompt = f"Dê as boas vindas de forma calorosa e amigável para {user_name}. Seja criativo e personalizado."
        else:
            prompt = "Dê as boas vindas de forma calorosa e amigável para um novo usuário. Seja criativo e acolhedor."
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system", 
                        "content": "Você é um assistente amigável e acolhedor. Sua função é dar boas vindas calorosas e criar um ambiente acolhedor."
                    },
                    {
                        "role": "user", 
                        "content": prompt
                    }
                ],
                max_tokens=150,
                temperature=0.7
            )
            
            message_content = response.choices[0].message.content
            return message_content.strip() if message_content else ""
            
        except Exception as e:
            return f"Desculpe, ocorreu um erro ao gerar a mensagem de boas vindas: {str(e)}"

def main():
    """Função principal do programa"""
    print("🤖 Agente de Boas Vindas")
    print("=" * 30)
    
    try:
        # Inicializa o agente
        agent = WelcomeAgent()
        
        # Solicita o nome do usuário
        user_name = input("Digite seu nome (ou pressione Enter para continuar): ").strip()
        
        # Gera e exibe a mensagem de boas vindas
        print("\n🎉 Gerando mensagem de boas vindas...")
        welcome_message = agent.welcome_user(user_name if user_name else None)
        
        print(f"\n{welcome_message}")
        
    except ValueError as e:
        print(f"❌ Erro de configuração: {e}")
        print("Por favor, configure sua OPENAI_API_KEY no arquivo .env")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    main() 