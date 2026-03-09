# 🚀 AI-102 — Plano de Estudo (Microsoft Learn)  
## AI Accelerated Study Framework: 5 Etapas por Learning Path

Página oficial da certificação:  
https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-engineer/?practice-assessment-type=certification

---

## ✅ Regras do Framework (aplicáveis a todos os cursos)

- ⚡ **Energia > tempo**: estude no seu pico de energia cognitiva.
- ⏱️ **Pomodoro obrigatório**: 4×25 + 5 (sem celular no descanso).
- 🎓 **Tutor Mode obrigatório** na etapa de Compreensão.
- 🧪 **Implementação obrigatória**: “não existe estudo sem entrega”.
- 📊 **Scoreboard obrigatório**: registrar cada sessão de estudo.

📊 Scoreboard:  
[Carreira_Cloud_Study_Scoreboard_Template.xlsx](Carreira_Cloud_Study_Scoreboard_Template.xlsx)

---

# 1) Develop generative AI apps in Azure  
⏱️ 7h 29min · 📦 8 módulos  
🔗 https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/

## 1️⃣ Objetivo
- [ ] Objetivo em 1 frase: construir base sólida de **GenAI no Azure** para AI-102 e casos reais.
- [ ] Resultado prático: mini-app GenAI com prompt estruturado + governança mínima.
- [ ] Critério de sucesso: explicar arquitetura + entregar demo com README.

## 2️⃣ Recursos
- [ ] Microsoft Learn (Learning Path acima)
- [ ] Documentação complementar (somente se necessário): Azure OpenAI / AI Foundry
- [ ] Repositório de anotações: `/notes/generative-ai/`

## 3️⃣ Priming
- [ ] Resumo executivo (10–15 linhas): “O que é GenAI no Azure e onde entra na AI-102?”
- [ ] Glossário (mín. 10): prompt, tokens, embeddings, safety, grounding, etc.
- [ ] Perguntas-guia (mín. 10): “quando usar X vs Y?”, “trade-offs?”
- [ ] Flashcards iniciais (mín. 10)

## 4️⃣ Compreensão (Tutor Mode)
Tutor escolhido:
- [ ] IA (Copilot/ChatGPT/Claude)
- [ ] Pessoa expert: ___________

Checklist:
- [ ] Explicar o conteúdo em nível básico, intermediário e avançado
- [ ] Tutor faz perguntas de **por quê** e **trade-offs**
- [ ] Criar lista de **antipadrões** (mín. 5)
- [ ] Criar quiz (mín. 10) e revisar com tutor

Prompt sugerido:
> “Aja como especialista AI-102. Faça perguntas difíceis sobre GenAI no Azure e critique minhas decisões.”

## 5️⃣ Implementação
Entrega mínima (obrigatória):
- [ ] 1 mini-demo (prompt + segurança básica + logging mínimo)
- [ ] README com arquitetura e decisões
- [ ] 1 variação do prompt (A/B) e conclusão


---

# 2) Develop AI Agents on Azure  
⏱️ 10h 21min · 📦 11 módulos  
🔗 https://learn.microsoft.com/training/paths/develop-ai-agents-on-azure/

## 1️⃣ Objetivo
- [ ] Objetivo: dominar **Agents** (orquestração, ferramentas, fluxo) alinhado ao exame e ao mundo real.
- [ ] Resultado prático: agente com ferramentas (ex: busca, dados) + logging.
- [ ] Critério: defender arquitetura e limites (segurança, custo, confiabilidade).

## 2️⃣ Recursos
- [ ] Microsoft Learn (Learning Path acima)
- [ ] Repositório: `/notes/agents/`
- [ ] Se necessário: docs de Agents/Foundry e boas práticas de observabilidade

## 3️⃣ Priming
- [ ] Resumo: “O que diferencia agente de chatbot?”
- [ ] Glossário: tools, planning, memory, routing, guardrails, etc.
- [ ] Perguntas-guia: “quando usar agent vs workflow?”, “risco de tool misuse?”
- [ ] Flashcards (mín. 15)

## 4️⃣ Compreensão (Tutor Mode)
- [ ] Ensinar o tema para o tutor (3 níveis)
- [ ] Tutor simula cenário real (cliente/produção)
- [ ] Identificar trade-offs: latência, custo, qualidade, segurança
- [ ] Quiz (mín. 15) + revisão

Prompt sugerido:
> “Simule um cliente corporativo e me force a justificar decisões de agent design e segurança.”

## 5️⃣ Implementação
Entrega mínima:
- [ ] 1 agente com pelo menos 2 tools
- [ ] Logging/telemetria básica
- [ ] README: arquitetura + limitações + próximos passos


---

# 3) Develop natural language solutions in Azure  
⏱️ 8h 38min · 📦 10 módulos  
🔗 https://learn.microsoft.com/training/paths/develop-language-solutions-azure-ai/

## 1️⃣ Objetivo
- [ ] Objetivo: dominar soluções de **NLP no Azure** cobradas na AI-102.
- [ ] Resultado prático: solução NLP aplicada (classificação, extração, análise).
- [ ] Critério: explicar cenário de uso + limites + custo/escala.

## 2️⃣ Recursos
- [ ] Microsoft Learn (Learning Path acima)
- [ ] Repositório: `/notes/nlp/`

## 3️⃣ Priming
- [ ] Resumo: “Que problemas NLP resolvem em negócios?”
- [ ] Glossário: entities, sentiment, summarization, classification, etc.
- [ ] Perguntas-guia: “quando NLP clássico vs LLM?”
- [ ] Flashcards (mín. 12)

## 4️⃣ Compreensão (Tutor Mode)
- [ ] Tutor pede comparação: NLP tradicional vs LLM
- [ ] Tutor propõe 2 cenários de cliente (ex: suporte, compliance)
- [ ] Antipadrões (mín. 5)
- [ ] Quiz (mín. 12)

Prompt sugerido:
> “Me questione como arquiteto: escolha de serviço, governança, custo e riscos.”

## 5️⃣ Implementação
Entrega mínima:
- [ ] 1 mini-lab NLP (entrada → processamento → saída)
- [ ] README com caso de uso + decisões
- [ ] Teste com 3 exemplos diferentes


---

# 4) Develop computer vision solutions in Azure  
⏱️ 6h 35min · 📦 8 módulos  
🔗 https://learn.microsoft.com/training/paths/create-computer-vision-solutions-azure-ai/

## 1️⃣ Objetivo
- [ ] Objetivo: dominar **visão computacional** no Azure alinhada à AI-102.
- [ ] Resultado prático: análise de imagem/OCR/visão com output claro.
- [ ] Critério: explicar limites, precisão, vieses, custo e latência.

## 2️⃣ Recursos
- [ ] Microsoft Learn (Learning Path acima)
- [ ] Repositório: `/notes/vision/`

## 3️⃣ Priming
- [ ] Resumo: “Principais capacidades de Vision no Azure”
- [ ] Glossário: OCR, detection, classification, confidence, etc.
- [ ] Perguntas-guia: “quando OCR vs Document Intelligence?”
- [ ] Flashcards (mín. 10)

## 4️⃣ Compreensão (Tutor Mode)
- [ ] Tutor questiona erros comuns (qualidade da imagem, ruído, bias)
- [ ] Tutor simula cenário (documentos, fotos, imagens de produto)
- [ ] Antipadrões (mín. 5)
- [ ] Quiz (mín. 10)

Prompt sugerido:
> “Aja como revisor técnico: identifique riscos e limitações na solução de visão.”

## 5️⃣ Implementação
Entrega mínima:
- [ ] 1 demo (input imagens → resultado)
- [ ] README com arquitetura + decisões
- [ ] Comparar 2 abordagens (ex: OCR vs DI) e concluir


---

# 5) Develop AI Information extraction solutions in Azure  
⏱️ 4h 18min · 📦 5 módulos  
🔗 https://learn.microsoft.com/training/paths/ai-extract-information/

## 1️⃣ Objetivo
- [ ] Objetivo: dominar **extração de informação** (documentos) no Azure.
- [ ] Resultado prático: pipeline de extração com campos e validação.
- [ ] Critério: explicar acurácia, exceções, governança e custo.

## 2️⃣ Recursos
- [ ] Microsoft Learn (Learning Path acima)
- [ ] Repositório: `/notes/information-extraction/`

## 3️⃣ Priming
- [ ] Resumo: “Por que extração de dados é core em empresas?”
- [ ] Glossário: forms, invoices, confidence, schema, etc.
- [ ] Perguntas-guia: “quando DI vs OCR vs LLM?”
- [ ] Flashcards (mín. 10)

## 4️⃣ Compreensão (Tutor Mode)
- [ ] Tutor questiona: confiabilidade, validação humana, exceções
- [ ] Criar antipadrões (mín. 5)
- [ ] Quiz (mín. 10)
- [ ] Defender arquitetura para produção

Prompt sugerido:
> “Simule um cenário corporativo com documentos imperfeitos e me force a lidar com exceções.”

## 5️⃣ Implementação
Entrega mínima:
- [ ] 1 demo extração (documento → campos estruturados)
- [ ] README: arquitetura + validação + limitações
- [ ] Testar com 3 documentos diferentes


---

# ✅ Checklist Final de Pronto para Prova

- [ ] Completei os 5 Learning Paths (Microsoft Learn)
- [ ] Tenho **pelo menos 5 demos** (uma por curso)
- [ ] Tenho README por lab com arquitetura e decisões
- [ ] Fiz Tutor Mode em todos os domínios
- [ ] Practice assessment consistente em 85%+
- [ ] Scoreboard preenchido em todas as sessões

---

