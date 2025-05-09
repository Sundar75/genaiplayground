import streamlit as st

st.set_page_config(page_title="AI Time Savings in Data Engineering", layout="wide")

st.title("🚀 AI-Driven Development in Data Engineering")

st.markdown("Use this tool to understand how GenAI accelerates your data engineering tasks.")

with st.sidebar:
    st.header("Estimate Your Savings")
    num_functions = st.number_input("Number of ETL Functions", min_value=1, value=5)
    function_complexity = st.selectbox("Function Complexity", ["Simple", "Moderate", "Complex"])

    complexity_multiplier = {
        "Simple": 45,
        "Moderate": 60,
        "Complex": 90
    }
    function_dev_time = complexity_multiplier[function_complexity]

    num_validations = st.number_input("Validation Rules", min_value=1, value=10)
    num_stored_procs = st.number_input("Stored Procedures (basic UPSERT)", min_value=0, value=3)

st.subheader("⏱️ Estimated Time Savings")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🧪 Unit Tests Saved (mins)", value=round(num_functions * (60 - 15)))
    st.metric("🧼 Validation Logic Saved (mins)", value=round(num_validations * (120 - 45)))

with col2:
    st.metric("🛠️ CI/CD Setup Saved (mins)", value=60)
    st.metric("🧮 Stored Proc Time Saved (mins)", value=round(num_stored_procs * (40 - 10)))

with col3:
    st.metric("🧱 Function App Dev Time Saved (mins)", value=round(num_functions * (function_dev_time - 20)))
    st.metric("📚 Docs Generation Saved (mins)", value=35)

st.divider()

st.subheader("🧠 Key Areas Optimized")
st.markdown("""
- Schema & datatype validation (PyDantic, Pandera)
- Nulls, duplicates, and range checks
- Business rule transformation into tests
- Async retry/test boilerplates
""")

st.subheader("🧪 Data Quality Validation Checks")
st.markdown("""
**Common Checks:**
- Not Null / Mandatory fields
- Data type and format validation
- Range checks (e.g. age > 0)
- Duplicate row detection
- Referential integrity checks (foreign keys)
- Enum / value constraints (e.g. status in ['open', 'closed'])
- Temporal logic (e.g. start_date <= end_date)
- Pattern matching (e.g. email format)
""")

st.subheader("🧰 Tools Used")
st.markdown("""
- **ChatGPT**: Code, test, and docs generation  
- **Cursor**: Inline AI editing in codebase  
- **Great Expectations**: Reusable validation suites  
- **dbt tests**: SQL logic validation  
""")
