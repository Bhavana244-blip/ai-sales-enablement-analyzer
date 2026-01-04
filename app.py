import streamlit as st


st.set_page_config(
    page_title="AI Sales Enablement Analyzer",
    layout="centered",
    page_icon=""
)

import pandas as pd
import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), "logic"))

from data_loader import load_and_prepare_data
from scorer import score_lead

st.markdown("""
<style>
body {
    background-color: #0f172a;
    color: #e5e7eb;
}

.main-container {
    background-color: #020617;
    padding: 36px;
    border-radius: 12px;
    border: 1px solid #334155;
    margin-bottom: 32px;
}

.card {
    background-color: #020617;
    padding: 24px;
    border-radius: 10px;
    border: 1px solid #334155;
    margin-bottom: 24px;
}

h1, h2, h3 {
    color: #f8fafc;
}

.subtitle {
    color: #94a3b8;
    font-size: 15px;
    margin-bottom: 24px;
}

.stDataFrame {
    border-radius: 8px;
}

.metric-box {
    background-color: #020617;
    padding: 18px;
    border-radius: 10px;
    border: 1px solid #334155;
    text-align: center;
}

.metric-title {
    font-size: 13px;
    color: #94a3b8;
}

.metric-value {
    font-size: 26px;
    font-weight: 700;
    color: #38bdf8;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.title("AI Sales Enablement Analyzer")
st.markdown(
    '<div class="subtitle">Enterprise-grade decision support for prioritizing sales leads</div>',
    unsafe_allow_html=True
)

st.markdown("""
This internal sales intelligence tool analyzes CRM pipeline data using
**explainable business rules** to help sales teams:
- Prioritize high-value leads
- Tailor sales pitches
- Identify conversion risks early
""")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("###  Load Sales Pipeline Data")

data_source = st.radio(
    "Select data source",
    ["Use sample dataset", "Upload Excel file"],
    horizontal=True
)

if data_source == "Upload Excel file":
    uploaded_file = st.file_uploader(
        "Upload sales pipeline (.xlsx)",
        type=["xlsx"]
    )
    if uploaded_file:
        df = load_and_prepare_data(uploaded_file)
    else:
        st.stop()
else:
    df = load_and_prepare_data("data/sales_pipeline.xlsx")

st.success(f"{len(df)} leads loaded successfully")
st.markdown('</div>', unsafe_allow_html=True)


st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("###  Lead Analysis")

results = []

for _, row in df.iterrows():
    analysis = score_lead(row)
    results.append({
        "Lead ID": row["lead_id"],
        "Company": row["company"],
        "Industry": row["industry"],
        "Score": analysis["score"],
        "Category": analysis["category"],
        "Reasons": ", ".join(analysis["reasons"]),
        "Risks": ", ".join(analysis["risks"]) if analysis["risks"] else "None"
    })

results_df = pd.DataFrame(results)

category_filter = st.multiselect(
    "Filter by lead category",
    ["High", "Medium", "Low"],
    default=["High", "Medium", "Low"]
)

filtered_df = results_df[
    results_df["Category"].isin(category_filter)
]

st.dataframe(filtered_df, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("###  Summary")

high_count = (results_df["Category"] == "High").sum()
medium_count = (results_df["Category"] == "Medium").sum()
low_count = (results_df["Category"] == "Low").sum()

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
        <div class="metric-box">
            <div class="metric-title">High Quality</div>
            <div class="metric-value">{high_count}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="metric-box">
            <div class="metric-title">Medium Quality</div>
            <div class="metric-value">{medium_count}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="metric-box">
            <div class="metric-title">Low Quality</div>
            <div class="metric-value">{low_count}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)

st.caption("Designed as an enterprise sales enablement and explainable AI decision-support system")
