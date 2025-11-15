import streamlit as st
from Langgraph_backend import chatbot # import chatbot object
from langchain_core.messages import HumanMessage, AIMessage
CONFIG = {'configurable': {'thread_id': 'thread-1'}}
# session_state itself is dict
# is message_history key is not present then add
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []


# To maintain conversation history
# message_history = [] 
# as user press enter this file runs again and message_history gets empty
# solution is session_state

# show past message history 
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


#{'role': 'user', 'content':'Hi'}
#{'role': 'assistant', 'content': 'Hello'}

user_input = st.chat_input('Type here')

if user_input:

    # first add message to message_history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]},config=CONFIG )
    ai_message = response['messages'][-1].content
     # first add message to message_history
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
    with st.chat_message('assistant'):
        st.text(ai_message)
