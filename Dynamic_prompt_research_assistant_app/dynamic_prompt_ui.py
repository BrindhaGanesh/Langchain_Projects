from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

st.header("Research Assistant Tool")

#Usually in static prompts, the user is asked to provide a research question.
# # In this dynamic prompt, we will ask the user to provide 3 inputs:

paper_input = st.selectbox(
    "Select a research paper to analyze:", ['Attention Is All You Need', 'BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding',
                                            'GPT-3: Language Models are Few-Shot Learners', 'RoBERTa: A Robustly Optimized BERT Pretraining Approach'])

style_input = st.selectbox(
    "Select a style for the response:", ['Beginners','Formal', 'Technical','Mathematical'])

length_input = st.selectbox(
    "Select the length of the response:", ['Short', 'Medium', 'Long'])

# Prompt template to use these inputs
template = PromptTemplate(
    
    template="""
    Summarize the paper '{paper_input}' and provide a {length_input} response in a {style_input} style.
    Make sure to include key concepts, methodologies, and findings.Include any relevant equations or mathematical expressions if applicable.
    """,
    input_variables=["paper_input", "style_input", "length_input"]
)

user_input = template.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
})

if st.button("Submit"):
        llm = ChatOpenAI()
        response = llm.invoke(user_input)
        st.write("Response from LLM:")
        st.write(response.content)
    