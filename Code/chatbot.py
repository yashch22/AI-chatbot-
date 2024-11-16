import os
import sys
import pandas as pd
import tiktoken
from langchain.chains import ConversationChain
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.document_loaders import CSVLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Qdrant
from langchain.document_loaders import DirectoryLoader, PyPDFDirectoryLoader
from langchain.schema import Document
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from qdrant_client.http.models import PointStruct
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains.conversational_retrieval.prompts import CONDENSE_QUESTION_PROMPT
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.schema import BaseMessage
from vector_db import DB


class Chatbot:

    def __init__(self, model_name="gpt-3.5-turbo"):
        self.model_name = model_name
        self.chat_history = []
        self.df = pd.read_csv("query_response_base.csv")
        self.process_data()
        self.qa = self.generate_new_qa()

    def chat(self, query):
        # temp_var = str(self.chat_history)
        # print('======temp========',temp_var,type(temp_var))
        result = self.qa({"question": query, "chat_history":self.chat_history})
        # self.chat_history.append(query)
        return result["answer"], result["source_documents"]

    def generate_new_qa(self):
        qa = ConversationalRetrievalChain.from_llm(
            llm=ChatOpenAI(model=self.model_name),
            retriever=self.db.qdrant.as_retriever(search_type="similarity", search_kwargs={"k": 1}),
            return_source_documents=True,
            chain_type="stuff",
        )

        qa.combine_docs_chain.llm_chain.prompt = PromptTemplate.from_template(
            """
            Consider yourshelf as a customer support at ecom store who solves customers doubt. 
            Now, consider the following 
            context:  {context}. 
            Based on this context, answer the following
            Question: {question} .
             
            Please ensure your answer should be rephrased but it should be based on the context
            Helpful Answer:"""
        )

        return qa

    def process_data(self):
        self.df["new_column"] = "Question: " + self.df["Question"] + ", Answer: " + self.df["Answer"]
        self.data = self.df["new_column"].to_list()
        self.db = DB(location=":memory:", collection_name="startups")
        self.db.import_data(self.data)