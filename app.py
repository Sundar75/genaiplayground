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

    # num_validations = st.number_input("Validation Rules", min_value=1, value=10)
    num_stored_procs = st.number_input("Stored Procedures (basic UPSERT)", min_value=0, value=3)

    st.subheader("Validation Checks")
    checks = {
        "Not Null / Mandatory fields": st.checkbox("Not Null / Mandatory fields", value=True),
        "Data type and format validation": st.checkbox("Data type and format validation", value=True),
        "Range checks": st.checkbox("Range checks", value=True),
        "Duplicate row detection": st.checkbox("Duplicate row detection", value=False),
        "Referential integrity checks": st.checkbox("Referential integrity checks", value=False),
        "Enum / value constraints": st.checkbox("Enum / value constraints", value=False),
        "Temporal logic": st.checkbox("Temporal logic", value=False),
        "Pattern matching": st.checkbox("Pattern matching", value=False)
    }

st.subheader("⏱️ Estimated Time Comparison")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Without AI (mins)**")
    st.write("Unit Tests:", num_functions * 60)
    st.write("Validation Logic:", num_validations * 120)
    st.write("CI/CD Setup:", 90)
    st.write("Stored Proc:", num_stored_procs * 40)
    st.write("Function App Dev:", num_functions * function_dev_time)
    st.write("Docs Generation:", 45)

with col2:
    st.markdown("**With AI (mins)**")
    st.write("Unit Tests:", num_functions * 15)
    st.write("Validation Logic:", num_validations * 45)
    st.write("CI/CD Setup:", 30)
    st.write("Stored Proc:", num_stored_procs * 10)
    st.write("Function App Dev:", num_functions * 20)
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
