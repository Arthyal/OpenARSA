from langchain_huggingface import HuggingFaceEmbeddings 
import os 
from langchain_community.vectorstores import Chroma
from processing.document_builder import document_builder


#os.environ['HF_HOME']='D:\research_assistant\logs'

class embedding():
    def __init__(self):
        self.model=HuggingFaceEmbeddings(
        model_name='sentence-transformers/all-MiniLM-L6-v2'
        )

    def embedder(self,text):
        return self.model.embed_query(text)
    
    def indexing(self,texts):
        
        embedding=self.embedder(texts)

