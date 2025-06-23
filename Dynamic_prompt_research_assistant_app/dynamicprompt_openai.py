import streamlit as st
import os
from openai import OpenAI  # New import for v1.x
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Initialize the client with the API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Prompt template
template = """
Explain the concept of {topic} in simple terms for a {audience_type}.
Use an example relevant to {domain}.
"""

# Streamlit UI
st.title("🧠 Concept Explainer")
st.write("Fill out the form and click Generate to get an explanation.")

# Input fields
topic = st.text_input("Topic", "Fourier Transform")
audience_type = st.selectbox("Audience Type", ["high school student", "engineer", "child", "general public"])
domain = st.selectbox("Domain", ["audio signal processing", "physics", "finance", "healthcare"])

if st.button("Generate Explanation"):
    final_prompt = template.format(
        topic=topic,
        audience_type=audience_type,
        domain=domain
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": final_prompt}
            ],
            temperature=0.7
        )

        explanation = response.choices[0].message.content
        st.subheader("📝 Explanation")
        st.write(explanation)

    except Exception as e:
        st.error(f"Error: {e}")

