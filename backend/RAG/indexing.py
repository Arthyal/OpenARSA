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
        self.db_path = "data/chroma_db"

   
    
    def indexing(self,docs):

        vector_store = Chroma(
        embedding_function=self.model,
        persist_directory=self.db_path,
        collection_name='sample'
        )
        
        ids = [str(hash(doc.page_content)) for doc in docs] # to prevent duplication
        vector_store.add_documents(docs,id=ids)
        vector_store.persist()

        return vector_store