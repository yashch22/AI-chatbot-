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


# Replace the below empty string with your open AI key
os.environ["OPENAI_API_KEY"] = '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'

class DB:

    def __init__(self, location=":memory:", collection_name="startups"):
        self.location = location
        self.collection_name = collection_name
        self.qdrant = QdrantClient()
        self.embed_model  = OpenAIEmbeddings(openai_api_key="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")

    def import_data(self, data):
        list_of_documents = [Document(page_content=d, metadata=dict(page=i)) for i, d in enumerate(data)]
        self.qdrant = Qdrant.from_documents(
        list_of_documents, self.embed_model, 
        # path="/Users/yash/Downloads/Cognitive_assignment/qdrant_storage/", 
        location = ":memory:",
        collection_name="startups",
            )
        # for doc in list_of_documents:
        #     self.qdrant.add_document(self.collection_name, doc)

    def search(self, query, k=1):
        return self.qdrant.search(self.collection_name, query, k=k, distance=Distance.COSINE)