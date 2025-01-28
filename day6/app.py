
from dotenv import load_dotenv
import streamlit as st
import chain

load_dotenv()

def code_generator_app():
    with st.form("code_generator"):
        language = st.text_input("enter the language")
        problem_statement = st.text_input("enter the problem statement")
        submitted = st.form_submit_button("Submit")

        if(submitted):

            response = chain.generate_code(language,problem_statement)
            st.info(response)

code_generator_app()