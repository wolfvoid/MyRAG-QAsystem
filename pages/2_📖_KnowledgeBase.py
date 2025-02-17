import streamlit as st
import os
import time
import pandas as pd

st.set_page_config(page_title="KnowledgeBase", page_icon="📖")
st.title("KnowledgeBase")

# 确保 uploads 目录存在
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# 获取当前 uploads 目录中的所有文件信息


def get_uploaded_files():
    files = []
    for filename in os.listdir(UPLOAD_FOLDER):
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.isfile(filepath):
            file_info = {
                "File Name": filename,
                "Type": filename.split('.')[-1] if '.' in filename else "Unknown",
                "Size (KB)": round(os.path.getsize(filepath) / 1024, 2),
                "Modified Time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(filepath))),
            }
            files.append(file_info)
    return pd.DataFrame(files) if files else pd.DataFrame(columns=["File Name", "Type", "Size (KB)", "Modified Time"])


# 上传文件功能
uploaded_file = st.file_uploader(
    "Choose a file", type=["pdf", "txt", "docx", "md"])

if uploaded_file is not None:
    save_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)

    if os.path.exists(save_path):
        st.error(f"File {uploaded_file.name} already exists! Upload denied.")
    else:
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"File {uploaded_file.name} uploaded successfully!")
        st.rerun()  # 重新运行以更新文件列表

# 显示上传的文件列表
st.subheader("Knowledge List")
uploaded_files_df = get_uploaded_files()

if not uploaded_files_df.empty:
    # **手动添加表头**
    col1, col2, col3, col4, col5 = st.columns([3, 2, 2, 3, 2])
    col1.write("📄 File Name")
    col2.write("📂 Type")
    col3.write("📏 Size (KB)")
    col4.write("🕒 Modified Time")
    col5.write("🗑️ Delete")
    # 使用 Streamlit 的 columns 布局在表格中添加删除按钮
    for index, row in uploaded_files_df.iterrows():
        col1, col2, col3, col4, col5 = st.columns([3, 2, 2, 3, 2])  # 设置列宽
        col1.write(row["File Name"])
        col2.write(row["Type"])
        col3.write(f"{row['Size (KB)']} KB")
        col4.write(row["Modified Time"])
        if col5.button("🗑️", key=row["File Name"]):  # 每个文件生成唯一按钮
            os.remove(os.path.join(UPLOAD_FOLDER, row["File Name"]))
            st.warning(f"Deleted: {row['File Name']}")
            st.rerun()  # 重新运行以更新文件列表

else:
    st.write("No files uploaded yet.")
