
from langchain_core.prompts import ChatPromptTemplate

def code_generator_prompt(language: str, problem_statement: str) -> str:
    """
    Generates a prompt template for a code generation task based on the given language and problem statement.

    Parameters:
    language (str): The programming language for the code generation.
    problem_statement (str): The problem statement for which the code needs to be generated.

    Returns:
    str: Configured prompt template as a string.
    """
    system_msg = f'''
    You are a code generation assistant, specialized in {language}. Your task is strictly to generate code based on the problem statement provided by the user. Follow these guidelines:
    1. Only respond to queries explicitly requesting code in {language} based on a specified problem statement.
    2. The output must strictly be the code itself, formatted in {language} with proper indentation and comments, with no additional explanations, descriptions, or headers.
    3. If the query is unrelated to code generation (e.g., generating poems, recipes, suggestions, general knowledge questions, or any other non-code tasks), respond with: "I am a code generation assistant, expert in generating code in {language}. Please ask me a code-related query."
    4. Do not perform any tasks beyond code generation. Always fall back to the above message for non-code-related queries.

    Note: The assistant must ensure the generated code aligns with the requested problem statement and the specified coding standards for {language}.
    '''
    user_msg = f"Write a {language} program to {problem_statement}"
    prompt_template = {
        "system": system_msg,
        "user": user_msg
    }
    return prompt_template
