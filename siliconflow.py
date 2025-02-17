# 一个单独的api验证示例
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os

dot_env_path = "E:\Code_files\LLM\.env"
_ = load_dotenv(find_dotenv(), verbose=True)  # 加载.env文件
api_key = os.getenv("API_KEY2")
api_base_url = os.getenv("API_BASE_URL")

client = OpenAI(api_key=api_key, base_url=api_base_url)
response = client.chat.completions.create(
    model='Qwen/Qwen2.5-Coder-7B-Instruct',
    messages=[
        {'role': 'user',
         'content': "中国大模型行业2025年将会迎来哪些机遇和挑战"}
    ],
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content, end='')
