#  AI-Assisted Developer Toolkit

This is a Python application that assists a developer in various tasks and makes it easy for them to write code. 
It utilizes the LangChain library, which provides a framework for working with language models such as OpenAI's GPT-3.5.
1. It generates SQL queries based on user input. 
2. It also helps the developer write the testcases for a given function in python.
3. It helps developer generate a full application code by specifying the application details in prompt, language to be used and directory name in which to save the app.


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

    C. To run the code generator

        streamlit run code_generator.py


2. The application will launch in your browser.

3. Enter your text or code snippet in the text area.

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

Test Case Generator: When working on the test case generator, I faced some challenges due to code truncation limitations imposed by the OpenAI model. The generated code was getting cut off, which impacted the accuracy and usefulness of the test cases. This required finding a workaround to handle code truncation.

Code Generator: Developing the app code generator presented a few difficulties. Firstly, larger files had their code truncated. To address this, I experimented with the max_tokens parameter in the model wrapper and found that setting it to a larger value, such as 500 or 1000, resolved the issue.

Invalid Argument Errors: I encountered some errors related to invalid arguments because the OpenAI request was including unnecessary explanations and filenames in the generated code. To rectify this, I modified the template instructions to exclude any explanations and only return valid code, which successfully resolved the issue.

Model Selection: Switching between different models, such as from text-davinci-003 to code-davinci-002 or the default model, had an impact on the precision and organization of the generated code. By experimenting with different models, I found the most suitable one for generating accurate and well-structured code.

By iteratively addressing these challenges and making adjustments to the code and instructions, I was able to enhance the performance and usability of the application. These insights demonstrate the importance of iterative development and the need for adaptability when working with language models like OpenAI's GPT-3.5.


## Acknowledgements

- LangChain: [https://github.com/openai/langchain](https://github.com/openai/langchain)
- Streamlit: [https://www.streamlit.io/](https://www.streamlit.io/)
- OpenAI: [https://openai.com/](https://openai.com/)
- Youtube: [https://youtube.com]
