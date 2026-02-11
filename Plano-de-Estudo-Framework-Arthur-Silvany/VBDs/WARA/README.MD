# 📘 Plano de Estudo — Framework de Estudo Cloud Solution Architect  
## Well-Architected Reliability Assessment (WARA)  
**Versão oficial para GitHub**

---

## 🧭 Sumário

- [🎯 1. Objetivo](#-1-objetivo)  
- [📚 2. Pesquisa de Recursos (Resources)](#-2-pesquisa-de-recursos-resources)  
- [🧠 3. Priming — Preparação (30–50 min)](#-3-priming--preparação--3050-min)  
- [📘 4. Compreensão (Understanding)](#-4-compreensão-understanding)  
- [🚀 5. Implementação — Fase Prática](#-5-implementação-fase-prática)  
- [🗓️ 6. Cronograma Sugerido (2 Semanas)](#-6-cronograma-sugerido-2-semanas)  
- [📁 7. Artefatos do Estudo](#-7-artefatos-do-estudo)  
- [🥇 8. Regras de Ouro do Framework Cloud Solution Architect](#-8-regras-de-ouro-do-framework-arthur-silvany)  
- [🔗 9. Referências Oficiais WARA](#-9-referências-oficiais-wara)

---

## 🎯 1. Objetivo

Este plano permite que **Cloud Solution Architect** domine a entrega completa do **Well-Architected Reliability Assessment (WARA)**, aplicando o **Framework de Estudo Cloud Solution Architect** para:

- Reduzir em **~70%** o tempo de estudo  
- Aumentar substancialmente a **retenção e aplicação prática**

Todo o conteúdo é baseado diretamente no documento oficial:  
**Well-Architected Reliability Assessment – VBD**

### 🎯 Objetivos específicos

- Dominar o pilar **Reliability** do **Well-Architected Framework**
- Entender profundamente a **metodologia de entrega do WARA**  
  (32h + pré e pós-engajamento)
- Utilizar com fluência as ferramentas oficiais:
  - APRL  
  - CxObserve  
  - Advisor Reliability Workbook  
  - WARA Tooling  
  - CAPE (Lighthouse)  
  - Service Health / IcM / OneSupport  

### 📦 Entregar todas as fases do WARA

- Pre-engagement  
- Scoping  
- Expert Analysis  
- Discovery Workshop  
- Technical Alignment  
- Generate Reports  
- Internal Review  
- Closeout  
- Post-engagement  

---

## 📚 2. Pesquisa de Recursos (Resources)

Etapa de consolidação de **todo o material necessário** para iniciar o estudo.

### 🔧 Ferramentas Microsoft usadas

- **Microsoft Copilot (Edge + M365)** — resumos, decomposição e extração de conhecimento  
- **OneNote + Copilot** — mapas mentais e organização estruturada  
- **Teams** — canal oficial WARA + @Reliability/Resiliency v-team  
- **Stream** — gravações do Deep Dive WARA  
- **Excel + Copilot** — análise do `Expert-Analysis.xlsx`  
- **PowerPoint + Copilot** — criação de narrativas executivas  
- **Visio** — diagramas arquiteturais  
- **Viva Learning** — cursos WAF, Mission-Critical e Resiliency  
- **SharePoint / OneDrive** — organização de kits e relatórios  

### 📦 Conteúdo oficial WARA

- IP Kit oficial — https://aka.ms/ipkit-wara  
- Delivery Guide — fluxo completo da entrega  
- Learning Path oficial  
- Self-Accreditation  
- Teams – WARA — https://aka.ms/AzureInfraVBDTeams/reliability  
- APRL — https://aka.ms/aprl  
- CxObserve — https://cxp.azure.com  
- WARA Tooling — https://azure.github.io/Azure-Proactive-Resiliency-Library-v2/tools  
- Reliability Checklist (WAF)  
- Office Hours + Deep Dives (Stream)  

---

## 🧠 3. Priming — Preparação (30–50 min)

Objetivo: **preparar o cérebro antes do estudo profundo**.

### ✔️ 1. Resumo executivo com Copilot

Pedir ao Copilot para resumir:
- Objetivo do WARA  
- Etapas da entrega  
- Ferramentas exigidas (APRL, CxObserve, WARA Tooling)  
- Requisitos do workload  
- O que caracteriza **High Impact**

### ✔️ 2. Deep Dive (Stream — apenas partes críticas)

- Overview da entrega  
- Ferramentas  
- Discovery Workshop  
- Expert Analysis  
- Workload Review no CxObserve  

### ✔️ 3. Flashcards (OneNote + Copilot)

- SLA / SLO / SLI  
- RTO / RPO  
- Zonal vs Regional redundancy  
- APRL × Advisor × CxObserve  
- Etapas da entrega  

### ✔️ 4. Quiz inicial (Forms)

10 perguntas rápidas sobre:
- Definição de workload  
- Falha Zonal vs Regional  
- WARA Tooling  
- Alto impacto vs Médio  
- Acesso via Lighthouse  

---

## 📘 4. Compreensão (Understanding)

Estudo profundo **em camadas**, seguindo o Framework Cloud Solution Architect.

### 4.1 Fundamentos de Reliability (WAF)

#### Design for Business Requirements
- SLA / SLO / SLI  
- RPO / RTO  
- Critical flows  
- Failure mode analysis  

#### Design for Resilience
- Redundancy  
- High Availability  
- Availability Zones  
- Replication  
- Failover  
- Regional redundancy  
- Scalability patterns  

#### Design for Recovery
- Health checks  
- Auto-healing  
- Disaster Recovery  
- DR drills  
- Backup posture  

#### Design for Operations
- Monitoring  
- Alerting  
- Logging  
- Diagnostics  
- Observabilidade  

---

### 4.2 Processos Oficiais do WARA (9 fases)

1. **Pre-engagement**  
   - Internal scoping  
   - Definição de workload  
   - Coleta de subscriptions  
   - Preparar CAPE / Lighthouse  

2. **Scoping Call**  
   - Confirmar workload  
   - Validar stakeholders e tags  
   - Solicitar diagramas  
   - Revisar pré-requisitos  

3. **Expert Analysis (~12h)**  
   - Rodar WARA Tooling  
   - Gerar `Expert-Analysis.xlsx`  
   - Avaliar:
     - High Impact  
     - Falha Zonal / Regional  
     - Service Retirement  
     - Platform Issues  
     - Support Requests  

4. **Discovery Workshop (3–6h)**  
   - Entrevistas  
   - Arquitetura  
   - Fluxos críticos  
   - Dependências  
   - Riscos  

5. **Technical Alignment (~10h)**  
   - Resolver pendências  
   - Validar High Impact  
   - Ajustar prioridades  

6. **Generate & Customize Reports**  
   - Findings Report (Excel)  
   - Technical Summary (PPTX)  
   - Baseline Metrics  
   - CSVs (Zones / ExpressRoute)  

7. **Internal Review**  
   - CSAM + EDE/DE/STA  
   - Validação de riscos  
   - Definir Job 2  

8. **Closeout Meeting**  
   - Entrega executiva  
   - Recomendações High/Medium  
   - Timelines  

9. **Post-engagement**  
   - Revisão quinzenal de High Impact  
   - Encaminhar outros VBDs  
   - Finalizar CAPE  

---

### 4.3 Ferramentas Essenciais

- **WARA Tooling** — Collector, Analyzer, Reports  
- **APRL** — validação manual e recomendações não automatizadas  
- **CxObserve** — Scorecards, Service Health, Workload Review  
- **Advisor Reliability Workbook** — AZ gaps, depreciações  

---

### 4.4 IA Microsoft Integrada

- **Copilot** — explicações, resumos, comparativos  
- **PowerPoint** — narrativa executiva  
- **Excel** — análise por impacto  
- **OneNote** — base de conhecimento pessoal  

---

## 🚀 5. Implementação — Fase Prática

- **Simulação 1:** WARA Tooling  
- **Simulação 2:** Discovery Workshop  
- **Simulação 3:** Relatórios (Excel + PPTX)  
- **Simulação 4:** CxObserve + Advisor  

---

## 🗓️ 6. Cronograma Sugerido (2 Semanas)

### Semana 1

| Dia | Atividade |
|----|----------|
| 1 | Priming + Flashcards |
| 2 | WAF Reliability |
| 3 | Pre-engagement |
| 4 | Expert Analysis I |
| 5 | Expert Analysis II |

### Semana 2

| Dia | Atividade |
|----|----------|
| 6 | Discovery Workshop |
| 7 | Technical Alignment |
| 8 | Relatórios (Excel + PPTX) |
| 9 | Workload Review |
| 10 | Closeout + Revisão Geral |

---

## 📁 7. Artefatos do Estudo

- `Expert-Analysis.xlsx`  
- `Assessment-Findings-Report.xlsx`  
- `Technical-Summary-Report.pptx`  
- Zone Resiliency CSV  
- ExpressRoute Resiliency CSV  
- Workload Review publicado  
- Plano de remediação High / Medium  

---

## 🥇 8. Regras de Ouro do Framework Cloud Solution Architect

- Objetivo claro sempre primeiro  
- Nunca pular o Priming  
- IA Microsoft em tudo que for possível  
- Estudo em camadas  
- Interleaving diário:
  - Ferramentas  
  - Reliability  
  - Processo  
- Revisão diária (OneNote)  
- **70/30 → 70% prática, 30% teoria**

---

## 🔗 9. Referências Oficiais WARA

- https://aka.ms/ipkit-wara  
- https://aka.ms/aprl  
- https://cxp.azure.com  
- https://aka.ms/AzureInfraVBDTeams/reliability  
- https://learn.microsoft.com/azure/well-architected/reliability/checklist  
- https://azure.github.io/Azure-Proactive-Resiliency-Library-v2/tools
```
