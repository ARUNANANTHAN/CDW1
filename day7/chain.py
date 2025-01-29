from langchain_core.output_parsers import StrOutputParser
import model
import prompt
import vectordb

#### RETRIEVAL and GENERATION for RAG ####
def generate_code_rag(language, task, vector):
    """
    Creates a RAG chain for retrieval and code generation.
    Args:
        language (str) - The programming language for code generation.
        task (str) - Description of the programming task.
        vector (object) - Instance of vector store for retrieving context.
    Returns:
        str - The generated code.
    """
    # Prompt for RAG-based code generation
    rag_prompt = prompt.code_generator_rag_prompt()  # Changed from `prompt` to `rag_prompt`
    
    # LLM initialization
    llm = model.create_chat_groq()

    # Post-processing for retrieved docs (format them for the prompt)
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    # Retrieve relevant context from the vector database (RAG step)
    retriever = vectordb.retrieve_from_chroma(task, vectorstore=vector)
    
    # Chain the retrieval and code generation process
    rag_chain = rag_prompt | llm | StrOutputParser()

    # Invoke the chain
    response = rag_chain.invoke({
        "context": format_docs(retriever),
        "task": task,
        "language": language  # Include the language for the code generation
    })
    return response
