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
        "Moderate": 75,
        "Complex": 120
    }
    function_dev_time = complexity_multiplier[function_complexity]

    num_stored_procs = st.number_input("Stored Procedures (basic UPSERT)", min_value=0, value=3)

    st.subheader("Validation Checks")
    validation_times = {
        "Not Null / Mandatory fields": 60,
        "Data type and format validation": 75,
        "Range checks": 60,
        "Duplicate row detection": 90,
        "Referential integrity checks": 90,
        "Enum / value constraints": 60,
        "Temporal logic": 90,
        "Pattern matching": 60
    }
    selected_checks = []
    total_validation_time_without_ai = 0
    total_validation_time_with_ai = 0
    for check, time in validation_times.items():
        if st.checkbox(check, value=("Mandatory" in check or "format" in check or "Range" in check)):
            selected_checks.append(check)
            total_validation_time_without_ai += time
            total_validation_time_with_ai += round(time * 0.4)  # Assume 60% time saving with AI

st.subheader("⏱️ Estimated Time Comparison")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Without AI (mins)**")
    st.write("Unit Tests:", num_functions * 90)
    st.write("Validation Logic:", total_validation_time_without_ai)
    st.write("CI/CD Setup:", 90)
    st.write("Stored Proc:", num_stored_procs * 60)
    st.write("Function App Dev:", num_functions * function_dev_time)
    st.write("Docs Generation:", 60)

with col2:
    st.markdown("**With AI (mins)**")
    st.write("Unit Tests:", num_functions * 20)
    st.write("Validation Logic:", total_validation_time_with_ai)
    st.write("CI/CD Setup:", 30)
    st.write("Stored Proc:", num_stored_procs * 15)
    st.write("Function App Dev:", num_functions * 25)
    st.write("Docs Generation:", 10)

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
