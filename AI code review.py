import streamlit as st
import google.generativeai as genai
import os


########
genai.configure(api_key=os.environ["Geminiapi_key"])
########

if "messages" not in st.session_state:
   st.session_state.messages = []
    

def response(user_prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest",system_instruction="You are a helpfull AI Assitance named Ai Assistance")
        chat = model.start_chat(history=[])
        
        if user_prompt:
            res = chat.send_message(user_prompt)
            return res.text
    except :
        st.write("Error Occured while accessing the api")


def main():
    st.title("AI Chatbot")
    st.chat_message("Ai").write("How may i help you today ?")
            
    if user_prompt := st.chat_input("Enter your message here"):
        
        for message in st.session_state.messages:
                st.chat_message(message["role"]).write(message["content"])
        
        try:
            st.chat_message("user").write(user_prompt)
            st.session_state.messages.append({"role": "user", "content": user_prompt})
            
            with st.spinner("Thinking"):
                res = response(user_prompt)

            st.chat_message("ai").write(res)
            st.session_state.messages.append({"role":"ai","content":res})
            
            
        except Exception as e: 
            st.write("Try again")

    
if __name__ == "__main__":
    main()





