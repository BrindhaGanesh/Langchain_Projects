from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Research Assistant Tool")

user_input = st.text_input("Enter your research question:")

if st.button("Submit"):
    if user_input:
        llm = ChatOpenAI()
        response = llm.invoke(user_input)
        st.write("Response from LLM:")
        st.write(response.content)
    else:
        st.error("Please enter a research question.")