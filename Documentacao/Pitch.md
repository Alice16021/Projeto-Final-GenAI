# Pitch (3 minutos)

## Roteiro Sugerido

### 1. O Problema (30 seg)

O FraudGuard foi criado para lidar com a dificuldade de interpretar transações financeiras e identificar movimentações que apresentam maior risco.

Em um histórico com várias operações, pode ser difícil perceber rapidamente quais transações merecem mais atenção e entender o significado de seus scores de risco.

---

### 2. A Solução (1 min)

O FraudGuard é um assistente de segurança financeira desenvolvido em Python e Streamlit.

A aplicação utiliza dados fictícios armazenados localmente, incluindo o perfil do cliente e o histórico de transações com informações de risco.

Esses dados são utilizados como contexto para o Google Gemini, que funciona como o modelo de inteligência artificial do sistema.

O usuário pode conversar com o FraudGuard e fazer perguntas sobre as transações, os riscos identificados e a segurança da conta.

Também foram definidas regras no System Prompt para impedir o agente de solicitar ou expor informações sensíveis e para limitar as respostas ao contexto de segurança financeira.

---

### 3. Demonstração (1 min)

Durante a demonstração, será apresentada a interface do FraudGuard funcionando em um navegador.

Será mostrado:

1. O carregamento do cliente fictício;
2. A interação com o chatbot;
3. Uma pergunta sobre uma transação de risco;
4. A identificação de uma movimentação com score elevado;
5. Uma pergunta sobre uma transação não reconhecida;
6. O comportamento do agente diante de uma pergunta fora do escopo.

A demonstração mostrará também que o agente mantém o contexto da conversa entre as mensagens.

---

### 4. Diferencial e Impacto (30 seg)

O principal diferencial do FraudGuard é combinar dados estruturados de transações com IA Generativa em uma interface simples de conversação.

A solução transforma informações técnicas, como scores de risco, em respostas mais fáceis de interpretar pelo usuário.

Como impacto, o projeto demonstra como IA Generativa pode ser utilizada como camada de apoio à segurança financeira, auxiliando na compreensão de alertas e movimentações suspeitas.

---

## Checklist do Pitch

- [x] Duração máxima de 3 minutos
- [x] Problema claramente definido
- [x] Solução demonstrada na prática
- [x] Diferencial explicado
- [ ] Áudio e vídeo com boa qualidade

---
