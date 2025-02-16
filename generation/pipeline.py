# generation/pipeline.py

from .model import generate_text
from .postprocess import clean_generated_text

def generate_response(query, context=None):
    """
    这是一个生成流程的封装，负责处理整个从输入到输出的过程
    """
    # 1. 输入处理（例如，可以在这里进行一些前处理，比如拼接上下文）
    input_text = f"Question: {query}\nContext: {context}" if context else f"Question: {query}"

    # 2. 调用模型生成文本
    generated_text = generate_text(input_text)

    # 3. 后处理（如清理生成的文本）
    cleaned_text = clean_generated_text(generated_text)

    return cleaned_text
