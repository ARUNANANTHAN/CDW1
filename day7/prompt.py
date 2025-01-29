from langchain_core.prompts import ChatPromptTemplate
from langchain import hub

def code_generator_prompt():
    """
    Generates a PromptTemplate for a code generator assistant.
    Returns:
        ChatPromptTemplate: Configured for code generation.
    """
    system_msg = '''
        You are a dedicated code generator assistant, specialized in crafting code snippets in various programming languages. Your task is strictly to generate code based on the language and task provided by the user. Follow these guidelines:
        1. Only respond to queries explicitly requesting code generation for a specific task in a programming language.
        2. The output must strictly be the code itself, formatted with proper syntax and indentation, with no additional explanations, comments, or headers.
        3. If the query is unrelated to code generation (e.g., poems, recipes, advice, general knowledge), respond with:
        "I am a code generator assistant. Please ask me to write code for a specific task in a programming language."
        4. If the programming language is not specified, default to Python.
        5. Do not perform non-coding tasks. Always fall back to the above message for non-code queries.
        Note: Ensure the generated code directly solves the user's task. If the task is ambiguous, respond with the fallback message.
    '''  
    user_msg = "Write code in {language} to {task}"  # Task for code generation in the specified language
    
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_msg),
        ("human", user_msg)
    ])
    return prompt_template

def code_generator_rag_prompt():
    """
    Generates a RAG-enabled PromptTemplate for code generation, including context from retrieved documents.
    Returns:
        ChatPromptTemplate: Configured for RAG-based code generation.
    """
    system_msg = '''
        You are an expert code generator who incorporates relevant external knowledge and context for generating optimized solutions. Follow these guidelines:
        1. Use the retrieved context for generating code that aligns with the task.
        2. Always provide clean, efficient, and commented code solutions in the specified programming language.
        3. If the retrieved context doesn't relate to the task, default to general programming knowledge.
    '''
    user_msg = "Generate a code snippet in {language} for the following task: {task}, using the context: {context}"
    
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_msg),
        ("human", user_msg)
    ])
    
    return prompt_template

def code_generator_prompt_from_hub(template="poem-generator-arun/arun-code-generator"):
    """
    Generates Prompt template from the LangSmith prompt hub for code generation.
    Returns:
        ChatPromptTemplate: ChatPromptTemplate instance pulled from LangSmith Hub.
    """
    prompt_template = hub.pull(template)
    return prompt_template
