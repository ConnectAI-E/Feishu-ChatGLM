# Feishu-ChatGLM
🍎 一套使用chatGLM模型，能够调用本地知识库的聊天机器人实现方案。  

### 实现思路  
预计使用使用python为主要开发语言，调用huggingface中的chatGLM模型并实现对话api，利用langchain框架中的 Agent 和 Indexes 模块来处理对话角色和私有数据库的逻辑。

🚀 预计需要完成的功能列表:

✨ 可以添加更多你们能想到的或你们想要的功能

- [ ] python版飞书机器人实现  
- [ ] ChatGLM 聊天 api 实现  
- [ ] 利用 langchain 的 agent 模块实现多角色的丝滑转换能力  
- [ ] 利用 langchain 的 indexes 模块实现两种类型的本地知识读取  
  - [ ] 一个文件夹内的多个txt文件读取和索引  
  - [ ] 一个超长文本文件的分片读取和索引  
- [ ] 两种chatGLM与本地知识交互类型的逻辑开发  
  - [ ] 预设部分知识嵌入的聊天机器人实现
  - [ ] 根据用户输入内容动态处理需要嵌入的知识内容实现
