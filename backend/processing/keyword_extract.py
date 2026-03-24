from sklearn.feature_extraction.text import TfidfVectorizer


def extract(data,top_k=5):
    vectorizer=TfidfVectorizer(
        stop_words='english'
    )

    vectorizer.fit(data)
    tfidf_matrix=vectorizer.transform(data)
    feature_names=vectorizer.get_feature_names_out()
    keywords_list=[]

    for row in tfidf_matrix:
        scores=row.to_array()
        top_scores=scores.argsort()[-top_k:][::1]
        keywords=[feature_names[i] for i in top_scores]
        keywords_list.append(keywords)

    return keywords_list
    
    #print(type(tfidf_matrix))

