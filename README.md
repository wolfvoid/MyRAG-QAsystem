# MyRAG-QAsystem
A simple try on RAG &amp; LLM, 2025

## Quick start

```

```

## Struct tree

```
rag_project/
│
├── data/                  # 数据存储和处理模块
│   ├── __init__.py
│   ├── preprocess.py      # 数据预处理脚本，负责清洗、分词、嵌入等
│   ├── load_data.py       # 数据加载脚本，负责从外部源导入数据（如CSV、PDF等）
│   ├── embedding.py       # 生成文档嵌入的脚本
│   └── index.py           # FAISS索引构建脚本
│
├── retrieval/             # 检索模块
│   ├── __init__.py
│   ├── faiss_search.py    # 使用FAISS进行相似性检索
│   ├── query_processing.py# 处理查询并准备索引进行检索
│   └── utils.py           # 辅助工具，如向量计算、距离度量等
│
├── generation/            # 生成模块
│   ├── __init__.py
│   ├── model.py           # 生成模型的封装（如GPT、T5）
│   ├── pipeline.py        # 生成和检索的集成逻辑
│   └── postprocess.py     # 生成结果后处理（如去除不相关内容、格式化等）
│
├── config/                # 配置文件和参数
│   ├── __init__.py
│   ├── config.py          # 配置文件（如模型路径、数据源、检索参数等）
│   └── logging_config.py  # 日志配置文件
│
├── tests/                 # 测试模块
│   ├── __init__.py
│   ├── test_data.py       # 测试数据处理模块
│   ├── test_retrieval.py  # 测试检索模块
│   └── test_generation.py # 测试生成模块
│
├── requirements.txt       # 项目依赖
├── run.py                 # 主入口脚本，运行RAG应用
└── README.md              # 项目说明文档

```

Thanks

icons from: https://www.flaticon.com/

