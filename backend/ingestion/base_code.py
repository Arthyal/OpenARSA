import logging 

logging.basicConfig(
    filename='logs/ingestions.log',
    level=logging.INFO,
    format ="%(asctime)s - %(levelname)s -%(message)s",
    filemode="w"
)

class BaseIngestor:
    def __init__ (self, source_name):
        self.source_name= source_name

    def fetch(self):
        raise NotImplementedError
    
    def parser(self,raw_data):
        raise NotImplementedError
    
    def run (self):
        try:
            logging.info(f"starting ingestion:{self.source_name}")
            raw_data=self.fetch()
            parsed_data=self.parser(raw_data)
            logging.info(f"Ingestion process completed:{self.source_name}")
            return parsed_data
        except Exception as e:
            logging.error(f"error in {self.source_name}:{str(e)}")
            return []
        