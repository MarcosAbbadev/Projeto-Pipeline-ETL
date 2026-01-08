"""
ETL Pipeline com IA
Projeto demonstrativo para portfólio
"""

# =========================
# IMPORTS
# =========================

from openai import OpenAI
from openai import RateLimitError, AuthenticationError


# =========================
# CONFIGURAÇÃO
# =========================

# Em projeto real, isso vem de variável de ambiente
openai_api_key = "OPENAI_API_KEY"
client = OpenAI(api_key=openai_api_key)


# =========================
# EXTRACT
# =========================

def extract_users():
    """
    Simula a extração de usuários de uma fonte de dados.
    """
    return [
        {"id": 1, "name": "João", "news": []},
        {"id": 2, "name": "Maria", "news": []},
        {"id": 3, "name": "Carlos", "news": []}
    ]


# =========================
# TRANSFORM
# =========================

def generate_ai_news(user):
    """
    Gera uma mensagem personalizada usando IA.
    Possui fallback em caso de limite de quota.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Você é um especialista em marketing bancário."
                },
                {
                    "role": "user",
                    "content": (
                        f"Crie uma mensagem para {user['name']} "
                        f"sobre a importância dos investimentos (máx. 100 caracteres)."
                    )
                }
            ],
            max_tokens=60,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()

    except (RateLimitError, AuthenticationError):
        return (
            f"{user['name']}, investir hoje é construir "
            f"segurança e liberdade financeira amanhã."
        )


def transform_users(users):
    """
    Aplica a transformação com IA e exibe o output.
    """
    print("\n=== INÍCIO DO TRANSFORM ===\n")

    for user in users:
        news_text = generate_ai_news(user)

        user["news"].append({
            "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
            "description": news_text
        })

        # Output do transform
        print(f"Usuário: {user['name']}")
        print(f"Mensagem IA: {news_text}")
        print("-" * 60)

    print("\n=== FIM DO TRANSFORM ===")


# =========================
# LOAD
# =========================

def load_user(user):
    """
    Simula o carregamento dos dados para um sistema externo.
    """
    print(f"[LOAD] Enviando usuário ID {user['id']}...")
    print("[LOAD] Payload:")
    print(user)
    print("[LOAD] Status: SUCESSO")
    print("=" * 60)
    return True


def load_users(users):
    print("\n=== INÍCIO DO LOAD ===\n")

    success_count = 0

    for user in users:
        if load_user(user):
            success_count += 1

    print(f"\n=== LOAD FINALIZADO: {success_count}/{len(users)} usuários processados ===")


# =========================
# EXECUÇÃO DO PIPELINE
# =========================

if __name__ == "__main__":
    users = extract_users()
    transform_users(users)
    load_users(users)
