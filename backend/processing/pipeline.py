from cleaning import clean_text
from deduplication import deduplicate
from keyword_extract import extract

def run(data):
    
    # cleaning
    data_cleaned={
        "title": clean_text(data["title"]),
        "summary": clean_text(data["summary"]),
        "authors": data["authors"],  # untouched
        "category": data["category"],
    }

    # deduplicate
    deduplicated=deduplicate(data_cleaned)

    #keywords
    texts = [
        item.get("title", "") + " " + item.get("summary", "")
        for item in deduplicated
    ]

    keywords = extract(texts)

    for i, item in enumerate(deduplicated):
        item["keywords"] = keywords[i]

    return deduplicated
