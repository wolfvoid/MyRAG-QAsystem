# 基于siliconflow的API
import requests
import json
import os


def get_chat(prompt, api_key, stream=False, model="deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"):
    api_url = "https://api.siliconflow.cn/v1/chat/completions"
    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "model": model,
        "frequency_penalty": 1,
        "max_tokens": 4096,
        "n": 1,             # 生成几个结果
        "stream": stream,    # 是否流式输出















































































































































































        --
        "temperature": 1,   # 0-1之间，越大越随机
        "top_k": 10,        # 保留概率最大的前k个token
        "top_p": 0.5        # 保留概率之和
    }
    headers = {"Authorization": api_key, "Content-Type": "application/json"}
    response = requests.request("POST", api_url, json=payload, headers=headers)
    if response.status_code == 200:
        response_json = response.json()
        formatted_json = json.dumps(
            response_json, indent=4, ensure_ascii=False)
        return formatted_json
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None


def get_vision_chat(prompt, base64_image, api_key, model="Pro/Qwen/Qwen2-VL-7B-Instruct"):
    api_url = "https://api.siliconflow.cn/v1/chat/completions"
    payload = {
        "model": model,
        "max_tokens": 1024,
        "n": 1,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}",
                            "detail": "auto"
                        },
                    }
                ]
            }
        ]
    }
    headers = {"Authorization": api_key, "Content-Type": "application/json"}
    response = requests.request("POST", api_url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        content = data['choices'][0]['message']['content']
        return content
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None


def get_embeddings(texts, api_key, model="BAAI/bge-m3", dimensions=None):
    api_url = "https://api.siliconflow.cn/v1/embeddings"
    payload = {
        "input": texts,
        "model": model,
        "encoding_format": "float",
    }
    headers = {"Authorization": api_key, "Content-Type": "application/json"}
    response = requests.request("POST", api_url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()  # 使用 json() 来直接解析响应
        embeddings = [item['embedding'] for item in data['data']]  # 获取所有文本的嵌入
        return embeddings
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None


def get_rerank(query, api_key, documents, model="BAAI/bge-reranker-v2-m3"):
    """
    query = "small animals"
    documents = ["little dog", "big cat", "car"]
    ==> [0.9, 0.8, 0.1]
    """
    api_url = "https://api.siliconflow.cn/v1/rerank"
    payload = {
        "query": query,
        "documents": documents,
        "model": model,
        "max_chunks_per_doc": 300,
        "overlap_tokens": 100,
        "return_documents": False,
        # "top_n": 2
    }
    headers = {"Authorization": api_key, "Content-Type": "application/json"}
    response = requests.request("POST", api_url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()  # 使用 json() 来直接解析响应
        scores = [item['relevance_score']
                  for item in data['results']]  # 获取所有的相关性分数
        return scores
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None
