import streamlit as st
# https://docs.streamlit.io/develop/api-reference
import os

# 设置页面标题
st.set_page_config(page_title="RAG Web Interface", layout="centered")
st.title("RAG Web Interface")
st.header("Chat with the RAG System")
# 存储对话记录（首次访问时初始化）
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# 第一次访问触发气球特效
if 'first_visit' not in st.session_state:
    st.session_state.first_visit = True  # 标记为第一次访问
if st.session_state.first_visit:
    st.balloons()  # 触发气球特效
    st.session_state.first_visit = False  # 只触发一次

# 显示对话历史
for message in st.session_state.chat_history:
    if message['role'] == 'user':
        # 用户消息（右侧）
        st.markdown(f"""
            <div style="text-align: right; margin: 10px;">
                <div style="display: inline-block; background-color: #DCF8C6; border-radius: 15px; padding: 10px; max-width: 70%; word-wrap: break-word;">
                    <span>{message['text']}</span>
                </div>
                <div style="display: inline-block; margin-left: 10px;">
                    <img src="./app/static/portrait.png" width="30" height="30" style="border-radius: 50%; vertical-align: top;" />
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        # RAG 系统消息（左侧）
        st.markdown(f"""
            <div style="text-align: left; margin: 10px;">
                <div style="display: inline-block; margin-right: 10px;">
                    <img src="./app/static/sparkles.png" width="30" height="30" style="border-radius: 50%; vertical-align: top;" />
                </div>
                <div style="display: inline-block; background-color: #EAEAEA; border-radius: 15px; padding: 10px; max-width: 70%; word-wrap: break-word;">
                    <span>{message['text']}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)


# 用户输入框和提交按钮
user_input = st.text_input("You: ", "")
if st.button("Send"):  # 按下按钮时发送消息
    if user_input:
        st.session_state.chat_history.append({"role": "user", "text": user_input})
        rag_response = f"{user_input[::-1]}"  # 举个例子，反转用户输入返回
        st.session_state.chat_history.append({"role": "rag", "text": rag_response})
        st.rerun()  # 重新运行应用程序以更新对话历史



# 上传文档部分
st.header("Upload Document to RAG System")
# 上传文件
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "txt", "docx", "md"])
if uploaded_file is not None:
    # 保存上传的文件到临时目录或一个指定的目录
    save_path = os.path.join("uploads", uploaded_file.name)
    # 创建目录，如果没有的话
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    # 将文件写入
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    # 提示用户文件上传成功
    st.success(f"File {uploaded_file.name} uploaded successfully!")
