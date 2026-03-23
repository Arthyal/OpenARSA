import feedparser 
from datetime import datetime
from base_code import BaseIngestor
import json 

class ArxivIngestor(BaseIngestor):
    def __init__(self,query="machine learning",max_results=5):
        super().__init__("arxiv")
        self.query=query
        self.max_results=max_results

    def fetch(self):
        url=f"http://export.arxiv.org/api/query?search_query=all:{self.query}&start=0&max_results={self.max_results}"
        return feedparser.parse(url)
    
    def parser(self,raw_data):
        results=[]
        for entry in raw_data.entries:
            results.append({
                "source":"arxiv",
                "title":entry.title,
                "summary":entry.summary,
                "published":entry.published,
                "link":entry.link,
                "timestamp":datetime.now(datetime.timezone.utc).isoformat()
            })

            with open ("data/raw/data.json","w") as f:
                json.dump(results,f,indent=2)

arxiv=ArxivIngestor()
arxiv.run()