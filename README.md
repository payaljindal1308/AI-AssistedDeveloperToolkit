#  AI-Assisted Developer Toolkit

## Overview

This Python application is designed to assist developers in various tasks, making it easier for them to write code. It leverages the LangChain library, which serves as a framework for working with language models like OpenAI's GPT-3.5. The application offers the following functionalities:

SQL Query Generation: Users can input their requirements, and the application generates SQL queries based on the given input.

Test Case Generation: The application aids developers in writing test cases for a specific Python function. This feature automates the process and saves time for the developer.

Application Code Generation: By providing necessary details such as application specifications, desired programming language, and directory name for saving the app, developers can generate a complete application code.

## Experimentation and Examples

The "experiments" directory contains different approaches and iterations taken during the development of this application. These files showcase the experimentation process and demonstrate how the application evolved over time.

Additionally, the "examples_generated" directory showcases some example applications that have been generated using the code generator feature. These examples serve as a reference and demonstrate the capabilities of the application in creating functional code for various applications.

Overall, the application serves as a valuable toolkit for developers, providing assistance in SQL query generation, test case writing, and complete application code generation. The experimentation and example directories further illustrate the evolution and effectiveness of the application.

## Prerequisites

Make sure you have the following dependencies installed:

- Python 3.x
- langchain
- streamlit
- dotenv

You can install these dependencies using pip:

pip install langchain streamlit python-dotenv

## Getting Started

1. Clone this repository to your local machine.

        git clone https://github.com/payaljindal1308/AI-AssistedDeveloperToolkit.git


2. Change into the project directory.

        cd AI-AssistedDeveloperToolkit

3. Generate the python environment and activate it using the follwoing commands-

        python -m venv venv
        .venv/Scripts/Activate

4. Install the required Python packages using pip.

        pip install -r requirements.txt

5. Create a `.env` file in the project directory and provide your OpenAI API key.

        OPENAI_API_KEY=your-api-key


## Usage

1. Run the application using the following command:

    A. To run the test case generator-

        streamlit run testcase_generator.py
    
    B. To run the sql generator

        streamlit run sql_query_generator.py

    C. To run the code generator

        streamlit run code_generator.py


2. The application will launch in your browser.

3. Enter your text or code snippet or prompt for app in the text area.

4. Click the "Generate Query" button if it is sql query generator or Generate test cases button to generate the test cases or "Generate App" to generate code. 

5. The generated SQL query or test cases will be displayed on the screen.

# Images

    1. Code Generator -

![Code Generator](https://raw.githubusercontent.com/payaljindal1308/AI-AssistedDeveloperToolkit/main/images/code_generator_console.png)

![Code Generator](https://raw.githubusercontent.com/payaljindal1308/AI-AssistedDeveloperToolkit/main/images/code_genrator_ui.png)

    2. Test Case Generator-

![Test Generator Console](https://raw.githubusercontent.com/payaljindal1308/AI-AssistedDeveloperToolkit/main/images/sql_console.png)

![Test Generator UI](https://raw.githubusercontent.com/payaljindal1308/AI-AssistedDeveloperToolkit/main/images/test_case_ui.png)


    3. SQL Query Generator- 

![SQL Query Genertor Console](https://raw.githubusercontent.com/payaljindal1308/AI-AssistedDeveloperToolkit/main/images/sql_console.png)

![SQL Query Generator UI](https://raw.githubusercontent.com/payaljindal1308/AI-AssistedDeveloperToolkit/main/images/sql_ui.png)


# Insights 

Throughout the development process of this project, I encountered various challenges and made necessary adjustments to overcome them. Here are some key insights gained:

SQL Query Generator: The initial implementation of the SQL query generator was relatively straightforward, and I was able to create the application without much difficulty.

Test Case Generator: When working on the test case generator, I faced some challenges due to code truncation limitations imposed by the OpenAI model. The generated code was getting cut off, which impacted the accuracy and usefulness of the test cases. This required finding a workaround to handle code truncation. Then I changed the model from text-davinci to default which is GPT-3.5 turbo and also changed the temparature parameter to 0.5 from 0.9. and saw that my tests were not getting truncated and they were also more accurate.


Code Generator: Developing the app code generator presented a few difficulties. Firstly, larger files had their code truncated. To address this, I experimented with the max_tokens parameter in the model wrapper and found that setting it to a larger value, such as 500 or 1000, resolved the issue.


Code Accuracy: While generating different outputs, I also noticed that some part of the generated code was getting replicated and code needs to be changed for accuracy, to resolve this issue, I tried changing the temperature parameter from 0.9 to smaller values and that made the generated code more accurate. Although it improved but further optimization is possible with more efforts.

Invalid Argument Errors: I encountered some errors related to invalid arguments because the OpenAI request was including unnecessary explanations and filenames in the generated code. To rectify this, I modified the template instructions to exclude any explanations and only return valid code, which successfully resolved the issue.

Model Selection: Switching between different models, such as from text-davinci-003 to code-davinci-002 or the default model(GPT-3.5 turbo), had an impact on the precision and organization of the generated code. By experimenting with different models, I found the most suitable one for generating accurate and well-structured code.

By iteratively addressing these challenges and making adjustments to the code and instructions, I was able to enhance the performance and usability of the application. These insights demonstrate the importance of iterative development and the need for adaptability when working with language models like OpenAI's GPT-3.5.


## Acknowledgements

- LangChain: [https://github.com/openai/langchain](https://github.com/openai/langchain)
- Streamlit: [https://www.streamlit.io/](https://www.streamlit.io/)
- OpenAI: [https://openai.com/](https://openai.com/)
- Youtube: [https://youtube.com]
