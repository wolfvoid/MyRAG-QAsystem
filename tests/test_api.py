import os
import sys
from dotenv import load_dotenv, find_dotenv
# 将上级目录添加到 sys.path 中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from api.siliconflow_api import get_embeddings, get_rerank, get_chat, get_vision_chat
import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def test_embeddings(api_key):
    print("test_embeddings")
    text_query = ["爱莉希雅是谁？", "爱莉希雅是什么动漫的角色？"]
    vec = get_embeddings(texts=text_query, api_key=api_key)[0]
    print(f"total dimensions: {len(vec)}")
    print(f"first 10 elements: {vec[:10]}")

def test_rerank(api_key):
    print("test_rerank")
    query = "崩坏三角色"
    documents = ["爱莉希雅", "布洛妮娅", "黑天鹅"]
    reranked = get_rerank(query=query, documents=documents, api_key=api_key)
    print(reranked)

def test_vision_chat(api_key):
    print("test_vision_chat")
    image_path = r"C:\Users\y\Desktop\爱莉希雅.png"
    base64_image = encode_image(image_path)
    prompt = "What is the name of this character?"
    print(get_vision_chat(prompt, base64_image, api_key))

def test_chat(api_key):
    print("test_chat")
    prompt = "What is the name of this character?"
    print(get_chat(prompt, api_key))

def test():
    print("test_api")
    dot_env_path = "E:\Code_files\LLM\.env"
    _ = load_dotenv(find_dotenv(), verbose=True) # 加载.env文件
    api_key = os.getenv("API_KEY")
    test_embeddings(api_key)
    test_rerank(api_key)
    test_vision_chat(api_key)
    test_chat(api_key)

if __name__ == "__main__":
    test()
