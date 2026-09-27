import json
import pandas as pd
import streamlit as st
from google import genai

st.set_page_config(
    page_title="FraudGuard - IA & Segurança Financeira",
    page_icon="🛡️"
)


#GEMINI 

GEMINI_API_KEY = "AQ.Ab8RN6LEhLCKhbVZNic2vlPvNvN9QpIljRDUhlHqMpqQmVnGGg"  #user test, not real

MODELO_GEMINI = "gemini-3.7-flash"


#DADOS

try:
    perfil_cliente = json.load(
        open(
            './data/perfil_investidor.json',
            encoding='utf-8'
        )
    )

    transacoes = pd.read_csv(
        './data/transacoes.csv'
    )

except Exception as e:
    st.error(
        f"Erro ao carregar os ficheiros de dados. "
        f"Verifique a pasta 'data': {e}"
    )
    st.stop()


#CONTEXTO

contexto = f"""
PERFIL DO CLIENTE:

Nome: {perfil_cliente.get('nome', 'Cliente')}
Idade: {perfil_cliente.get('idade', 'N/A')}
Profissão: {perfil_cliente.get('profissao', 'N/A')}

Renda Mensal: R$ {perfil_cliente.get('renda_mensal', '0')}
Patrimônio Total: R$ {perfil_cliente.get('patrimonio_total', '0')}

Perfil de Investidor: {perfil_cliente.get('perfil_investidor', 'N/A')}
Aceita Risco: {perfil_cliente.get('aceita_risco', 'N/A')}


HISTÓRICO DE TRANSAÇÕES E RISCOS:

{
    transacoes.to_string(index=False)
    if not transacoes.empty
    else "Sem transações."
}
"""


#system prompt

SYSTEM_PROMPT = f"""
Você é o FraudGuard, um assistente virtual especializado
em cibersegurança financeira e análise de fraudes.

CONTEXTO DOS DADOS DO CLIENTE:

{contexto}


OBJETIVO:

Analisar transações, identificar alertas de alto risco
e orientar sobre a segurança da conta.


REGRAS:

- NUNCA solicite ou exiba senhas, CVV ou dados sensíveis;
- JAMAIS responda a perguntas fora do tema de análise
  de transações e cibersegurança financeira;
- Se a pergunta fugir do escopo, informe que é um agente
  de segurança focado em fraudes;
- Seja claro, direto e didático.
"""


#INTERFACE

st.title("🛡️ FraudGuard - Monitor de Segurança & Fraudes")

st.write(
    f"Bem-vindo(a)! Monitorando a conta de "
    f"**{perfil_cliente.get('nome', 'Cliente')}**."
)


# 

if "gemini_client" not in st.session_state:
    st.session_state.gemini_client = genai.Client(
        api_key=GEMINI_API_KEY
    )


#HISTÓRICO

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []


# Historico 2

for mensagem in st.session_state.mensagens:

    with st.chat_message(mensagem["role"]):
        st.write(mensagem["content"])


#CHAT

if pergunta := st.chat_input(
    "Pergunte sobre suas transações, alertas de risco ou segurança..."
):

    # Mensagem do user
    with st.chat_message("user"):
        st.write(pergunta)

    # Salvar mensagem
    st.session_state.mensagens.append({
        "role": "user",
        "content": pergunta
    })


    # Gemini

    with st.chat_message("assistant"):

        with st.spinner("Analisando com IA..."):

            try:

                #Histórico da conversa
                historico = []

                for mensagem in st.session_state.mensagens:

                    historico.append({
                        "role": (
                            "user"
                            if mensagem["role"] == "user"
                            else "model"
                        ),
                        "parts": [
                            {
                                "text": mensagem["content"]
                            }
                        ]
                    })


                # Faz a requisição para o Gemini
                response = st.session_state.gemini_client.models.generate_content(
                    model=MODELO_GEMINI,
                    contents=historico,
                    config={
                        "system_instruction": SYSTEM_PROMPT
                    }
                )


                resposta = response.text

                # Mostra resposta
                st.write(resposta)


                # Salva resposta
                st.session_state.mensagens.append({
                    "role": "assistant",
                    "content": resposta
                })


            except Exception as e:

                st.error(
                    f"Não foi possível conectar com o Gemini: {e}"
                )
