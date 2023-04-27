# Note: The openai-python library support for Azure OpenAI is in preview.

import logging
import os
import openai
from util.app_config import app_config
from util.logger import gpt_logger, app_logger
if app_config.LLM == 'azure':
    openai.api_type = "azure"
    openai.api_base = app_config.AZURE_API_HOST
    openai.api_version = "2023-03-15-preview"
    openai.api_key = app_config.AZURE_API_KEY
elif app_config.LLM == 'openai':
    openai.api_key = app_config.OPENAI_KEY
    openai.api_base = app_config.API_URL





def get_single_response(message, prompt=app_config.DEFAULT_PROMPT):
    return get_chat_response([{"role": "user", "content": message}])


def get_chat_response(chat_history, prompt=app_config.DEFAULT_PROMPT):
    """传入对话记录返回一个字符串

    Args:
        chat_history (list of dict): 对话记录
        prompt (str, optional): . Defaults to app_config.DEFAULT_PROMPT.

    Returns:
        str: GPT返回的一句话
    """
    messages = [{"role": "system", "content": prompt}, *chat_history]
    gpt_logger.info("GPT request: %s", messages)
    response = get_gpt_response(messages)
    if "choices" not in response:
        gpt_logger.info("GPT raw response: %s", response)
        return ""
    choice = response["choices"][0]  # type: ignore
    if "message" not in choice:
        gpt_logger.info("GPT raw response: %s", response)
        return ""
    message = choice["message"]
    if "content" in message and "role" in message and message["role"] == "assistant":
        gpt_logger.info("GPT response: %s", message["content"])
        return message["content"]
    gpt_logger.info("GPT raw response: %s", response)
    return ""


def get_gpt_response(messages):
    """ 调接口获得返回
    
    Args:
        messages （list of dict) : 历史对话消息， like:
            messages=[{"role": "system", "content": '你是一个AI助手'}, {"role": "user", "content": '你好'}]
    Returns:
        <class 'openai.openai_object.OpenAIObject'>, 类json结构，like: 
            {'choices': [{'finish_reason': 'stop', 'index': 0, 'message': {'content': '你好！我可以帮助你完成一些任务，有什么我能帮你的吗？', 'role': 'assistant'}}], 'created': 1682473612, 'id': 'chatcmpl-79OX62tr98OWmtJgZ70Rk0BzrFsGx', 'model': 'gpt-3.5-turbo-0301', 'object': 'chat.completion', 'usage': {'adjust_total': 41, 'completion_tokens': 28, 'final_total': 1, 'pre_token_count': 4096, 'pre_total': 42, 'prompt_tokens': 22, 'total_tokens': 50}}

    """
    response = openai.ChatCompletion.create(
        model=app_config.GPT_MODEL,
        messages=messages,
        stop=None)
    return response


if __name__ == "__main__":
    app_logger.info(get_chat_response([{"role": "assistant", "content": "Hello, how can I help you?"}, {
                    "role": "user", "content": "Tell me a joke."}]))
    app_logger.info(get_single_response("什么是战争国债"))
