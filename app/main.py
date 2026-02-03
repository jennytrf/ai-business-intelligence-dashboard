import streamlit as st
import pandas as pd
from kpi import load_data, calculate_kpis
from ai_insights import generate_insights
import os

st.set_page_config(page_title="AI Business Intelligence Dashboard", layout="wide")

st.title("📊 AI Business Intelligence Dashboard")

df = load_data()
df, total_revenue, avg_growth, avg_churn = calculate_kpis(df)

# KPI Cards
col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Revenue", f"${total_revenue:,.0f}")
col2.metric("📈 Avg Revenue Growth", f"{avg_growth:.2f}%")
col3.metric("🔻 Avg Churn Rate", f"{avg_churn:.2f}%")

st.divider()
st.subheader("🧠 AI Business Insights")

summary_text = f"""
Total Revenue: {total_revenue}
Average Revenue Growth: {avg_growth:.2f}%
Average Churn Rate: {avg_churn:.2f}%

Monthly Data:
{df[['date', 'revenue', 'revenue_growth', 'churn_rate']].to_string(index=False)}
"""

api_key = st.secrets.get("OPENAI_API_KEY", "")

if api_key:
    if st.button("Generate AI Insights"):
        with st.spinner("Analyzing business performance..."):
            insights = generate_insights(api_key, summary_text)
            st.success("Insights generated")
            st.write(insights)
else:
    st.warning("OpenAI API key not found. Add it to Streamlit secrets.")

# Charts
st.subheader("Revenue Over Time")
st.line_chart(df.set_index("date")["revenue"])

st.subheader("Customer Churn Rate")
st.bar_chart(df.set_index("date")["churn_rate"])

st.subheader("Dataset Preview")
st.dataframe(df)
