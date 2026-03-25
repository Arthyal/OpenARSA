import json
from langchain_core.documents import Document

class document_builder():
    
    def __init__(self):
        with open('data/raw/data_cleaned.json','r') as f:
            self.data=json.load(f)
      
    def convert_document(self):
        documents=[]
        
        for item in self.data:
            content= f"""
            Title:{item['title']}
            Summary:{item['summary']}
            Keywords:{' , '.join(item['keywords'])}
            """

            metadata={"source": item.get("source"),
            "timestamp": item.get("timestamp"),
            "keywords": item.get("keywords"),
            "title": item.get("title")
            }

        doc=Document(
            page_content=content,
            metadata=metadata
        )

        documents.append(doc)

        return documents
        
