#  AI-Assisted Developer Toolkit

This is a Python application that assists a developer in various tasks and makes it easy for them to write code. It generates SQL queries based on user input. It utilizes the LangChain library, which provides a framework for working with language models such as OpenAI's GPT-3.5.
It also helps the developer write the testcases for a given function in python.


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


3. Install the required Python packages using pip.

    pip install -r requirements.txt


4. Create a `.env` file in the project directory and provide your OpenAI API key.

    OPENAI_API_KEY=your-api-key


## Usage

1. Run the application using the following command:

    A. To run the test case generator-

        streamlit run testcase_generator.py
    
    B. To run the sql generator

        streamlit run sql_query_generator.py


2. The application will launch in your browser.

3. Enter your text or code snippet in the text area.

4. Click the "Generate Query" button if it is sql query generator or Generate test cases button to generate the test cases.

5. The generated SQL query or test cases will be displayed on the screen.

# Images

    1. Test Case Generator-

        ![Alt Text](images\test_case_console.png)

        ![Alt Text](images\test_case_ui.png)

    2. SQL Query Generator- 

        ![Alt Text](images\sql_console.png)

        ![Alt Text](images\sql_ui.png)


# Insights 

By adopting this approach, we can create a user-friendly application that leverages the capabilities of language models to generate SQL queries or test cases based on user input. The integration of LangChain and Streamlit simplifies development while allowing for customization and extensibility.

The prompt-driven approach of LangChain makes it easy to customize the template, enabling developers to structure and interact with the language model effectively. The power of LLMs (Language Model Models) opens up possibilities for extending this project to assist developers in writing applications with great ease.

For example, additional utilities can be added to the application, such as a code generator utility or the ability to generate environment files, further enhancing its usefulness to developers.

Currently, the project generates one test case at a time. However, with future updates, it can be expanded to generate multiple test cases, providing even more comprehensive testing capabilities.

## Customization

If you want to modify the behavior or appearance of the application, you can make changes to the `testcase_generator.py` file or `sql_query_generator.py`.


## Acknowledgements

- LangChain: [https://github.com/openai/langchain](https://github.com/openai/langchain)
- Streamlit: [https://www.streamlit.io/](https://www.streamlit.io/)
- OpenAI: [https://openai.com/](https://openai.com/)
- Youtube: [https://youtube.com]
