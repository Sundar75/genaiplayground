import streamlit as st

st.set_page_config(page_title="AI Time Savings in Data Engineering", layout="wide")

st.title("🚀 AI-Driven Development in Data Engineering")

st.markdown("Use this tool to understand how GenAI accelerates your data engineering tasks.")

with st.sidebar:
    st.header("Estimate Your Savings")
    num_functions = st.number_input("Number of ETL Functions", min_value=1, value=5)
    num_validations = st.number_input("Validation Rules", min_value=1, value=10)

st.subheader("⏱️ Estimated Time Savings")
col1, col2 = st.columns(2)

with col1:
    st.metric("🧪 Unit Tests Saved (mins)", value=round(num_functions * (60 - 15)))
    st.metric("🧼 Validation Logic Saved (mins)", value=round(num_validations * (120 - 45)))

with col2:
    st.metric("🛠️ CI/CD Setup Saved (mins)", value=60)
    st.metric("📚 Docs Generation Saved (mins)", value=35)

st.divider()

st.subheader("🧠 Key Areas Optimized")
st.markdown("""
- Schema & datatype validation (PyDantic, Pandera)
- Nulls, duplicates, and range checks
- Business rule transformation into tests
- Async retry/test boilerplates
""")

st.subheader("🧰 Tools Used")
st.markdown("""
- **ChatGPT**: Code, test, and docs generation  
- **Cursor**: Inline AI editing in codebase  
- **Great Expectations**: Reusable validation suites  
- **dbt tests**: SQL logic validation  
""")
