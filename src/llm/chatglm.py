import logging
import os
import openai
from util.app_config import app_config
from util.logger import gpt_logger, app_logger
import requests
import json



def get_gpt_response(data):
    """ 调接口获得返回
    
    Args:
        data （dict) : 历史对话消息， like:
            data = {'prompt': '北方呢？用10个字回答', 'history': [["中国南方热吗？用10个字回答","中国南方热。"]]}
    Returns:
        dict : 例如：{"response":"中国北方冷。","history":[["中国南方热吗？用10个字回答","中国南方热。"],["北方呢？用10个字回答","中国北方冷。"]],"status":200,"time":"2023-04-26 02:09:24"}
    """

    
    
    """
    
    round1:
        data = {'prompt': '中国南方热吗？用10个字回答', 'history': []}
        response.text: '{"response":"中国南方热。","history":[["中国南方热吗？用10个字回答","中国南方热。"]],"status":200,"time":"2023-04-26 01:58:11"}'

    round2:
        data = {'prompt': '北方呢？用10个字回答', 'history': [["中国南方热吗？用10个字回答","中国南方热。"]]}
        response.text: '{"response":"中国北方冷。","history":[["中国南方热吗？用10个字回答","中国南方热。"],["北方呢？用10个字回答","中国北方冷。"]],"status":200,"time":"2023-04-26 02:09:24"}'
    """

    response = requests.post(app_config.CHATGLM_API_HOST, json=data)
    response_dict = json.loads(response.text)
    return response_dict



def get_chat_response(input, history=[], prompt=app_config.DEFAULT_PROMPT):
    """
    Args:
        input (str): 当前的问题
        history (list):  like: [["中国南方热吗？用10个字回答","中国南方热。"],["北方呢？用10个字回答","中国北方冷。"]]
    Return:
        str
    """ 
    data = {'prompt': input, 'history': history}
    response_dict = get_gpt_response(data)
    return response_dict.get('response')


if __name__ == "__main__":
    app_logger.info(get_chat_response())

