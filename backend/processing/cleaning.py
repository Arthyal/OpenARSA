import re

def clean_text(text:str)->str:
    if not text:
        return ""
    
    text=text.lower() 
    text=re.sub(r'\s+',' ',text)#to remove extra spaces
    text=re.sub(r'[^\w\s]','',text)# to remove special chars

    return text.strip()

def clean_record(record: dict) -> dict:
    record["title"] = clean_text(record.get("title", ""))
    record["summary"] = clean_text(record.get("summary", ""))
    record["description"] = clean_text(record.get("description", ""))

    return record