from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI()
chat_history = []

# Define a system message to set the context for the chatbot
system_message = SystemMessage(content="You are a helpful assistant that provides information based on the user's queries.")
human_message = HumanMessage(content="explain the concept of Dynamic Programming in simple terms.")

messages = [system_message, human_message]

# Invoke the model with the messages
response = model.invoke(messages)

messages.append(AIMessage(content=response.content))

print(messages)
