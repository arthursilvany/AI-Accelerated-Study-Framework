# 🚀 AI-102 — Study Plan (Microsoft Learn)
## AI Accelerated Study Framework: 5 Steps per Learning Path

### 🌐 Multi-Language Support

#### Available in this repository

[English](./README.md) | [Português (Brasil)](../../../../examples/AI-102-Certification/README.md)

Official certification page:
https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-engineer/?practice-assessment-type=certification

---

## ✅ Framework Rules (apply to all courses)

- ⚡ **Energy > time**: study during your cognitive energy peak.
- ⏱️ **Pomodoro is mandatory**: 4×25 + 5 (no phone during the break).
- 🎓 **Tutor Mode is mandatory** during the Comprehension stage.
- 🧪 **Implementation is mandatory**: "there is no study without delivery".
- 📊 **Scoreboard is mandatory**: record every study session.

📊 Scoreboard:
[Study_Scoreboard_Template.xlsx](../../../../Study_Scoreboard_Template.xlsx)

---

# 1) Develop generative AI apps in Azure
⏱️ 7h 29min · 📦 8 modules
🔗 https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/

## 1️⃣ Goal
- [ ] Goal in 1 sentence: build a strong **GenAI foundation in Azure** for AI-102 and real-world scenarios.
- [ ] Practical outcome: mini GenAI app with structured prompt + minimum governance.
- [ ] Success criteria: explain the architecture + deliver a demo with README.

## 2️⃣ Resources
- [ ] Microsoft Learn (learning path above)
- [ ] Complementary documentation only if needed: Azure OpenAI / AI Foundry
- [ ] Notes repository: `/notes/generative-ai/`

## 3️⃣ Priming
- [ ] Executive summary (10-15 lines): "What is GenAI in Azure and where does it fit in AI-102?"
- [ ] Glossary (min. 10): prompt, tokens, embeddings, safety, grounding, etc.
- [ ] Guiding questions (min. 10): "when should I use X vs Y?", "what are the trade-offs?"
- [ ] Initial flashcards (min. 10)

## 4️⃣ Comprehension (Tutor Mode)
Selected tutor:
- [ ] AI (Copilot/ChatGPT/Claude)
- [ ] Expert person: ___________

Checklist:
- [ ] Explain the content at beginner, intermediate, and advanced levels
- [ ] Tutor asks **why** and **trade-off** questions
- [ ] Create a list of **anti-patterns** (min. 5)
- [ ] Create a quiz (min. 10) and review it with the tutor

Suggested prompt:
> "Act as an AI-102 expert. Ask hard questions about GenAI on Azure and critique my decisions."

## 5️⃣ Implementation
Minimum required delivery:
- [ ] 1 mini-demo (prompt + basic safety + minimal logging)
- [ ] README with architecture and decisions
- [ ] 1 prompt variation (A/B) and conclusion

---

# 2) Develop AI Agents on Azure
⏱️ 10h 21min · 📦 11 modules
🔗 https://learn.microsoft.com/training/paths/develop-ai-agents-on-azure/

## 1️⃣ Goal
- [ ] Goal: master **Agents** (orchestration, tools, flow) aligned to the exam and real-world work.
- [ ] Practical outcome: agent with tools (for example, search and data) + logging.
- [ ] Criteria: defend the architecture and limits (security, cost, reliability).

## 2️⃣ Resources
- [ ] Microsoft Learn (learning path above)
- [ ] Repository: `/notes/agents/`
- [ ] If needed: Agents/Foundry docs and observability best practices

## 3️⃣ Priming
- [ ] Summary: "What differentiates an agent from a chatbot?"
- [ ] Glossary: tools, planning, memory, routing, guardrails, etc.
- [ ] Guiding questions: "when should I use agent vs workflow?", "what is the risk of tool misuse?"
- [ ] Flashcards (min. 15)

## 4️⃣ Comprehension (Tutor Mode)
- [ ] Teach the topic to the tutor (3 levels)
- [ ] Tutor simulates a real scenario (client/production)
- [ ] Identify trade-offs: latency, cost, quality, security
- [ ] Quiz (min. 15) + review

Suggested prompt:
> "Simulate an enterprise client and force me to justify agent design and security decisions."

## 5️⃣ Implementation
Minimum required delivery:
- [ ] 1 agent with at least 2 tools
- [ ] Basic logging/telemetry
- [ ] README: architecture + limitations + next steps

---

# 3) Develop natural language solutions in Azure
⏱️ 8h 38min · 📦 10 modules
🔗 https://learn.microsoft.com/training/paths/develop-language-solutions-azure-ai/

## 1️⃣ Goal
- [ ] Goal: master **NLP solutions in Azure** covered in AI-102.
- [ ] Practical outcome: applied NLP solution (classification, extraction, analysis).
- [ ] Criteria: explain the use case + limits + cost/scale.

## 2️⃣ Resources
- [ ] Microsoft Learn (learning path above)
- [ ] Repository: `/notes/nlp/`

## 3️⃣ Priming
- [ ] Summary: "What business problems can NLP solve?"
- [ ] Glossary: entities, sentiment, summarization, classification, etc.
- [ ] Guiding questions: "when should I use classic NLP vs LLM?"
- [ ] Flashcards (min. 12)

## 4️⃣ Comprehension (Tutor Mode)
- [ ] Tutor asks for a comparison: traditional NLP vs LLM
- [ ] Tutor proposes 2 client scenarios (for example, support and compliance)
- [ ] Anti-patterns (min. 5)
- [ ] Quiz (min. 12)

Suggested prompt:
> "Question me like an architect: service choice, governance, cost, and risks."

## 5️⃣ Implementation
Minimum required delivery:
- [ ] 1 mini NLP lab (input → processing → output)
- [ ] README with use case + decisions
- [ ] Test with 3 different examples

---

# 4) Develop computer vision solutions in Azure
⏱️ 6h 35min · 📦 8 modules
🔗 https://learn.microsoft.com/training/paths/create-computer-vision-solutions-azure-ai/

## 1️⃣ Goal
- [ ] Goal: master **computer vision** in Azure aligned with AI-102.
- [ ] Practical outcome: image analysis/OCR/vision solution with clear output.
- [ ] Criteria: explain limits, accuracy, bias, cost, and latency.

## 2️⃣ Resources
- [ ] Microsoft Learn (learning path above)
- [ ] Repository: `/notes/vision/`

## 3️⃣ Priming
- [ ] Summary: "Main Vision capabilities in Azure"
- [ ] Glossary: OCR, detection, classification, confidence, etc.
- [ ] Guiding questions: "when should I use OCR vs Document Intelligence?"
- [ ] Flashcards (min. 10)

## 4️⃣ Comprehension (Tutor Mode)
- [ ] Tutor questions common errors (image quality, noise, bias)
- [ ] Tutor simulates a scenario (documents, photos, product images)
- [ ] Anti-patterns (min. 5)
- [ ] Quiz (min. 10)

Suggested prompt:
> "Act as a technical reviewer: identify risks and limitations in the vision solution."

## 5️⃣ Implementation
Minimum required delivery:
- [ ] 1 demo (input images → result)
- [ ] README with architecture + decisions
- [ ] Compare 2 approaches (for example, OCR vs DI) and conclude

---

# 5) Develop AI Information extraction solutions in Azure
⏱️ 4h 18min · 📦 5 modules
🔗 https://learn.microsoft.com/training/paths/ai-extract-information/

## 1️⃣ Goal
- [ ] Goal: master **information extraction** (documents) in Azure.
- [ ] Practical outcome: extraction pipeline with fields and validation.
- [ ] Criteria: explain accuracy, exceptions, governance, and cost.

## 2️⃣ Resources
- [ ] Microsoft Learn (learning path above)
- [ ] Repository: `/notes/information-extraction/`

## 3️⃣ Priming
- [ ] Summary: "Why is data extraction core to businesses?"
- [ ] Glossary: forms, invoices, confidence, schema, etc.
- [ ] Guiding questions: "when should I use DI vs OCR vs LLM?"
- [ ] Flashcards (min. 10)

## 4️⃣ Comprehension (Tutor Mode)
- [ ] Tutor questions reliability, human validation, and exceptions
- [ ] Create anti-patterns (min. 5)
- [ ] Quiz (min. 10)
- [ ] Defend the architecture for production

Suggested prompt:
> "Simulate an enterprise scenario with imperfect documents and force me to handle exceptions."

## 5️⃣ Implementation
Minimum required delivery:
- [ ] 1 extraction demo (document → structured fields)
- [ ] README: architecture + validation + limitations
- [ ] Test with 3 different documents

---

# ✅ Final Ready-for-Exam Checklist

- [ ] I completed the 5 Learning Paths (Microsoft Learn)
- [ ] I have **at least 5 demos** (one per course)
- [ ] I have a README per lab with architecture and decisions
- [ ] I used Tutor Mode in all domains
- [ ] Practice assessment consistently above 85%
- [ ] Scoreboard filled in for all sessions

---