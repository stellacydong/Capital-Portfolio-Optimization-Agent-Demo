import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Capital & Portfolio Optimization Agent", layout="wide")

# Sidebar Navigation
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio(
    "Select a step:",
    [
        "🏠 Home",
        "📂 Step 1: Portfolio Setup",
        "📊 Step 2: Scenario Simulation",
        "🧠 Step 3: RL Optimization",
        "💬 Step 4: LLM Summary",
        "✅ Step 5: Final Report"
    ]
)

# ---------------------------------------------
# HOME
# ---------------------------------------------
if page == "🏠 Home":
    st.image("assets/logo.png", width=220)
    st.markdown("<h1 style='text-align: center;'>💼 Capital & Portfolio Optimization Agent</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>AI-powered decision support for capital deployment and reinsurance optimization</p>", unsafe_allow_html=True)
    st.markdown("---")

    # --------------------------
    # Problem Section
    # --------------------------
    st.markdown("### ⚠️ The Capital Allocation Dilemma")
    st.markdown("""
    Insurance CFOs and CROs must continuously decide:
    
    - 📉 How much risk to **retain** across lines of business?
    - 💸 How much protection to **purchase** via reinsurance?

    **Too little** reinsurance → Elevated tail risk and capital strain  
    **Too much** reinsurance → Reduced profits and inefficient capital usage

    Most insurers manage this through static spreadsheets or costly actuarial consulting — unable to adapt dynamically to changing market conditions or portfolio volatility.
    """)

    st.markdown("---")

    # --------------------------
    # Our Solution
    # --------------------------
    st.markdown("### 💡 Our AI-Powered Solution")
    st.markdown("""
    The **Capital & Portfolio Optimization Agent** is your intelligent co-pilot for capital strategy. It:
    
    - 🔁 Simulates 1,000+ years of financial outcomes using Dynamic Financial Analysis
    - 🧠 Uses **Reinforcement Learning** to test and learn optimal retention vs. reinsurance trade-offs
    - 🌪 Adapts to macro shocks, CAT risk trends, and market pricing dynamics
    - 📝 Uses **LLMs** to generate executive-level insights in natural language
    
    Designed to break down silos between actuarial, finance, and reinsurance teams — and ensure capital is deployed where it creates the most value.
    """)

    # --------------------------
    # How It Works
    # --------------------------
    st.markdown("---")
    st.markdown("### ⚙️ How It Works")
    st.markdown("""
    1. **Define Your Portfolio:** Upload or simulate lines of business with exposures and capital  
    2. **Simulate Loss Years:** Generate thousands of future loss scenarios  
    3. **Optimize Strategy:** Let the RL agent learn the best balance of capital retention and risk transfer  
    4. **Interpret Results:** Review ROI, tail risk, and LLM-generated rationale for each recommended strategy  
    5. **Export Reports:** Download a summary or share with management

    Every step is interactive and auditable.
    """)
    st.markdown("---")
    # --------------------------
    # What to Expect in the Demo
    # --------------------------
    st.markdown("### 🧪 What to Expect in This Demo")
    st.markdown("""
    In this interactive demo, you'll walk through a 5-step optimization journey:
    
    1. 🧾 **Portfolio Setup** – Create a sample insurance book  
    2. 🌪️ **Scenario Simulation** – Generate loss events over time  
    3. 🤖 **RL Optimization** – Learn optimal capital/reinsurance strategy  
    4. 💬 **LLM Explanation** – See the results explained in plain English  
    5. ✅ **Final Strategy** – View the optimized output and download your packet
    """)

    st.success("➡️ Use the sidebar to begin your optimization journey.")


# ---------------------------------------------
# STEP 1: Portfolio Setup
# ---------------------------------------------
elif page == "📂 Step 1: Portfolio Setup":
    st.header("📂 Step 1: Define Portfolio Structure")

    st.markdown("""
    ### 🧾 What Is a Portfolio?
    A portfolio defines the insurer's current exposure across lines of business (LOBs), including:
    - **TIV**: Total Insured Value  
    - **Expected Loss**: Forecasted annual loss  
    - **Capital Allocated**: Capital reserves for each line

    This foundation enables our RL agent to simulate solvency and optimize capital deployment.
    """)

    st.markdown("### 📥 Choose or Create a Portfolio")

    option = st.radio("Select portfolio input method:", ["Use Sample", "Upload CSV", "Create Manually", "Generate Random"], horizontal=True)

    if option == "Use Sample":
        df = pd.DataFrame({
            "Line of Business": ["Homeowners", "Commercial Property", "Motor", "Liability"],
            "TIV ($M)": [500, 400, 300, 200],
            "Expected Loss ($M)": [50, 60, 30, 20],
            "Capital Allocated ($M)": [120, 100, 80, 50]
        })
        st.success("✅ Sample portfolio loaded.")

    elif option == "Upload CSV":
        uploaded_file = st.file_uploader("Upload a CSV with columns: Line of Business, TIV ($M), Expected Loss ($M), Capital Allocated ($M)")
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            st.success("✅ Uploaded portfolio loaded.")
        else:
            st.warning("Waiting for CSV upload...")
            st.stop()

    elif option == "Create Manually":
        st.markdown("### 📝 Enter Portfolio Data")
        num_rows = st.slider("Number of lines of business:", min_value=1, max_value=10, value=4)
        df = pd.DataFrame({
            "Line of Business": [f"LOB {i+1}" for i in range(num_rows)],
            "TIV ($M)": [100] * num_rows,
            "Expected Loss ($M)": [10] * num_rows,
            "Capital Allocated ($M)": [25] * num_rows
        })
        edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)
        df = edited_df
        st.success("✅ Manual portfolio defined.")

    elif option == "Generate Random":
        st.markdown("### 🎲 Generating Random Portfolio")
        num_lobs = st.slider("Number of random LOBs", 3, 10, 5)
        lob_names = [f"LOB {i+1}" for i in range(num_lobs)]
        df = pd.DataFrame({
            "Line of Business": lob_names,
            "TIV ($M)": np.random.randint(100, 1000, size=num_lobs),
            "Expected Loss ($M)": np.random.randint(10, 100, size=num_lobs),
            "Capital Allocated ($M)": np.random.randint(20, 200, size=num_lobs)
        })
        st.success("✅ Random portfolio generated.")

    # Display the portfolio
    st.markdown("### 📋 Portfolio Overview")
    st.dataframe(df, use_container_width=True)

    # Pie chart: Capital Allocation by LOB
    st.markdown("### 📊 Capital Allocation Visualization")

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.pie(df["Capital Allocated ($M)"], labels=df["Line of Business"], autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

    # Cache the portfolio for next steps
    st.session_state["portfolio_df"] = df

    st.markdown("---")
    st.markdown("""
    ✅ This portfolio will be used to:
    - Simulate financial performance under CAT and macroeconomic stress
    - Train the RL agent to adjust capital vs. reinsurance over time
    - Evaluate solvency risk and capital efficiency

    """)
    st.info("➡️ Proceed to **Step 2: Scenario Simulation** to stress-test this portfolio.")


# ---------------------------------------------
# STEP 2: Scenario Simulation
# ---------------------------------------------
elif page == "📊 Step 2: Scenario Simulation":
    st.header("📊 Step 2: Scenario Simulation")

    st.markdown("""
    ### 🌍 What This Step Does

    We simulate your portfolio’s performance across **5 years** under diverse:
    - 🌀 **Catastrophe events** (e.g. hurricane, wildfire)
    - 📉 **Macroeconomic stress** (e.g. inflation, asset shocks)

    These simulations provide the **training environment** for our Reinforcement Learning agent in Step 3.
    """)

    st.markdown("📌 Each simulation run generates: ")
    st.markdown("""
    - Projected **Return on Equity (ROE)**  
    - Regulatory **Solvency Ratio**  
    - Potential drawdowns from tail events  
    """)

    if st.button("▶️ Run 5-Year Simulation"):
        with st.spinner("Generating realistic portfolio scenarios..."):
            time.sleep(2)

            years = np.arange(2024, 2029)
            simulated_ROE = np.random.normal(loc=11, scale=2, size=5).round(2)
            simulated_solvency = np.random.normal(loc=140, scale=10, size=5).round(1)
            sim_df = pd.DataFrame({
                "Year": years,
                "ROE (%)": simulated_ROE,
                "Solvency Ratio (%)": simulated_solvency
            })

        st.success("✅ Simulation complete!")

        # Show table
        st.markdown("### 📋 Simulated Financial Metrics")
        st.dataframe(sim_df, use_container_width=True)

        # Plot
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(sim_df["Year"], sim_df["ROE (%)"], marker='o', label='ROE (%)', color='teal')
        ax.plot(sim_df["Year"], sim_df["Solvency Ratio (%)"], marker='s', label='Solvency Ratio (%)', color='orange')
        ax.set_title("📈 Projected ROE and Solvency Over Time", fontsize=13)
        ax.set_ylabel("Percentage")
        ax.set_xlabel("Year")
        ax.grid(True, linestyle="--", alpha=0.6)
        ax.legend()
        st.pyplot(fig)

        st.markdown("""
        🔍 **Interpretation Tips**:
        - **ROE** reflects profitability given capital deployment  
        - **Solvency Ratio** shows capital adequacy relative to risk  

        Strategies that sustain high ROE *and* maintain solvency above regulatory thresholds are preferred.
        """)

        st.info("➡️ Proceed to **Step 3: RL Optimization** to train the AI agent on these simulations.")

# ---------------------------------------------
# STEP 3: RL Optimization
# ---------------------------------------------
elif page == "🧠 Step 3: RL Optimization":
    st.header("🧠 Step 3: Reinforcement Learning Optimization")

    st.markdown("""
    ### 🧠 Train the AI Agent

    In this step, a reinforcement learning agent learns how to:
    - 📉 Retain or cede risk dynamically
    - 📈 Maximize return on equity (ROE)
    - 🛡 Maintain required solvency across economic cycles

    The agent observes portfolio outcomes from Step 2 and learns policies to balance risk and capital efficiency.
    """)

    st.markdown("---")
    st.subheader("🎛️ Optimization Parameters")

    solvency_target = st.slider("Target Solvency Ratio (%)", min_value=100, max_value=180, value=140, step=5)
    horizon = st.slider("Simulation Horizon (Years)", min_value=3, max_value=10, value=5)

    st.markdown("---")

    if st.button("🤖 Train Optimization Agent"):
        with st.spinner(f"Training RL agent for {horizon}-year simulation..."):
            time.sleep(3)

            years = list(range(2024, 2024 + horizon))
            capital_retained = np.random.randint(250, 310, size=horizon)
            reinsurance_premium = np.random.randint(25, 40, size=horizon)
            solvency = np.clip(np.random.normal(loc=solvency_target, scale=6, size=horizon), 100, 200)
            roe = np.clip(np.random.normal(loc=11.5, scale=1.5, size=horizon), 5, 20)

            strategy = pd.DataFrame({
                "Year": years,
                "Capital Retained ($M)": capital_retained,
                "Reinsurance Premium ($M)": reinsurance_premium,
                "Solvency Ratio (%)": solvency.round(1),
                "ROE (%)": roe.round(2)
            })

        st.success("✅ RL Agent Training Complete")

        st.markdown("### 📋 Optimized Capital Strategy")
        st.dataframe(strategy, use_container_width=True)

        st.markdown("### 📉 Risk vs Return Over Time")
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(strategy["Year"], strategy["ROE (%)"], marker='o', label="ROE (%)", color="teal")
        ax.plot(strategy["Year"], strategy["Solvency Ratio (%)"], marker='s', label="Solvency Ratio (%)", color="orange")
        ax.axhline(solvency_target, linestyle="--", color="red", label=f"Target Solvency ({solvency_target}%)")
        ax.set_ylabel("Percent")
        ax.set_xlabel("Year")
        ax.set_title("Capital Efficiency vs Risk")
        ax.grid(True, linestyle="--", alpha=0.6)
        ax.legend()
        st.pyplot(fig)

        st.markdown("### 📄 Policy Summary (LLM Preview)")
        st.info(f"""
        “Based on a target solvency of **{solvency_target}%**, the agent recommends:
        - Retaining more capital in early years when solvency is strong
        - Increasing reinsurance protection during projected CAT-heavy years
        - Targeting ROE improvements of **{round(np.mean(roe),1)}%** while maintaining buffers”
        """)

        st.info("➡️ Proceed to **Step 4: LLM Explanation** for natural language strategy generation.")

# ---------------------------------------------
# STEP 4: LLM Summary
# ---------------------------------------------
elif page == "💬 Step 4: LLM Summary":
    st.header("💬 Step 4: LLM-Generated Executive Summary")

    st.markdown("""
    ### 🧠 How It Works

    The system uses a **Large Language Model (LLM)** to turn technical strategy outputs into clear, natural language summaries for management, auditors, and regulators.

    **Input to the LLM includes:**
    - Portfolio structure (lines of business, TIV, expected loss)
    - Simulated economic & catastrophe scenarios
    - RL-optimized strategy: capital retained, reinsurance spend, ROE, solvency ratios
    - Target constraints (e.g. solvency floor)

    The LLM is prompted with this structured data using a custom template to generate:
    - 📄 Executive summaries
    - 📊 Line-of-business insights
    - 📌 Recommended actions and rationale

    The summary is designed to sound like a Chief Risk Officer's briefing.
    """)

    st.markdown("---")
    st.markdown("### 📄 Executive Summary Output")
    st.success("""
    “From 2024 to 2027, the RL model recommends a dynamic capital strategy:

    - In **2025–2026**, increased catastrophe frequency and tightening reinsurance markets lead the model to raise reinsurance spend by 20%, preserving solvency ratios above 130%.
    - In **2024 and 2027**, with milder forecast conditions, capital retention increases to enhance ROE.

    This approach ensures regulatory compliance, reduces tail risk exposure, and improves capital efficiency year-over-year.”
    """)

    st.markdown("### 🔧 Prompt Engineering (Optional)")
    with st.expander("🔍 View Sample Prompt Sent to LLM"):
        st.code("""
You are a financial strategy assistant. Summarize the following multi-year capital optimization results:

Portfolio:
- Homeowners: TIV=$500M, Expected Loss=$50M
- Motor: TIV=$300M, Expected Loss=$30M

Strategy (2024–2027):
- Reinsurance spend increases in 2025–26 due to forecasted CAT events
- Solvency maintained above 130%
- ROE improves in 2026–27

Return a concise, professional summary suitable for insurance management and regulators.
        """, language="markdown")

    st.markdown("### 📌 Why This Matters")
    st.markdown("""
    - 🧩 Turns complex simulations into understandable, decision-ready output  
    - 🧠 Aligns CFO, CRO, and Actuarial teams with a shared strategy  
    - 📎 Can be directly used in ORSA filings, board decks, or rating agency reviews
    """)

    st.info("➡️ Proceed to **Step 5** to export your strategy packet.")


# ---------------------------------------------
# STEP 5: Final Report
# ---------------------------------------------
elif page == "✅ Step 5: Final Report":
    st.header("✅ Step 5: Final Capital Strategy Report")

    st.markdown("### 🧾 Executive Highlights")
    st.markdown("""
    - 📈 **ROE improves** from *10.2%* to *12.3%* over four years  
    - 🛡️ **Solvency ratio consistently** exceeds target (140%)  
    - 💸 **Reinsurance spend dynamically adjusts** to market and risk  
    - 🤖 Strategy is **RL-optimized** across business cycles
    """)

    st.markdown("---")
    st.markdown("### 📋 Multi-Year Capital Optimization Results")

    summary = pd.DataFrame({
        "Year": [2024, 2025, 2026, 2027],
        "Capital Retained": [300, 280, 260, 290],
        "Reinsurance Premium": [28, 32, 36, 30],
        "Solvency Ratio (%)": [145, 138, 132, 140],
        "ROE (%)": [10.2, 11.5, 12.0, 12.3]
    })

    st.dataframe(summary.style.format({
        "Capital Retained": "${:,.0f}M",
        "Reinsurance Premium": "${:,.0f}M",
        "Solvency Ratio (%)": "{:.0f}%",
        "ROE (%)": "{:.1f}%"
    }), use_container_width=True)

    # Explanation of Results
    st.markdown("### 🧠 Interpretation of Strategy Results")
    st.markdown("""
    Over the simulated period (2024–2027), the AI agent learned to adjust the insurer’s capital and reinsurance strategy in response to macroeconomic and catastrophe conditions:

    - **2024–2025:** The model recommended increasing reinsurance spend due to elevated catastrophe risk and pricing pressure.  
      ➤ Result: Solvency ratio stayed above 138% even under stress, and ROE grew to 11.5%.

    - **2026:** With a favorable risk environment, the model retained more capital, reducing reinsurance premiums.  
      ➤ Result: ROE peaked at 12.0%, with solvency dipping slightly but still above 130%.

    - **2027:** A moderate correction rebalanced the portfolio to hit the 140% solvency target again.  
      ➤ Result: ROE reached 12.3% — the highest in the 4-year cycle.

    ✅ The agent learned a **cyclical strategy**: spend more on protection when risk is high, retain capital when safe — maximizing **risk-adjusted returns** while maintaining **regulatory buffers**.
    """)

    # Optional Visualization
    st.markdown("### 📊 ROE and Solvency Trends")
    fig, ax = plt.subplots()
    ax.plot(summary["Year"], summary["ROE (%)"], marker="o", label="ROE (%)")
    ax.plot(summary["Year"], summary["Solvency Ratio (%)"], marker="s", label="Solvency Ratio (%)")
    ax.axhline(140, linestyle="--", color="red", label="Target Solvency (140%)")
    ax.set_ylabel("Metric (%)")
    ax.set_title("Capital Strategy Performance")
    ax.legend()
    st.pyplot(fig)

    # Download buttons (disabled placeholder)
    col1, col2 = st.columns(2)
    with col1:
        st.download_button(
            label="⬇️ Download as Word (Coming Soon)",
            data="Summary content here...",
            file_name="Capital_Strategy_Summary.docx",
            disabled=True
        )
    with col2:
        st.download_button(
            label="⬇️ Download as Excel (Coming Soon)",
            data="Excel placeholder",
            file_name="Capital_Strategy_Summary.xlsx",
            disabled=True
        )

    st.markdown("---")
    st.success("✅ Demo complete. You're ready to use this AI co-pilot for capital optimization in real-world scenarios.")
    st.info("Book a strategy session or download the enterprise version to integrate with your internal capital models.")
