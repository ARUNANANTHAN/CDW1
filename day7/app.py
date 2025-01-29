import streamlit as st
import chain
import model
import vectordb

def code_generator_app():
    """Enhanced Code Generator Application with RAG functionality"""
    
    st.title("Code Generator AI")
    st.markdown("Generate code snippets in various programming languages using RAG")

    # Sidebar for choosing code generation or file ingestion for RAG
    st.sidebar.title("Menu")
    section = st.sidebar.radio(
        "Choose a section:",
        ("Code Generator", "RAG File Ingestion")
    )
    
    # Initialize vector database
    vectordatabase = vectordb.initialize_chroma()

    if section == "RAG File Ingestion":
        # RAG File Ingestion Section
        st.subheader("Upload Documents for RAG Context Retrieval")
        uploaded_file = st.file_uploader("Upload a file:", type=["txt", "csv", "docx", "pdf"])
        
        if uploaded_file is not None:
            vectordb.store_pdf_in_chroma(uploaded_file, vectordatabase)
            st.success(f"File '{uploaded_file.name}' uploaded and embedded successfully!")
    
    else:
        # Code Generation Section (Single Form Handling Both Regular and RAG Code Generation)
        st.subheader("AI Code Generator")

        with st.form("code_gen_form"):
            col1, col2 = st.columns([1, 3])
            
            with col1:
                language = st.text_input("Programming Language", value="Python")
            with col2:
                problem_statement = st.text_area(
                    "Task Description",
                    height=150,
                    placeholder="Describe the task you want to implement"
                )
            
            # Checkbox to toggle RAG functionality
            rag_enabled = st.checkbox("Enable RAG (Retrieve relevant context before generation)", value=True)

            submitted = st.form_submit_button("Generate Code", use_container_width=True)

        if submitted:
            if not problem_statement:
                st.error("Please provide a task description.")
                return
            
            with st.spinner(f"Generating {language} code..."):
                try:
                    # Use RAG-based generation if enabled, otherwise use regular generation
                    if rag_enabled:
                        response = chain.generate_code_rag(language, problem_statement, vectordatabase)
                    else:
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
                    st.info("Please try adjusting your task description.")

if __name__ == "__main__":
    code_generator_app()
