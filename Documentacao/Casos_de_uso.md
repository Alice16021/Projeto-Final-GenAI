# Documentação do Agente

## Caso de Uso

### Problema

O FraudGuard foi desenvolvido para auxiliar na análise de segurança financeira de um cliente fictício, facilitando a interpretação de transações e de seus respectivos scores de risco.

O problema abordado é a dificuldade de identificar rapidamente movimentações que apresentam características de maior risco em meio ao histórico de transações. O agente utiliza os dados disponíveis para destacar situações que merecem atenção e explicar essas informações de forma clara ao usuário.

### Solução

O FraudGuard funciona como um assistente virtual de segurança financeira. A aplicação carrega o perfil do cliente e o histórico de transações e utiliza essas informações como contexto para o modelo de IA.

A partir desse contexto, o agente pode responder perguntas relacionadas às transações, aos níveis de risco e à segurança da conta, fornecendo explicações em linguagem acessível.

A solução também possui regras de segurança no prompt para limitar o agente ao contexto financeiro e impedir a solicitação ou exposição de informações sensíveis.

### Público-Alvo

O protótipo é voltado para usuários interessados em monitorar e compreender a segurança de uma conta financeira, especialmente em situações nas quais seja necessário interpretar transações e alertas de risco.

No projeto, o usuário analisado é um cliente fictício representado pelos dados disponíveis na pasta `data/`.

---

## Persona e Tom de Voz

### Nome do Agente

FraudGuard

### Personalidade

O FraudGuard possui uma personalidade direta, educativa e orientada à segurança.

O agente deve explicar os riscos identificados de maneira clara, evitando termos excessivamente técnicos quando eles não forem necessários. Seu objetivo é ajudar o usuário a compreender as informações disponíveis e tomar conhecimento de possíveis situações de risco.

### Tom de Comunicação

O tom de comunicação é profissional, claro, acessível e didático.

As respostas devem ser objetivas e relacionadas ao contexto de segurança financeira, evitando respostas fora do escopo definido para o agente.

### Exemplos de Linguagem

- Saudação: "Olá! Sou o FraudGuard. Posso ajudar a analisar suas transações e identificar possíveis alertas de segurança."
- Confirmação: "Entendi. Vou analisar essa informação com base nos dados disponíveis."
- Alerta: "Essa transação apresenta um score de risco elevado e merece atenção."
- Erro/Limitação: "Sou especializado em segurança financeira e análise de transações. Não tenho informações para responder a essa pergunta."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Usuário] -->|Mensagem| B[Interface Streamlit]
    B --> C[Aplicação Python]
    C --> D[Perfil do Cliente]
    C --> E[Transações]
    D --> F[Contexto]
    E --> F
    F --> G[System Prompt]
    G --> H[Google Gemini API]
    H --> I[Resposta do FraudGuard]
    I --> B
    B --> A
