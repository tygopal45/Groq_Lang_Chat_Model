# Q & A Chatbot

import os
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

from dotenv import load_dotenv

load_dotenv()

import streamlit as st

# function to load llm model and get response

def get_groq_response(question):
    llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"),model="llama-3.3-70b-versatile",temperature=0.6,max_tokens=60)
    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content=question)
    ]
    resp = llm.invoke(messages)     
    return resp.content             # returns only the text, not the object
    return response

# Intialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input=st.text_input("Input: ", key="input")

response = get_groq_response(input)


submit = st.button("Ask the question.")

# If ask is clicked

if submit:
    st.subheader("The response is :")
    st.write(response)