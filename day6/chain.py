from langchain_groq import ChatGroq
from model import create_chat_groq
from  prompt import code_generator_prompt

def generate_code(language,problem_statement):
    '''
    function to generate code
    args:
        topic (str) - topic of the poem
    return:
        response.content (str)
    '''
    prompt_template = prompt.code_generator_prompt()
    llm = model.create_chat_groq()

    chain = prompt_template | llm
    response = chain.invoke({
        "language" : language,
        "problem_statement" : problem_statement
    })
    return response.content