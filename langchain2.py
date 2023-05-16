# -*- coding: utf-8 -*-
"""Langchain2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_guPwGeLjVPkSLVw2PiFczrFpBIe486c
"""

from langchain.indexes import VectorstoreIndexCreator
from dotenv import dotenv_values
import os
os.environ["OPENAI_API_KEY"] = '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'
from langchain.document_loaders import  TextLoader
loader1 = TextLoader('./NP.txt')
loader2 = TextLoader('./project_management.txt')
index = VectorstoreIndexCreator().from_loaders([loader1,loader2])
index.query('What is project sickness?')

from langchain.indexes import VectorstoreIndexCreator
from dotenv import dotenv_values
import os
os.environ["OPENAI_API_KEY"] = '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'
from langchain.document_loaders.chatgpt import ChatGPTLoader
loader = ChatGPTLoader(log_file='./conversations.json', num_logs=1)
loader.load()
from langchain.document_loaders import  ChatGPTLoader
loader1 = ChatGPTLoader('./conversations.json')
index = VectorstoreIndexCreator().from_loaders([loader1])
index.query('what is tcp?')