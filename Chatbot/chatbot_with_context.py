from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

load_dotenv()

model = ChatOpenAI()

chat_history = [SystemMessage(content="You are a helpful AI assistant")]

# run the program infinitely until the user types "exit"
while True:
    user_input = input("You: ")
    #when the user types any input, append it to the chat history
    #chat_history.append(user_input)
    chat_history.append(HumanMessage(content=user_input))
    
    if user_input.lower() == "exit":
        break
    # invoke the model with the chat history
    #in invoke method we can pass either a single string or a list of strings
    #here we are passing the chat history as a list of strings
    response = model.invoke(chat_history)
    
    # append the response to the chat history
    #chat_history.append(response.content)
    chat_history.append(AIMessage(content=response.content))
    
     
    
    print(f"Chatbot: {response.content}")

print(chat_history)