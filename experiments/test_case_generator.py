# Bring in deps
import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

os.environ['OPENAI_API_KEY'] = apikey

# App framework
st.title('Test Case Generator')
prompt = st.text_area('Code Snippet or Function')

# Prompt template
test_case_template = PromptTemplate(
    input_variables=['snippet'],
    template="""You're using a Test Case Generator.
    Write test cases in python to validate the correctness of the code snippet or function- {snippet}. Please provide the whole code"""
)

# Memory
test_case_memory = ConversationBufferMemory(input_key='snippet', memory_key='test_case_history')

# LLM
llm = OpenAI(temperature=0.9)
test_case_chain = LLMChain(llm=llm, prompt=test_case_template, verbose=True, output_key='title', memory=test_case_memory)

# Generate test cases
if st.button('Generate Test Cases'):
    # Generate code using LLM
    generated_cases = test_case_chain.run(prompt)
    
    generated_cases_lines = generated_cases.split('\n')
    generated_cases_lines = generated_cases_lines[1:]  # Remove the first line
    generated_cases = '\n'.join(generated_cases_lines)
    print("generated", generated_cases)
    # Write the test cases to a Python file
    with open('test_cases.py', 'w') as file:
        file.write(generated_cases)
    # # Extract the generated test cases from the LLM output
    # test_cases_start = generated_cases.find('Test Cases:\n') + len('Test Cases:\n')
    # test_cases = generated_cases[test_cases_start:].strip()
    # print(test_cases)

    # Display the generated test cases
    st.write('Generated Test Cases:')
    st.text_area('generated_cases', value=generated_cases, height=300)
    st.success('Test cases generated successfully!')

# # Show previously generated test cases
# if os.path.exists('test_cases.py'):
#     with st.expander('Previously Generated Test Cases'):
#         with open('test_cases.py', 'r') as file:
#             saved_test_cases = file.read()
#         st.code(saved_test_cases, language='python')
