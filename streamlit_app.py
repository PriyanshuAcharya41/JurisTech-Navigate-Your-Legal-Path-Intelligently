import streamlit as st
from crew_simple import legal_assistant_crew_simple # <-- Import the simple crew

st.set_page_config(page_title="AI Legal Assistant (Simple)", layout="wide")

st.title("⚖️ AI Legal Assistant (Simple Text Output)")

with st.form("simple_form"):
    user_input = st.text_area("Enter your legal issue:", height=150)
    submit_button = st.form_submit_button("Get Legal Draft")

if submit_button and user_input:
    with st.spinner("Generating legal draft..."):
        # The result will be a single string
        result_string = legal_assistant_crew_simple.kickoff(inputs={"user_input": user_input})
        st.success("Draft Generated!")
        st.markdown("### Your Legal Document:")
        st.markdown(result_string)