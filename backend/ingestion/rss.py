import feedparser
from base_code import BaseIngestor
from datetime import datetime
import json 

class RSSFeedIngestor(BaseIngestor):
    def __init__(self,url):
        super().__init__('rss')
        self.url=url

    def fetch(self):
        return feedparser.parse(self.url)
    
    def parser(self,raw_data):
        items=[]

        for entry in raw_data.entries:
            items.append({
                "source": "rss",
                "title": entry.title,
                "summary": entry.summary if "summary" in entry else "",
                "link": entry.link,
                "published": entry.get("published", ""),
                #"timestamp": datetime.now(datetime.timezone.utc).isoformat()
            })
        
        with open ("data/raw/data.json","w") as f:
                json.dump(items,f,indent=2)
    
rss=RSSFeedIngestor("https://techcrunch.com/feed/")
rss.run()