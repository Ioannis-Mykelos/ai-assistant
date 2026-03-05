import os

import streamlit as st
from langchain_openai import ChatOpenAI

##############################
# SETTINGS
##############################

# Load From .env File
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
REMOTE_MODEL_NAME = os.environ.get("REMOTE_MODEL_NAME")
REMOTE_BASE_URL = os.environ.get("REMOTE_BASE_URL")

# Initialize Big Cloud Model
cloud_llm = ChatOpenAI(
    model=REMOTE_MODEL_NAME, api_key=OPENROUTER_API_KEY, base_url=REMOTE_BASE_URL
)
# Select Cloud Model
llm = cloud_llm

##############################
# GUI
##############################

st.title("Personal AI assistant chatbot")

# Initialize Chat Message Memory
st.session_state.setdefault("messages", [])

# Display Chat Message History from Memory
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Collect User Prompt
prompt = st.chat_input("type you message...")

# If New User Prompt was Submitted
if prompt:
    # Add the New User Prompt to Memory
    st.session_state["messages"].append({"role": "user", "content": prompt})
    # Display the New User Prompt
    with st.chat_message("user"):
        st.write(prompt)

    context = ""

    # Combine Chat History as Context to the New Prompt
    for msg in st.session_state["messages"]:
        context += msg["role"] + ": " + msg["content"]

    # Generate Model Response from User Prompt + Context
    response = llm.invoke(context)

    # Add the New Model Response to Memory
    st.session_state["messages"].append(
        {"role": "assistant", "content": response.content}
    )
    # Display the New Model Response
    with st.chat_message("assistant"):
        st.write(response.content)
