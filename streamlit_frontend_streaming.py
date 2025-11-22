import streamlit as st
from Langgraph_backend import chatbot # import chatbot object
from langchain_core.messages import HumanMessage, AIMessage
CONFIG = {'configurable': {'thread_id': 'thread-1'}}
# session_state itself is dict
# is message_history key is not present then add
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

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

    
    with st.chat_message('assistant'):

        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages' : [HumanMessage(content=user_input)]},
                config = {'configurable': {'thread_id': 'thread-1'}},
                stream_mode='messages'
            )
        )
    
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})




