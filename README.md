# AI Sales Enablement Analyzer

An enterprise-grade business AI application that analyzes CRM sales pipeline data to help sales teams prioritize leads, tailor pitches, and identify conversion risks using explainable decision logic.

---

##  Overview

Sales teams often struggle to efficiently prioritize leads due to scattered CRM data, unclear buying intent, and lack of explainability in automated scoring systems.  
This project addresses that gap by transforming raw sales pipeline data into **actionable, explainable insights** that support informed sales decision-making.

The system is designed as an **internal enterprise sales enablement tool**, similar to those used in large organizations for pipeline analysis and opportunity prioritization.

---

##  Key Features

- 📊 **Lead Quality Scoring (0–100)** based on business-driven rules  
- 🏷️ **Lead Categorization** (High / Medium / Low priority)  
- 🔍 **Explainable Insights** — clear reasons and risk flags for every score  
- 📂 **Excel-based CRM ingestion** (realistic enterprise workflow)  
- 🌐 **Interactive Web Dashboard** built with Streamlit  
- ☁️ **Cloud-deployed** with stateless, dependency-safe architecture  

---

##  System Architecture

Sales Pipeline (Excel)
↓
Feature Engineering (Pandas)
↓
Explainable Scoring Engine (Business Rules)
↓
Lead Insights (Reasons + Risks)
↓
Streamlit Web Dashboard


---

##  Tech Stack

- **Python**
- **Pandas** – data loading & feature engineering  
- **Streamlit** – interactive enterprise-style dashboard  
- **OpenPyXL** – Excel ingestion  

Designed to be lightweight, cloud-safe, and deployment-ready.

---

##  Lead Scoring Logic (Explainable)

Each lead is evaluated using four core business signals:

| Signal | Purpose |
|------|--------|
| Budget | Ability to purchase |
| Urgency | Time sensitivity |
| Decision Maker Engagement | Authority to convert |
| Call Notes Intent | Buying intent clarity |

Scores are mapped to categories and accompanied by:
- ✅ Positive signals (reasons)
- ⚠️ Risk indicators (conversion blockers)

This ensures **full transparency**, avoiding black-box decision making.

---

##  Business Impact

- Reduces manual effort in lead prioritization  
- Improves consistency in sales decision-making  
- Enables faster identification of high-value opportunities  
- Supports explainable, trustable AI adoption in sales workflows  

---

##  Live Demo

🔗 **Streamlit App:** https://ai-sales-enablement-analyze.streamlit.app/  
🔗 **Source Code:** https://github.com/Bhavana244-blip/ai-sales-enablement-analyzer

---

##  Use Cases

- Internal sales enablement dashboards  
- CRM decision-support tooling  
- Business AI demonstrations  
- Enterprise analytics prototypes  

---

##  Future Enhancements

- LLM-based natural language explanations  
- Predictive ML models for conversion probability  
- CRM integrations (Salesforce / HubSpot)  
- Downloadable lead reports (CSV / PDF)

---

##  Author
 
Built as an enterprise-style Business AI project focused on explainability and decision support.
