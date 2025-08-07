# Capital & Portfolio Optimization Agent Demo

**AI-powered decision support for optimizing capital deployment and reinsurance strategy — built for insurers, reinsurers, and advisors.**

This demo showcases a multi-step Streamlit application using Reinforcement Learning (RL) and LLMs to guide capital and reinsurance decisions under solvency constraints. It is part of our broader mission to deliver intelligent financial infrastructure for risk-bearing entities.

---

## 🚀 What It Does

Insurance CFOs, CROs, and reinsurance buyers must decide how much risk to retain and how much reinsurance to buy — every year, under uncertainty.

Our app helps answer:
- How do I deploy capital across business lines to maximize ROE?
- When should I increase or reduce reinsurance?
- What’s the optimal capital strategy over multiple years?
- How can I explain this strategy to regulators or my board?

The agent:
- Simulates macroeconomic and catastrophe risks
- Trains a reinforcement learning (RL) policy to maximize return under solvency constraints
- Uses an LLM to explain the rationale and generate a management report
- Provides a downloadable, decision-ready capital strategy

---

## 📂 Project Structure

```

📁 capital-optimizer-app/
├── assets/
│   ├── step1\_icon.png
│   ├── step2\_icon.png
│   ├── step3\_icon.png
│   ├── step4\_icon.png
│   └── step5\_icon.png
├── app.py                      ← Main Streamlit app
├── requirements.txt            ← Python dependencies
├── README.md                   ← This file

````

---

## 🧭 App Workflow

| Step | Description |
|------|-------------|
| **🏠 Home** | Introduces the tool, the problem, and what the user will experience |
| **📂 Step 1: Portfolio Setup** | Upload or edit portfolio across lines of business (TIV, losses, capital) |
| **📊 Step 2: Scenario Simulation** | Configure catastrophe frequency, simulate recession scenarios, and visualize projected ROE / solvency |
| **🧠 Step 3: RL Optimization** | Run the reinforcement learning agent to optimize capital allocation and reinsurance spend |
| **💬 Step 4: LLM Summary** | Generate a management-friendly narrative of the strategy using GPT |
| **✅ Step 5: Final Report** | Review KPIs, see strategy tables/plots, and (coming soon) download summary reports |

---

## 📈 Sample Output

**Optimized Strategy (2024–2027)**  
- ROE increases from **10.2% → 12.3%**  
- Solvency ratio held between **132–145%**  
- Reinsurance spend adjusts dynamically  
- Explanation: “Model recommends increasing CAT cover in 2025–26 due to hurricane risk and reinsurance pricing shifts.”

---

## 🛠 Tech Stack

- 🧠 **Reinforcement Learning** (simulated agent logic)
- 💬 **LLMs** via OpenAI/Azure OpenAI (management summaries)
- 📊 **Streamlit** UI for interactivity
- 🧮 **Pandas / NumPy / Matplotlib** for simulation and plotting

---

## 💡 Why It Matters

> "Optimizing reinsurance and capital is one of the most critical, yet underserved, areas of insurance finance."  
> — *Actuaries Digital, 2023*

Large insurers run expensive Dynamic Financial Analysis models. We bring that power to smaller and mid-size insurers via intuitive AI co-pilots.

---

## 📅 What's Next

- 📄 Auto-generate full PDF / Word summaries
- 🔍 Add risk decomposition and attribution
- 🧑‍⚖️ Integrate Solvency II / RBC compliance modules
- 🌐 Connect with live reinsurance market data
- 🧾 Upload actual portfolio results for real-world tuning

---

## 🧪 Demo This App

You can explore a live demo here:  
👉 [Streamlit Demo App](https://your-streamlit-app-link.com)

Or run locally:

```bash
pip install -r requirements.txt
streamlit run app.py
````

---

## 📬 Contact

Built by **[Reinsurance Analytics](https://www.linkedin.com/company/reinsurance-analytics)**
🔗 Co-founders: Stella Dong (CTO) and James Finlay (CEO)
✉️ [contact@reinsuranceanalytics.ai](mailto:contact@reinsuranceanalytics.ai)

---

## 🧠 Part of a Broader Vision

This demo is one of several AI-powered tools we’re building to modernize risk and capital decision-making:

* **ClauseLens™** — Legal clause explanation + retrieval
* **MarketLens™** — Market benchmarking and fairness analysis
* **CCAC** — Constrained capital allocation for treaty bidding
* **Governance-in-the-Loop** — Stress-test + audit RL agent behavior

We're building **transparent market platforms** for insurance and reinsurance.

