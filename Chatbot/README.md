# 📚 Simple chatbot app 
This is a small project I made using **LangChain** and **OpenAI**.

It is a simple chatbot application.
User can ask questions to the chatbot until the user types exit.
This application is not useful for real problems. It does not remember the previous questions, so there is no context.

Solution : we need to maintain the chat history and send the whole history to the LLM model. check: Chatbot_with_context_app.py 

# 📚 Chatbot with context app
we store each user input and chatbot response in a list as a history and send the history to the model 
now the model will able to get the context 

Problem : when we add both user input and response to a list and send to the model, model cannot understand which message is sent by user and which msg is sent by model as a reponse. 

Solution : Messages parameter , for any conversational chatbots the labelling of msgs are important


 







 




