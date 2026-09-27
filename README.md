# 🛡️ FraudGuard — Monitor de Segurança & Fraudes

> Assistente inteligente de segurança financeira desenvolvido com IA Generativa para analisar transações, interpretar scores de risco e fornecer orientações de segurança de forma clara e contextualizada.

## 📌 Sobre o projeto

O **FraudGuard** é um protótipo de agente financeiro inteligente criado para auxiliar na análise de segurança de uma conta fictícia.

A aplicação utiliza dados estruturados de um cliente e seu histórico de transações para fornecer respostas personalizadas por meio de uma interface conversacional. O agente foi projetado para interpretar informações de risco e ajudar o usuário a identificar movimentações que merecem atenção.

O projeto foi desenvolvido como parte de um desafio acadêmico de **IA Generativa aplicada ao setor financeiro**, com foco em personalização, segurança e confiabilidade das respostas.

## 🎯 Objetivos

- Analisar transações financeiras e seus respectivos indicadores de risco;
- Facilitar a interpretação de scores de risco por meio de linguagem natural;
- Fornecer orientações relacionadas à segurança da conta;
- Personalizar as respostas com base no perfil e no histórico do cliente fictício;
- Restringir o agente ao contexto de segurança financeira;
- Evitar a solicitação ou exposição de informações sensíveis.

## 🧩 Como funciona

O fluxo principal da aplicação é:


┌──────────────────────┐
│ Usuário              │
└──────────┬───────────┘
           │ pergunta
           ▼
┌──────────────────────┐
│ Interface Streamlit  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Aplicação Python     │
│                      │
│ • Perfil do cliente  │
│ • Transações         │
└──────────┬───────────┘
           │ contexto
           ▼
┌──────────────────────┐
│ System Prompt        │
│ + contexto dos dados │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Google Gemini        │
│ gemini-3.7-flash     │
└──────────┬───────────┘
           │ resposta
           ▼
┌──────────────────────┐
│ FraudGuard           │
│ resposta ao usuário  │
└──────────────────────┘


## 🛠️ Stack tecnológico

| Tecnologia | Utilização |
|---|---|
| **Python** | Lógica principal da aplicação |
| **Streamlit** | Interface web e chat interativo |
| **Pandas** | Leitura e manipulação do histórico de transações |
| **JSON** | Leitura das informações do perfil do cliente |
| **Google Gemini** | Modelo de IA Generativa utilizado pelo agente |
| **google-genai** | SDK para integração com a API do Gemini |

## 📂 Estrutura do projeto


Projeto-Final-GenAI/
│
├── 📁 data/
│   ├── perfil_investidor.json
│   └── transacoes.csv
│
├── 📁 Documentacao/
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
│
├── 📁 src/
│   └── app.py
│
└── 📄 README.md


## 🗃️ Base de conhecimento

O agente utiliza dados mockados armazenados localmente na pasta data/.

### `perfil_investidor.json`

Contém informações do cliente fictício utilizadas para contextualizar as respostas, como:

- Nome;
- Idade;
- Profissão;
- Renda mensal;
- Patrimônio total;
- Perfil de investidor;
- Aceitação de risco.

### `transacoes.csv`

Contém o histórico de transações utilizado pelo FraudGuard para análise de movimentações e riscos.

Entre as informações utilizadas está a coluna **score_risco_ml**, que representa a pontuação de risco associada às transações.

> Os dados utilizados no projeto são fictícios e foram empregados exclusivamente para fins acadêmicos e de demonstração.

## 🤖 Modelo de IA

O FraudGuard utiliza a **API do Google Gemini** por meio do SDK google-genai.

O modelo configurado na aplicação é:


gemini-3.7-flash


A integração foi escolhida em substituição ao modelo local utilizado inicialmente com Ollama, reduzindo a necessidade de armazenamento e processamento local e simplificando a arquitetura do protótipo.

## 🧠 System Prompt

O comportamento do agente é definido por um SYSTEM_PROMPT que estabelece:

- O papel do FraudGuard como assistente de segurança financeira;
- O uso do contexto do cliente e das transações;
- O objetivo de analisar riscos e orientar sobre a segurança da conta;
- A proibição de solicitar ou exibir senhas, CVV ou outros dados sensíveis;
- A restrição de respostas ao contexto de análise de transações e cibersegurança financeira;
- A necessidade de utilizar uma comunicação clara, direta e didática.

## 🔐 Segurança e limitações

O FraudGuard possui regras explícitas de segurança para reduzir respostas inadequadas ou informações inventadas.

O agente:

- Não solicita ou exibe senhas e CVV;
- Não possui acesso a contas bancárias reais;
- Não executa transações;
- Não realiza bloqueios de conta;
- Não substitui sistemas profissionais de monitoramento ou detecção de fraude;
- Utiliza dados fictícios fornecidos pela aplicação;
- Deve informar quando uma solicitação estiver fora do escopo definido.

## 💬 Exemplo de uso

O usuário pode fazer perguntas como:


"Existe alguma transação de alto risco?"



"Qual transação possui o maior score de risco?"



"Não reconheço essa transação. O que devo fazer?"


O FraudGuard utiliza o contexto disponível para elaborar uma resposta relacionada à segurança financeira.

## 📊 Avaliação

A qualidade do agente pode ser avaliada por meio de testes estruturados e feedback de usuários.

As principais métricas consideradas no projeto são:

- **Assertividade:** a resposta corresponde ao que foi perguntado e aos dados disponíveis?
- **Segurança:** o agente evita inventar informações ou fornecer dados sensíveis?
- **Coerência:** a resposta faz sentido para o perfil do cliente e para o contexto financeiro?

## 🚀 Como executar

### 1. Instale as dependências


pip install streamlit pandas google-genai


### 2. Configure a chave da API

No arquivo src/app.py, informe sua chave do Google Gemini na variável destinada à API:


GEMINI_API_KEY = "SUA_CHAVE_AQUI"


> **Importante:** não compartilhe sua chave de API em repositórios públicos, prints ou arquivos enviados para terceiros.

### 3. Execute a aplicação

A partir da pasta do projeto:


streamlit run src/app.py


Depois, abra no navegador o endereço informado pelo Streamlit, normalmente:


http://localhost:8501


## 📚 Documentação

A documentação complementar do projeto está organizada em:

| Arquivo | Conteúdo |
|---|---|
| 01-documentacao-agente.md | Caso de uso, persona, arquitetura e segurança |
| 02-base-conhecimento.md | Dados utilizados e estratégia de integração |
| 03-prompts.md | System Prompt, exemplos de interação e edge cases |
| 04-metricas.md | Testes e avaliação do agente |
| 05-pitch.md | Roteiro da apresentação do projeto |

## 👩‍💻 Projeto acadêmico

Projeto desenvolvido para demonstrar a aplicação de **IA Generativa em um cenário de segurança financeira**, utilizando dados mockados, uma interface conversacional e integração com um modelo de linguagem via API.


🛡️ **FraudGuard** — Segurança financeira explicada de forma simples e conversacional.
