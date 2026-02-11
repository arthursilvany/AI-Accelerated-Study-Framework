
# Plano de Estudo — Framework de Estudo Arthur Silvany
## Azure Landing Zone VBD — Assessment

**Documento base**: [Azure Landing Zone VBD - Assessment.docx](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1&EntityRepresentationId=8ec0cf7a-b089-4814-a9e8-77c01c4629e8) [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)  
**Impacto esperado**: reduzir tempo de estudo em **60–70%**, com maior retenção usando Copilot e ferramentas Microsoft de IA.

---

## Sumário
1. Objetivo (Goal)
2. Pesquisa de Recursos (Resources)
3. Priming
4. Compreensão (Understanding)
5. Implementação (Implementation)
6. Cronograma sugerido (2 semanas)
7. Artefatos do estudo
8. Regras de ouro para acelerar
9. Referências (corporativas)

---

## 1) Objetivo (Goal)
**Resultado desejado**: planejar e conduzir uma avaliação **Azure Landing Zone (ALZ)** — formato **1‑Dia** ou **3‑Dias** — apresentar achados e recomendações e planejar próximos passos, incluindo **resiliência multi‑região** e, quando aplicável, **Sovereign Landing Zone**. [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)

**Metas específicas**
- Entender os **Key Objectives** (CAF, gaps e roadmap). [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)
- Dominar as **8 design areas** (Billing/Entra Tenant, Identity & Access, Network, Resource Organization, Security, Management, Governance, Platform Automation & DevOps) e explicar usando o **ALZ Visio**. [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)
- Conduzir **Pre‑Scoping**, **Scoping**, **Kickoff**, **Delivery**, **Reporting** e **Closeout** com templates do **IP Kit** e o **checklist** oficial. [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)
- Avaliar **multi‑região** (DR/HA, compliance, desempenho global) e **Sovereign Landing Zone** (políticas). [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)
- Estimar custos com **Azure Pricing Calculator** e componentes típicos. [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)

---

## 2) Pesquisa de Recursos (Resources)
**Ferramentas Microsoft**
- **Microsoft Copilot (M365)**: busca/explicações de conteúdo do tenant (SharePoint/OneDrive/Teams) e docs Microsoft.
- **SharePoint/OneDrive**: pasta `ALZ VBD Study` com IP Kit, Visio, gravações e anotações.
- **Teams + Stream**: acessar **VBD Deep Dive – ALZ Assessment** (vídeo/transcrição). [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)[2](https://microsoft.sharepoint.com/teams/FY23AzureCoreSolutionPlay-MigrateModernize/Shared%20Documents/Forms/DispForm.aspx?ID=675&web=1)
- **Visio**: abrir o **ALZ Visio Diagram** (GitHub público). [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)
- **Viva Learning**: trilhas de **CAF/ALZ**.
- **Copilot Studio**: criar um **bot de estudo** com base nos artefatos do **IP Kit**.

**Materiais principais**
- **IP Kit (Trainer.zip)** com templates/checklist. [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)
- **Canal de Teams dos ALZ VBDs** (marcar **@ALZ v‑team**). [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)[3](https://teams.microsoft.com/l/message/19:903f2517b8224941aec29b3bbd9fc1e5@thread.skype/1702402209318?tenantId=72f988bf-86f1-41af-91ab-2d7cd011db47&groupId=c7087e72-0dd8-41bf-a454-4aaad4a37753&parentMessageId=1702402209318&teamName=IP%20Forum%3A%20Cloud%20Infra%20and%20Management&channelName=Premier%20-%20CAF%20Azure%20Landing%20Zone&createdTime=1702402209318)
- **Checklist oficial** (_review_checklist.xlsm/xlsx_). [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)
- **Templates de Apresentação (PPTX)** para Scoping/Kickoff/Closeout (ex.: [Azure Landing Zone - Assessment - Scoping.pptx](https://microsoft.sharepoint.com/teams/ASDIPDevelopment/AzureCloudAI/SP1%20VBD/ALZ/Development/2.%20ALZ%20Assessment/1.%20Scoping/Azure%20Landing%20Zone%20-%20Assessment%20-%20Scoping.pptx?web=1&EntityRepresentationId=fa97a9a2-c511-461e-acf6-96dfa4e91800), [Azure Landing Zones - Assessment - Presentation.pptx](https://microsoft.sharepoint.com/teams/ASDIPDevelopment/AzureCloudAI/SP1%20VBD/ALZ/Development/2.%20ALZ%20Assessment/3.%20Engagement/Customer%20Report%20examples/Contoso/Azure%20Landing%20Zones%20-%20Assessment%20-%20Presentation.pptx?web=1&EntityRepresentationId=acc75f5d-2a0c-4d8e-a5ab-d7c9cc1beae4)). [4](https://microsoft.sharepoint.com/teams/ASDIPDevelopment/AzureCloudAI/SP1%20VBD/ALZ/Development/2.%20ALZ%20Assessment/1.%20Scoping/Azure%20Landing%20Zone%20-%20Assessment%20-%20Scoping.pptx?web=1)[5](https://microsoft.sharepoint.com/teams/ASDIPDevelopment/AzureCloudAI/SP1%20VBD/ALZ/Development/2.%20ALZ%20Assessment/3.%20Engagement/Customer%20Report%20examples/Contoso/Azure%20Landing%20Zones%20-%20Assessment%20-%20Presentation.pptx?web=1)
- **Guia VBD (Engineering Hub)** — páginas de **Assessment 1‑Day** e **Deployment Delivery**. [6](https://eng.ms/docs/microsoft-customer-partner-solutions-mcaps-core/customer-experience-and-support/customer-success/azure-core/resource-center/alz/alza_1day)[7](https://eng.ms/docs/microsoft-customer-partner-solutions-mcaps-core/customer-experience-and-support/customer-success/azure-core/resource-center/alz/deployment/alzd_delivery)
- **Azure Pricing Calculator** (template de estimativa). [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)
- **Práticas de CPE Survey** (slide e orientação). [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)

---

## 3) Priming (30–60 min)
- **Copilot no Word**: gerar **resumo executivo** por seção do documento base ([Azure Landing Zone VBD - Assessment.docx](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1&EntityRepresentationId=8ec0cf7a-b089-4814-a9e8-77c01c4629e8)). [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)
- **Visio + Copilot**: revisar o **ALZ Visio** e listar conceitos/fluxos por design area. [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)
- **Stream**: ativar transcrição do **VBD Deep Dive** e ler só títulos/seções. [2](https://microsoft.sharepoint.com/teams/FY23AzureCoreSolutionPlay-MigrateModernize/Shared%20Documents/Forms/DispForm.aspx?ID=675&web=1)
- **Forms**: criar **quiz** inicial (10 perguntas) sobre objetivos, fases, multi‑região e soberania (conteúdo do IP Kit). [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)
- **Azure AI Speech**: gerar **podcast** curto (5–10 min) com definições e exemplos.

---

## 4) Compreensão (Understanding) — aprender em camadas
### 4.1 Arquitetura e Framework
- Estudar **CAF Overview** e **ALZ conceptual architecture**; revisitar **Key Objectives**. [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)
- Usar **ALZ Visio** para explicar dependências por design area (mapas mentais com Copilot). [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)

### 4.2 Processo de Entrega
- **Pre‑Scoping / Scoping**: perguntas‑guia, escopo, agenda e pré‑requisitos (templates do **IP Kit**: Scoping/Kickoff/Closeout). [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)[4](https://microsoft.sharepoint.com/teams/ASDIPDevelopment/AzureCloudAI/SP1%20VBD/ALZ/Development/2.%20ALZ%20Assessment/1.%20Scoping/Azure%20Landing%20Zone%20-%20Assessment%20-%20Scoping.pptx?web=1)[5](https://microsoft.sharepoint.com/teams/ASDIPDevelopment/AzureCloudAI/SP1%20VBD/ALZ/Development/2.%20ALZ%20Assessment/3.%20Engagement/Customer%20Report%20examples/Contoso/Azure%20Landing%20Zones%20-%20Assessment%20-%20Presentation.pptx?web=1)
- **Delivery**: praticar o **checklist** (macros, filtros por Design Area, status/comentários, “More Info”). [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)
- **Reporting**: compilar achados → **Executive Summary** (PPTX do **IP Kit**). [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)
- **Closeout**: roteiro do meeting, **CPE Survey** e envio de **PDF** + **_review_checklist.xlsx_**. [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)

### 4.3 Resiliência, Multi‑Região e Soberania
- **Multi‑Região**: avaliar DR/HA, desempenho global, compliance e data sovereignty; recomendações de melhoria. [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)
- **Sovereign Landing Zone**: estudar a variante, **Policy Portfolio** e aba de soberania no checklist (ver guias no Engineering Hub / docs Microsoft). [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)

### 4.4 Prática com IA Microsoft
- **Excel + Copilot**: explicar colunas do **review_checklist** e gerar filtros por prioridade/design area. [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)
- **PowerPoint + Copilot**: montar slides de diagnóstico e **roadmap** com base em um cenário.
- **VS Code + GitHub Copilot**: criar exemplos **Bicep/ARM**, **Policy** e automações de plataforma (RBAC, tags, policy assignments) e **scripts Azure CLI**.
- **Teams + Whiteboard**: simular entrevistas por design area; Copilot no Teams captura **notas e ações**.

---

## 5) Implementação (Implementation)
### 5.1 Simulação “1‑Dia”
- **Kickoff curto** + **checklist filtrado** (ex.: Network/Connectivity). [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)
- **Executive Summary** e **Closeout** com recomendações focadas e impactos na arquitetura. [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)
- **Entregáveis**: _Azure Landing Zone Assessment – Presentation.pdf_ e _review_checklist.xlsx_. [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)

### 5.2 Simulação “3‑Dias”
- Agenda flexível por blocos, com tempo dedicado para **preparar entregáveis** antes do closeout. [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)

### 5.3 Estimativa de Custos
- **Azure Pricing Calculator** + template; variar região/horas/escala e incluir componentes (Entra ID, vWAN, VPN/ER Gateway, Firewall, DDoS, Bastion, Defender for Cloud, Monitor/Sentinel, Automation, Backup, Site Recovery). [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)
- **Excel/Power BI + Copilot**: consolidar cenários e comparar faixas de custo.

### 5.4 Encerramento e CPE
- Preparar **slide** e mensagem de encerramento do **CPE Survey**. [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)

---

## 6) Cronograma sugerido (2 semanas, interleaving)
**Semana 1**  
- Dia 1: Priming (resumo + quiz + Visio + podcast). [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)  
- Dia 2: Arquitetura/CAF. [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)  
- Dia 3: Processo (Pre‑Scoping/Scoping/Kickoff). [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)  
- Dia 4: Checklist (prática guiada). [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)  
- Dia 5: Multi‑Região/Soberania. [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)

**Semana 2**  
- Dias 6–7: Simulação 1‑Dia (um design area). [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)  
- Dias 8–9: Simulação 3‑Dias (todas as áreas). [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)  
- Dia 10: Custos + Closeout (CPE). [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)

---

## 7) Artefatos do estudo
- **OneNote + Copilot**: caderno “ALZ Study” por design area e fase.  
- **Visio**: diagramas por cenário (single region, active‑active, active‑passive, sovereign).  
- **PowerPoint**: Kickoff e Closeout conforme IP Kit (ex.: [Azure Landing Zones - Assessment - Presentation.pptx](https://microsoft.sharepoint.com/teams/ASDIPDevelopment/AzureCloudAI/SP1%20VBD/ALZ/Development/2.%20ALZ%20Assessment/3.%20Engagement/Customer%20Report%20examples/Contoso/Azure%20Landing%20Zones%20-%20Assessment%20-%20Presentation.pptx?web=1&EntityRepresentationId=acc75f5d-2a0c-4d8e-a5ab-d7c9cc1beae4)). [5](https://microsoft.sharepoint.com/teams/ASDIPDevelopment/AzureCloudAI/SP1%20VBD/ALZ/Development/2.%20ALZ%20Assessment/3.%20Engagement/Customer%20Report%20examples/Contoso/Azure%20Landing%20Zones%20-%20Assessment%20-%20Presentation.pptx?web=1)  
- **Excel/Checklist**: _review_checklist_ com filtros e status por item. [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)  
- **Excel/Power BI**: planilha de custos com hipóteses por componente.  
- **Forms**: pré‑teste e pós‑teste.  
- **Teams/Stream**: gravações de simulações e transcrições do Deep Dive. [2](https://microsoft.sharepoint.com/teams/FY23AzureCoreSolutionPlay-MigrateModernize/Shared%20Documents/Forms/DispForm.aspx?ID=675&web=1)

---

## 8) Regras de ouro para acelerar
- **Aprender em camadas**: visão geral → detalhes → casos → prática.  
- **Interleaving diário**: alternar blocos (arquitetura, processo, checklist).  
- **Foco em energia**: estudar no horário de maior energia.  
- **IA Microsoft em tudo**: Copilot para resumos/transformações; **Azure AI Speech** para áudio; **Visio** para visual; **GitHub Copilot** para código; **Power Automate** para organização; **Viva Learning** para trilhas.

---

## 9) Referências (corporativas)
- **IP Kit (Trainer.zip)** — materiais e templates: [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)  
- **Canal de Teams ALZ VBDs** (usar **@ALZ v‑team**): [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)  
- **ALZ Visio Diagram** (GitHub público): [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)  
- **Checklist oficial** (review_checklist): [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)  
- **Gravação VBD Deep Dive – ALZ Assessment** (Stream): [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)[2](https://microsoft.sharepoint.com/teams/FY23AzureCoreSolutionPlay-MigrateModernize/Shared%20Documents/Forms/DispForm.aspx?ID=675&web=1)  
- **Guias no Engineering Hub** (Assessment/Deployment): [6](https://eng.ms/docs/microsoft-customer-partner-solutions-mcaps-core/customer-experience-and-support/customer-success/azure-core/resource-center/alz/alza_1day)[7](https://eng.ms/docs/microsoft-customer-partner-solutions-mcaps-core/customer-experience-and-support/customer-success/azure-core/resource-center/alz/deployment/alzd_delivery)  
- **Azure Pricing Calculator + Template**: [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)  
- **CPE Survey (slide/práticas)**: [1](https://microsoft-my.sharepoint.com/personal/arsilvan_microsoft_com/Documents/Desktop/Azure%20Landing%20Zone%20VBD%20-%20Assessment.docx?web=1)

---

