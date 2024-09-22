## Loading Data

from pymongo import MongoClient
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain.document_loaders import DirectoryLoader 
from langchain.llms import openai
from langchain.chains import retrieval_qa
import gradio as gr 
from gradio.themes.base import Base
import parameters

from dotenv import load_dotenv 
import os 
load_dotenv() 

MONGO_URI = os.getenv("MONGO_URI")
OPENAI_API_KEY = os.getenv("OPEN_AI_API_KEY")


client = MongoClient(MONGO_URI)
dbName = "Cluster1"
collectionName = "documents"
collection = client[dbName][collectionName]

loader = DirectoryLoader('./sample_files', glob='./*.txt', show_progress=True)
data = loader.load()

embeddings = OpenAIEmbeddings(OPENAI_API_KEY)

vectorStore = MongoDBAtlasVectorSearch(data, embeddings, collection=collection)


