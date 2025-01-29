
from dotenv import load_dotenv
import chain
import streamlit as st
from streamlit.components.v1 import html

load_dotenv()

# Apply custom CSS styles
st.markdown("""
    <style>
        /* Set background color for header */
        .stApp {
            background-color: #f0f4f8;
        }

        /* Style for the title */
        .stTitle {
            color: #2d6a4f;
        }

        /* Form background color */
        .stContainer {
            background-color: #ffffff;
            border-radius: 8px;
            padding: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }

        /* Button styles */
        .stButton>button {
            background-color: #2d6a4f;
            color: white;
            border-radius: 8px;
            box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
        }

        /* Input fields and text area styling */
        .stTextInput, .stTextArea {
            background-color: #e0f7fa;
            border: 1px solid #00796b;
            border-radius: 6px;
            padding: 8px;
        }

        /* Expander styling */
        .stExpander {
            background-color: #e0f7fa;
            border: 1px solid #00796b;
        }

        /* Customizing error message color */
        .stError {
            color: #d32f2f;
            font-weight: bold;
        }

        /* Customizing success and spinner text */
        .stSuccess {
            color: #388e3c;
        }

        .stSpinner {
            color: #00796b;
        }
    </style>
""", unsafe_allow_html=True)

def code_generator_app():
    """Enhanced Code Generator Application"""
    
    st.title("Code Generator AI")
    st.markdown("Generate code snippets in various programming languages")
    
    with st.container():
        with st.form("code_gen_form"):
            col1, col2 = st.columns([1, 3])
            
            with col1:
                language = st.text_input(
                    "Programming Language",
                    value="Python",  # Default to Python
                    help="Type the programming language you want the code in (e.g., Python, Java, C++)"
                )
                
            with col2:
                problem_statement = st.text_area(
                    "Task Description",
                    height=150,
                    placeholder="Describe the task you want to implement (e.g., 'Implement a stack data structure')",
                    help="Clearly describe the functionality you need"
                )

            submitted = st.form_submit_button(
                "Submit and Generate Code",
                use_container_width=True
            )

    if submitted:
        if not problem_statement:
            st.error("Please provide a task description")
            return
        with st.spinner(f"Generating {language} code..."):
            try:
                response = chain.generate_code(language, problem_statement)
                st.subheader("Generated Code")
                
                lang_map = {
                    "C": "c",
                    "C++": "cpp",
                    "Python": "python",
                    "Java": "java",
                    "JavaScript": "javascript",
                    "Go": "go",
                    "Rust": "rust"
                }
                
                with st.expander("View Code", expanded=True):
                    st.code(response, language=lang_map.get(language, "text"))

            except Exception as e:
                st.error(f"Code generation failed: {str(e)}")
                st.info("Please try adjusting your task description")

if __name__ == "__main__":
    code_generator_app()
