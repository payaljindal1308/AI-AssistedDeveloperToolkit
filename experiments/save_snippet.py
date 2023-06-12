# Bring in deps
import os 
from apikey import apikey 

import streamlit as st 

# Define Snippet class
class Snippet:
    def __init__(self, name, language, code):
        self.name = name
        self.language = language
        self.code = code

# App framework
st.title('Code Snippet Manager')

# Input fields for snippet details
name = st.text_input('Snippet Name')
language = st.text_input('Language')
code = st.text_area('Code')

# Save button
if st.button('Save Snippet'):
    # Create a new snippet instance
    snippet = Snippet(name, language, code)
    
    # Check if snippets directory exists, create if not
    if not os.path.exists('snippets'):
        os.makedirs('snippets')

    # Generate a unique filename for the snippet
    filename = f'snippets/{name}.txt'

    # Save the snippet to file
    with open(filename, 'w') as file:
        file.write(code)

    st.success('Snippet saved successfully!')

# Display existing snippets
st.header('Existing Snippets')

# Check if snippets directory exists
if os.path.exists('snippets'):
    # Iterate over snippet files
    for filename in os.listdir('snippets'):
        with open(os.path.join('snippets', filename), 'r') as file:
            snippet_lines = file.readlines()

        # Extract snippet details
        snippet_name = snippet_lines[0].replace('Name: ', '').strip()
        snippet_language = snippet_lines[1].replace('Language: ', '').strip()
        snippet_code = ''.join(snippet_lines[3:])

        # Display snippet details
        st.subheader(snippet_name)
        st.write(f'Language: {snippet_language}')
        st.code(snippet_code)
        st.write('---')
else:
    st.info('No snippets found.')

