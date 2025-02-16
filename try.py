
from openai import OpenAI
import streamlit as st

st.title("ChatGPT-like clone")

if "api_key" not in st.session_state:
    st.balloons()  # 第一次访问触发气球特效
    from dotenv import load_dotenv, find_dotenv
    import os
    dot_env_path = "E:\Code_files\LLM\.env"
    _ = load_dotenv(find_dotenv(), verbose=True) # 加载.env文件
    st.session_state["api_key"] = os.getenv("API_KEY2")
    st.session_state["api_base_url"] = os.getenv("API_BASE_URL")
    st.session_state["openai_model"] = "Qwen/Qwen2.5-Coder-7B-Instruct"

if "messages" not in st.session_state:
    st.session_state.messages = []

client = OpenAI(api_key=st.session_state["api_key"], base_url=st.session_state["api_base_url"])

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
