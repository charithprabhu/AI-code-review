AI Chatbot with Streamlit and Google Generative AI
This project demonstrates a simple AI chatbot application built using Streamlit and Google Generative AI (specifically, Gemini).

Features:

Interactive chat interface
Utilizes Gemini-1.5-Pro-latest model for generating responses
Maintains chat history within the session
Requirements:

Python 3.7+
Streamlit
google-generativeai
API Key for Google Generative AI (Gemini) - Set as environment variable geminiapi_key
Running the application:

Install the required libraries:
pip install streamlit google-generativeai

Set the geminiapi_key environment variable with your API key.
Run the Streamlit app:
streamlit run your_script_name.py

Code Explanation:

Import Libraries:
Streamlit for the user interface.
google.generativeai to access and interact with Gemini.
os to manage environment variables.
Configure Generative AI:
Sets the API key for authentication.
Session State Initialization:
Creates an empty list called messages in the session state to store chat history.
response function:
Takes user input as user_prompt.
Configures Gemini model (gemini-1.5-pro-latest) with the system instruction to act as "Ai Assistance."
Starts a chat session.
Sends the user prompt to the model and returns the model's response.
Handles potential errors during API access.
main function:
Sets the title of the Streamlit app to "AI Chatbot."
Displays the initial message from the AI.
Gets user input from the chat input box.
Displays the chat history from the session state.
Sends the user input to the response function and gets the AI's reply.
Displays the AI's response and updates the session state with the new messages.
Running the app:
Standard code to execute the main function when the script is run.
To-Do (Potential Enhancements):

User Interface:
Improve styling and layout for a better user experience.
Add options to clear chat history or start a new conversation.
Functionality:
Implement different AI models or allow users to choose between them.
Explore advanced features like text summarization, translation, etc.
Error Handling:
Provide more specific error messages for better debugging.
