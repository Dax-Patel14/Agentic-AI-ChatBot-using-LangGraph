import streamlit as st

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

     # first add message to message_history
    st.session_state['message_history'].append({'role': 'assistant', 'content': user_input})
    with st.chat_message('assistant'):
        st.text(user_input)
